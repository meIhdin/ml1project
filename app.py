import sys
import os

# Add the 'src' directory to Python's sys.path
project_root = os.path.abspath(os.getcwd())
sys.path.append(os.path.join(project_root, "src"))

# Now try importing the logger
from src.ml1project.logger import logging
from src.ml1project.exception import CustomException
from src.ml1project.components.data_ingestion import DataIngestion
from src.ml1project.components.data_ingestion import DataIngestionConfig
from src.ml1project.components.data_transformation import DataTransformationConfig, DataTransformation


if __name__ == "__main__":
    logging.info("The execution has started.")

    try:
        data_ingestion = DataIngestion()
        train_data_path, test_data_path = data_ingestion.initiate_data_ingestion()

        data_transformation = DataTransformation()
        data_transformation.initiate_data_transformation(train_data_path, test_data_path)
        
    except Exception as e:
        logging.info("Custom Exception")
        raise CustomException(e,sys)