from src.ELearning.config.configuration import Configuration
from src.ELearning.components.metadata_extraction import MetadataExtraction
import os

class MetadataExtractionPipeline:
    def __init__(self):
        self.config = Configuration().get_metadata_config()

    def main(self):
        metadata_extraction = MetadataExtraction(self.config)

        # Specify the paths to your extracted data JSON files
        pptx_json_path = os.path.join("artifacts/data_ingestion_pptx", "extracted_data.json")
        pdf_json_paths = [
            os.path.join("artifacts/ingest_pdf", "extracted_data_1umzTCsbBmuFx4xz9DSMI82oq21tHhbKL.json"),
            os.path.join("artifacts/ingest_pdf", "extracted_data_13oqVt9LYdESPS8XNYFLhSLZMkZk52JXG.json")
        ]
        
        metadata_extraction.process(pptx_json_path, pdf_json_paths)
