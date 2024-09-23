# main.py
from . import module1
from . import module2
from . import example_plot

import logging

logger = logging.getLogger(__name__)

def main():
    print("just printing here")
    example_plot.plot()
    try:
        logger.info("Starting the main function")
        module1.some_function()
        module2.another_function()
    except Exception as e:
        # Disable propagation to prevent double print to the console or unhandled `e`
        logger_package = logging.getLogger(str(__package__))
        logger_package.propagate, old_value = False, logger_package.propagate
        logger.exception('Here')
        logger_package.propagate = old_value
        raise e

if __name__ == "__main__":
    main()
