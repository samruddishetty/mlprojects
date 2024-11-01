#Considering a big data team thats responsible to obtaining constantly collect from different data sources
import os
import sys
sys.path.append('C:\\Users\\Samruddi\\Documents\\GitHub\\mlprojects')
from ..exception import CustomException
from src.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass 

#certain inputs are a requirement where the paths will be stored
@dataclass
class DataIngestionConfig:
    #The trained,test,raw data will be stored in this path
    train_data_path: str=os.path.join('artifacts',"train.csv")
    test_data_path: str=os.path.join('artifacts',"test.csv")
    raw_data_path: str=os.path.join('artifacts',"data.csv")

#Input is initialised to ingestion_config
class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()

#This class is created for reading the data from certain databases
    def initiate_data_ingestion(self):
        logging.info("Entered data ingestion method or component")
        try:
            df=pd.read_csv('notebook\data\Stud.csv')
#Write about logging.info to catch exceptions
            logging.info('Read the dataset as dataframe')
#Create the artifacts folder now
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)
           
            logging.info("Train test split initiated")
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            logging.info("Implementation of the data is completed")
            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path

            )

        except Exception as e:
            raise CustomException(e,sys)

if __name__=="__main__":
    obj=DataIngestion()
    obj.initiate_data_ingestion()
      


