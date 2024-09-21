# main.py
from . import module1
from . import module2

import logging

logger = logging.getLogger(__name__)

def main():
    print("just printing here")
    try:
        logger_package = logging.getLogger(str(__package__))
        print(__package__)
        logger.info("Starting the main function")
        module1.some_function()
        module2.another_function()
    except Exception as e:
        logger_package.propagate, old_value = False, logger_package.propagate
        # console_handler = None
        # print(logger_package.handlers)
        # print(logger_package.propagate)
        # logger_package.exception("Yo")
        # if console_handler:
        #     logger_package.addHandler(console_handler)
        # logger_package.propagate = old_value
        # logger.error(e, stack_info=True)
        logger.exception(e)
        logger_package.propagate = old_value
        raise e

    # try:
    #     logger_package = logging.getLogger(str(__package__))
    #     print(__package__)
    #     logger_package.setLevel(logging.ERROR)
    #     logger.info("Starting the main function")
    #     for handler in logger_package.handlers:
    #         print(handler)
    #         if handler.get_name() == 'console':
    #             console_handler = handler
    #             logger.removeHandler(handler)
    #             print("removed")
    #             break
    #     logger_package.propagate = False
    #     module1.some_function()
    #     module2.another_function()
    # except Exception as e:
    #     # logger_package.propagate, old_value = False, logger_package.propagate
    #     # console_handler = None
    #     # print(logger_package.handlers)
    #     # print(logger_package.propagate)
    #     # logger_package.exception("Yo")
    #     # if console_handler:
    #     #     logger_package.addHandler(console_handler)
    #     # logger_package.propagate = old_value
    #     # logger.error(e, stack_info=True)
    #     logger.exception(e)
    #     raise e

if __name__ == "__main__":
    main()
