from src.datascience.config.configuration import ConfigurationManager
from src.datascience.components.data_ingestion import DataIngestion
from src.datascience import logger

STAGE_NAME = "Data Ingestion stage"

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass
    
    def initiate_data_ingestion(self):
        logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<")
        try:
            config = ConfigurationManager()
            data_ingestion_config = config.get_data_ingestion_config()
            
            data_ingestion = DataIngestion(config=data_ingestion_config)
            data_ingestion.download_data()
            data_ingestion.extract_zip_file()
            
            logger.info(f">>>>>> Stage {STAGE_NAME} completed <<<<<<\n\n")
        except Exception as e:
            logger.exception(f"Error in {STAGE_NAME}: {e}")
            raise e
        
        
if __name__ == "__main__":
    try:
        logger.info(">>>>> Pipeline execution started <<<<<")
        data_ingestion_pipeline = DataIngestionTrainingPipeline()
        data_ingestion_pipeline.initiate_data_ingestion()
        logger.info(">>>>> Pipeline execution completed <<<<<")
    except Exception as e:
        logger.exception(f"Pipeline execution failed: {e}")
        raise e