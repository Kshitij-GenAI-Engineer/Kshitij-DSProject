from src.datascience import logger
from src.datascience.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline


STAGE_NAME = "Data Ingestion stage"

try:
    logger.info(">>>>> Pipeline execution started <<<<<")
    data_ingestion_pipeline = DataIngestionTrainingPipeline()
    data_ingestion_pipeline.initiate_data_ingestion()
    logger.info(">>>>> Pipeline execution completed <<<<<")
except Exception as e:
    logger.exception(f"Pipeline execution failed: {e}")
    raise e