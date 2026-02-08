import logging
import os
from datetime import datetime

class EventLogger:
    """Handles logging of file system events 
    Writes evnets to logs/events.log with timestamps
    """
    def __init__(self,log_file='logs/events.log'):
        """Initialize the event logger
        
        Args:
             log_file: Path to the log file (default: logs/events.log)
        """
        log_dir = os.path.dirname(log_file)
        if log_dir and not os.path.exists(log_dir):
            os.mkdirs(log_dir)
        
        self.log_file = log_file #Stores the log file path
        
        #Configure logging
        
        logging.basicConfig(
            filename= log_file,
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            datefmt='%y-%m-%d %H:%M:%S'
        )
       
        self.logger = logging.getLogger(__name__)  
    
    def log_info(self, message):
        """Log an informanal message
        
        Agrs:
             message: The message to log
        """
        self.logger.info(message)
    
    def log_warning(self, message):
        """Log a warning message
        
           Args:
               message: The warning message to log
        """
        self.logger.warning(message)
    
    def log_error(self, message):
        """ Log a error message
        
            Args:
               message: The error message to log
        """
        self.logger.error(message)


if __name__ =="__main__":
    logger = EventLogger() #create a logger object
    
    logger.log_info("Logger initialezed Successfully")
    logger.log_info("This is a test info message")
    logger.log_warning("This is a test warning message")
    logger.log_error("This is a test error message")
    
    print("✅ Logs written to logs/events.log")
    print("Check the file to see the output!")
    
 