import yaml
import os
import logging
from src.ELearning.constants import CONFIG_FILE_PATH
from src.ELearning.entity.config_entity import DataIngestionConfig
from src.ELearning.entity.config_entity import DataIngestionPdfConfig

class Configuration:
    def __init__(self, config_file_path=CONFIG_FILE_PATH):
        self.config_file_path = config_file_path
        self.config = self.read_yaml_file(self.config_file_path)

    def read_yaml_file(self, file_path):
        logging.info(f"Reading configuration file from {file_path}")
        with open(file_path, 'r') as file:
            return yaml.safe_load(file)

    def get_data_ingestion_pptx_config(self) -> DataIngestionConfig:
        data_ingestion_pptx_config = self.config.get('data_ingestion_pptx', {})
        return DataIngestionConfig.from_dict(data_ingestion_pptx_config)
    
    def get_data_ingestion_pdf_config(self) -> DataIngestionPdfConfig:
        pdf_config = self.config["pdf_data_ingestion"]
        return DataIngestionPdfConfig(
            root_dir=pdf_config["root_dir"],
            pdf_links=pdf_config["pdf_links"]
        )