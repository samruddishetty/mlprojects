#logger ---for any execution that happens we need to log that into some files;especially with errors
import logging
import os
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log" #It will be a text file
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)
#any logs that will get created,it will be in the current directory
os.makedirs(logs_path,exist_ok=True)

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,

)   

if __name__=="__main__":
    logging.info("Logging has started")