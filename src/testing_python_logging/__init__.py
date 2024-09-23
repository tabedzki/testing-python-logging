# logging_config.py
import logging
import logging.config

from . import main

def setup_logging():
    logging_config = {
        'version': 1,
        'disable_existing_loggers': False, # Doing this allows you to not override the root logger set by an external user
        'formatters': {
            'standard': {
                'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            },
        },
        'handlers': {
            'app_log_file': {
                'level': 'DEBUG',
                'class': 'logging.FileHandler',
                'filename': 'app.log',
                'mode': 'w',
                'formatter': 'standard',
            },
            'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'standard',
            'level': 'INFO',
            },
        },
        'loggers': {
            str(__package__): {  # module-level logger
                # 'handlers': ['app_log_file', 'console'],
                'handlers': ['app_log_file'],
                'level': "DEBUG",
                'propagate': True,
            },
            'root': { # Defines the root logger if the external user did not define it
                'handlers': ['console'],
                'level': 'INFO',  # Root logger level
            },
            # Other loggers, such as for matplotlib, can be define here.
            'matplotlib': {  # module-level logger
                'handlers': ['app_log_file'],
                'level': "INFO",
                'propagate': True,
            },
        }
    }
    logging.config.dictConfig(logging_config)

setup_logging()