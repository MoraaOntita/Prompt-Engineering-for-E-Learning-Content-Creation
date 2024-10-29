import os
import json
import datetime
from src.ELearning.entity.config_entity import MetadataConfig

class MetadataExtraction:
    def __init__(self, config: MetadataConfig):
        self.config = config
        os.makedirs(self.config.root_dir, exist_ok=True)

    def load_json_data(self, json_path):
        with open(json_path, 'r') as json_file:
            return json.load(json_file)

    def create_metadata(self, extracted_data, source_file):
        metadata = {
            "source_file": source_file,
            "extraction_date": str(datetime.datetime.now()),
            "number_of_slides_or_pages": len(extracted_data),
            "details": []
        }

        for item in extracted_data:
            if 'slide_number' in item:
                metadata['details'].append({
                    "slide_number": item['slide_number'],
                    "text_length": len(item['text']),
                    "image_count": len(item['images'])
                })
            elif 'page_number' in item:
                metadata['details'].append({
                    "page_number": item['page_number'],
                    "text_length": len(item['text']),
                    "image_count": len(item['images'])
                })

        return metadata

    def save_metadata(self, metadata, file_name):
        metadata_path = os.path.join(self.config.root_dir, file_name)
        with open(metadata_path, 'w') as metadata_file:
            json.dump(metadata, metadata_file, indent=4)
        return metadata_path

    def process(self, pptx_json_path, pdf_json_paths):
        # Process PPTX data
        pptx_data = self.load_json_data(pptx_json_path)
        pptx_metadata = self.create_metadata(pptx_data, 'downloaded_presentation.pptx')
        pptx_metadata_path = self.save_metadata(pptx_metadata, self.config.pptx_file_name)

        print(f"PPTX metadata saved to {pptx_metadata_path}")

        # Process PDF data
        for pdf_json_path in pdf_json_paths:
            pdf_data = self.load_json_data(pdf_json_path)
            pdf_file_name = os.path.basename(pdf_json_path)
            pdf_metadata = self.create_metadata(pdf_data, pdf_file_name)
            pdf_metadata_path = self.save_metadata(pdf_metadata, f"{self.config.pdf_file_prefix}{pdf_file_name}")
            
            print(f"Metadata for {pdf_file_name} saved to {pdf_metadata_path}")
