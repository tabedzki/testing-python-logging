# logging_config.py
import logging
import logging.config

from . import main

def setup_logging():
    logging_config = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'standard': {
                'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            },
        },
        'handlers': {
            'file': {
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
                # 'handlers': ['file', 'console'],
                'handlers': ['file'],
                'level': "DEBUG",
                'propagate': True,
                # 'propagate': False,
            },
            'root': {
                'handlers': ['console'],
                # 'level': 'ERROR',  # Root logger level
                'level': 'WARNING',  # Root logger level
            },
        }
    }
    logging.config.dictConfig(logging_config)

setup_logging()