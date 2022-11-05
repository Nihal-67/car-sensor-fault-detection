from sensor.configuration.mongodb_connection import MongoDBClient
from sensor.exception import SensorException
import os,sys
from sensor.logger import logging
import os
from sensor.entity.config_entity import TrainingPipelineConfig, DataIngestionConfig

if __name__ == '__main__':
    training_pipeline_config = TrainingPipelineConfig()
    data_ingetion_config = DataIngestionConfig(training_pipeline_config=training_pipeline_config)
    print(data_ingetion_config.__dict__)