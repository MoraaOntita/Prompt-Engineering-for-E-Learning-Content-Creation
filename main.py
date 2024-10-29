import logging
from src.ELearning.pipeline.stage_01_data_ingestion_pptx import DataIngestionPipeline
from src.ELearning.pipeline.stage_02_ingest_pdf import DataIngestionPDFPipeline
from src.ELearning.pipeline.stage_03_metadata_extraction import MetadataExtractionPipeline
from src.ELearning.pipeline.stage_04_data_chunking import DataChunkingPipeline  # New chunking stage

# Define stage names
DATA_INGESTION_STAGE_NAME = "Data Ingestion PPTX Stage"
DATA_INGESTION_PDF_STAGE = "PDF Data Ingestion Stage"
METADATA_EXTRACTION_STAGE_NAME = "Metadata Extraction Stage"
CHUNKING_STAGE_NAME = "Data Chunking Stage"  # New chunking stage name

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

def run_metadata_extraction():
    """
    Runs the metadata extraction stage of the pipeline.
    """
    try:
        logging.info(f"Starting {METADATA_EXTRACTION_STAGE_NAME}.")
        metadata_extraction_pipeline = MetadataExtractionPipeline()  # Create an instance of the metadata extraction pipeline
        metadata_extraction_pipeline.main()  # Call the main method to run it
        logging.info(f"{METADATA_EXTRACTION_STAGE_NAME} completed successfully.")
    except Exception as e:
        logging.error(f"Error occurred during {METADATA_EXTRACTION_STAGE_NAME}: {e}")
        raise e

def run_data_chunking():
    """
    Runs the data chunking stage of the pipeline.
    """
    try:
        logging.info(f"Starting {CHUNKING_STAGE_NAME}.")
        chunking_pipeline = DataChunkingPipeline()  # Create an instance of the data chunking pipeline
        chunking_pipeline.main()  # Call the main method to run it
        logging.info(f"{CHUNKING_STAGE_NAME} completed successfully.")
    except Exception as e:
        logging.error(f"Error occurred during {CHUNKING_STAGE_NAME}: {e}")
        raise e

def main():
    """
    Main function to run all stages of the pipeline.
    """
    try:
        run_data_ingestion()  # Run PPTX ingestion
        run_pdf_data_ingestion()  # Run PDF ingestion
        run_metadata_extraction()  # Run metadata extraction
        run_data_chunking()  # Run data chunking
    except Exception as e:
        logging.error(f"Pipeline failed with error: {e}")
        raise e

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()
