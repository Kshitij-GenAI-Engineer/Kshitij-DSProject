from src.datascience.config.configuration import ConfigurationManager
from src.datascience.components.data_transformation import DataTransformation
from src.datascience.components.model_training import ModelTrainer
from src.datascience import logger

STAGE_NAME = "Model Trainer Pipeline"

class ModelTrainerPipeline:
    def __init__(self):
        pass
    
    def initiate_model_trainer(self):
        try:
            logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<")
            
            config = ConfigurationManager()
            model_trainer_config = config.get_model_trainer_config()
            
            model_trainer = ModelTrainer(model_trainer_config=model_trainer_config)
            model_trainer.train()
            
            logger.info(f">>>>>> Stage {STAGE_NAME} completed <<<<<<\n\n")