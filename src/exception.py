# exception.py
import sys
from logger import logging  # Import the logging setup

# Error message detail function
def error_message_detail(error, error_detail: sys):
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "ERROR OCCURED IN THE PYTHON SCRIPT NAME [{0}] LINE NUMBER [{1}] ERROR MESSAGE [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error))
    return error_message

# Custom exception class
class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail)

    def __str__(self):
        return self.error_message

if __name__ == "__main__":
    try:
        a = 1 / 0
    except Exception as e:
        exception = CustomException(e, sys)
        logging.error(exception, exc_info=True)  # Log the exception with traceback
        raise exception
