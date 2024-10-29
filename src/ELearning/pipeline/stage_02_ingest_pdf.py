from src.ELearning.config.configuration import Configuration
from src.ELearning.components.ingest_pdfs import DataIngestionPDF

class DataIngestionPDFPipeline:
    def __init__(self):
        self.config = Configuration().get_data_ingestion_pdf_config()

    def main(self):
        data_ingestion = DataIngestionPDF(self.config)
        data_ingestion.initiate_data_ingestion()