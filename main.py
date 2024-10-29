import logging
from src.ELearning.pipeline.stage_01_data_ingestion_pptx import DataIngestionPipeline
from src.ELearning.pipeline.stage_02_ingest_pdf import DataIngestionPDFPipeline

DATA_INGESTION_STAGE_NAME = "Data Ingestion PPTX Stage"

def run_data_ingestion():
    """
    Runs the data ingestion stage of the PPTX pipeline.
    """
    try:
        logging.info(f"Starting {DATA_INGESTION_STAGE_NAME}.")
        data_ingestion_pipeline = DataIngestionPipeline()  # Create an instance of the PPTX pipeline
        data_ingestion_pipeline.main()  # Call the main method to run it
        logging.info(f"{DATA_INGESTION_STAGE_NAME} completed successfully.")
    except Exception as e:
        logging.error(f"Error occurred during {DATA_INGESTION_STAGE_NAME}: {e}")
        raise e
    

DATA_INGESTION_PDF_STAGE = "PDF Data Ingestion Stage"

def run_pdf_data_ingestion():
    """
    Runs the data ingestion stage of the PDF pipeline.
    """
    try:
        logging.info(f"Starting {DATA_INGESTION_PDF_STAGE}.")
        pdf_pipeline = DataIngestionPDFPipeline()  # Create an instance of the PDF pipeline
        pdf_pipeline.main()  # Call the main method to run it
        logging.info(f"{DATA_INGESTION_PDF_STAGE} completed successfully.")
    except Exception as e:
        logging.error(f"Error occurred during {DATA_INGESTION_PDF_STAGE}: {e}")
        raise e


def main():
    """
    Main function to run all stages of the pipeline.
    """
    try:
        run_data_ingestion()  # Run PPTX ingestion
        run_pdf_data_ingestion()  # Run PDF ingestion
    except Exception as e:
        logging.error(f"Pipeline failed with error: {e}")
        raise e

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()
