from sensor.configuration.mongodb_connection import MongoDBClient
from sensor.exception import SensorException
import os,sys
from sensor.logger import logging
import os
from sensor.entity.config_entity import TrainingPipelineConfig, DataIngestionConfig
from sensor.pipeline.training_pipeline import TrainPipeline
from sensor.configuration.mongodb_connection import MongoDBClient
from sensor.data_access.sensor_data import SensorData
from sensor.constant.training_pipeline.database import DATABASE_NAME



if __name__ == '__main__':
    from sensor.configuration.mongodb_connection import MongoDBClient
from sensor.exception import SensorException
import os,sys
from sensor.logger import logging
import os
from sensor.entity.config_entity import TrainingPipelineConfig, DataIngestionConfig
from sensor.pipeline.training_pipeline import TrainPipeline
from sensor.configuration.mongodb_connection import MongoDBClient
from sensor.data_access.sensor_data import SensorData
from sensor.constant.training_pipeline.database import DATABASE_NAME



if __name__ == '__main__':
    training_pipeline = TrainPipeline()
    training_pipeline.run_pipeline()

