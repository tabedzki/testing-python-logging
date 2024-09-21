# module2.py
import logging

logger = logging.getLogger(__name__)

def another_function():
    logger.debug("This is a debug message from module2")
    logger.info("This is a info message from module2")
    logger.warning("This is a warning message from module2")
    logger.error("This is an error message from module2")
    0/0
    # Your code here
