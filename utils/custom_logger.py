import logging
import os

class LogGen:
    @staticmethod
    def loggen():
        # Ensure the logs directory exists
        log_path = ".\\logs\\automation.log"
        
        # Configure the logger
        logging.basicConfig(
            filename=log_path,
            format='%(asctime)s: %(levelname)s: %(message)s', 
            datefmt='%m/%d/%Y %I:%M:%S %p',
            force=True # This ensures the logger resets for every run
        )
        
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger