import pandas as pd
import os
from src.datascience import logger
from sklearn.linear_model import ElasticNet
import joblib
from src.datascience.entity.config_entity import ModelTrainerConfig

class ModelTrainer:
    def __init__(self, ModelTrainerConfig: ModelTrainerConfig):
        self.model_trainer_config = ModelTrainerConfig

    def train(self):
        train_data = pd.read_csv(self.model_trainer_config.train_data_path)
        test_data = pd.read_csv(self.model_trainer_config.test_data_path)

        train_x = train_data.drop([self.model_trainer_config.target_column], axis=1)
        test_x = test_data.drop([self.model_trainer_config.target_column], axis=1)
        train_y = train_data[[self.model_trainer_config.target_column]]
        test_y = test_data[[self.model_trainer_config.target_column]]

        lr = ElasticNet(alpha=self.model_trainer_config.alpha, l1_ratio=self.model_trainer_config.l1_ratio, random_state=42)
        lr.fit(train_x, train_y)

        joblib.dump(lr, os.path.join(self.model_trainer_config.root_dir, self.model_trainer_config.model_name))