import logging
from src.ELearning.config.configuration import Configuration
from src.ELearning.components.data_ingestion_pptx import DataIngestion

class DataIngestionPipeline:
    def __init__(self):
        self.config = Configuration()
        self.data_ingestion_config = self.config.get_data_ingestion_pptx_config()

    def main(self):
        data_ingestion = DataIngestion(self.data_ingestion_config)
        data_ingestion.initiate_data_ingestion()
