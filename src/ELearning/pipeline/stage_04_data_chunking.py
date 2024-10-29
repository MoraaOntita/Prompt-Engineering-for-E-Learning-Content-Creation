from src.ELearning.config.configuration import Configuration
from src.ELearning.components.chunking import DataChunking
import os

class DataChunkingPipeline:
    def __init__(self):
        self.config = Configuration().get_chunking_config()

    def main(self):
        chunking = DataChunking(self.config)

        # Load and chunk PPTX data
        pptx_json_path = os.path.join("artifacts/data_ingestion_pptx", "extracted_data.json")
        pptx_data = chunking.load_json_data(pptx_json_path)
        pptx_text = " ".join([item.get('text', '') for item in pptx_data])
        
        chunking.save_chunks_and_metadata(
            'downloaded_presentation.pptx',
            pptx_text,
            self.config.pptx_chunk_filename,
            self.config.pptx_metadata_filename
        )

        # Load and chunk PDF data
        pdf_json_paths = [
            os.path.join("artifacts/ingest_pdf", "extracted_data_1umzTCsbBmuFx4xz9DSMI82oq21tHhbKL.json"),
            os.path.join("artifacts/ingest_pdf", "extracted_data_13oqVt9LYdESPS8XNYFLhSLZMkZk52JXG.json")
        ]
        for pdf_json_path in pdf_json_paths:
            pdf_data = chunking.load_json_data(pdf_json_path)
            pdf_text = " ".join([item.get('text', '') for item in pdf_data])
            pdf_filename = os.path.basename(pdf_json_path).replace('extracted_data_', '').replace('.json', '')

            chunking.save_chunks_and_metadata(
                pdf_filename,
                pdf_text,
                f"{self.config.pdf_chunk_filename_prefix}{pdf_filename}.json",
                f"{self.config.pdf_metadata_filename_prefix}{pdf_filename}.json"
            )
