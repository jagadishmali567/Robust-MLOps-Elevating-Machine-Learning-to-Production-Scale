import os
import sys
from pandas import DataFrame
from sklearn.model_selection import train_test_split
from us_visa.entity.config_entity import DataIngestionConfig
from us_visa.entity.artifact_entity import DataIngestionArtifact
from us_visa.exception import USvisaException
from us_visa.logger import logging
from us_visa.data_access.usvisa_data import USvisaData

class DataIngestion:
    def __init__(self, data_ingestion_config: DataIngestionConfig = DataIngestionConfig()) -> None:
        """
        Initialize the DataIngestion class with configuration.
        :param data_ingestion_config: Configuration for data ingestion
        """
        try:
            self.data_ingestion_config = data_ingestion_config
        except Exception as e:
            raise USvisaException(e, sys)

    def export_data_into_feature_store(self) -> DataFrame:
        """
        Export data from MongoDB to CSV file.
        :return: DataFrame containing the data
        """
        try:
            logging.info("Exporting data from MongoDB")
            usvisa_data = USvisaData()
            dataframe = usvisa_data.export_collection_as_dataframe(collection_name=self.data_ingestion_config.collection_name)
            logging.info(f"Shape of DataFrame: {dataframe.shape}")

            feature_store_file_path = self.data_ingestion_config.feature_store_file_path
            os.makedirs(os.path.dirname(feature_store_file_path), exist_ok=True)
            logging.info(f"Saving exported data to feature store file path: {feature_store_file_path}")
            dataframe.to_csv(feature_store_file_path, index=False, header=True)
            return dataframe
        except Exception as e:
            raise USvisaException(e, sys)

    def split_data_as_train_test(self, dataframe: DataFrame) -> None:
        """
        Split the DataFrame into train and test sets based on the split ratio.
        :param dataframe: DataFrame to be split
        """
        logging.info("Entered split_data_as_train_test method of DataIngestion class")
        try:
            train_set, test_set = train_test_split(dataframe, test_size=self.data_ingestion_config.train_test_split_ratio)
            logging.info("Performed train-test split on the DataFrame")

            os.makedirs(os.path.dirname(self.data_ingestion_config.training_file_path), exist_ok=True)
            logging.info("Exporting train and test datasets to specified paths")
            train_set.to_csv(self.data_ingestion_config.training_file_path, index=False, header=True)
            test_set.to_csv(self.data_ingestion_config.testing_file_path, index=False, header=True)
            logging.info("Exported train and test datasets")
        except Exception as e:
            raise USvisaException(e, sys)

    def initiate_data_ingestion(self) -> DataIngestionArtifact:
        """
        Initiate the data ingestion process.
        :return: DataIngestionArtifact containing paths to the train and test datasets
        """
        logging.info("Entered initiate_data_ingestion method of DataIngestion class")
        try:
            dataframe = self.export_data_into_feature_store()
            logging.info("Data retrieved from MongoDB")

            self.split_data_as_train_test(dataframe)
            logging.info("Train-test split performed on the dataset")

            data_ingestion_artifact = DataIngestionArtifact(
                trained_file_path=self.data_ingestion_config.training_file_path,
                test_file_path=self.data_ingestion_config.testing_file_path
            )
            logging.info(f"Data ingestion artifact created: {data_ingestion_artifact}")
            return data_ingestion_artifact
        except Exception as e:
            raise USvisaException(e, sys)
