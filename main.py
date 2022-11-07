from sensor.configuration.mongodb_connection import MongoDBClient
from sensor.exception import SensorException
import os,sys
from sensor.logger import logging
import os
from sensor.entity.config_entity import TrainingPipelineConfig, DataIngestionConfig
from sensor.pipeline.training_pipeline import TrainPipeline
from sensor.configuration.mongodb_connection import MongoDBClient

if __name__ == '__main__':
    database = MongoDBClient()
    print (database.database_name)