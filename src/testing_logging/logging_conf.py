# logging_config.py
import logging
import logging.config

def run_once(func):
    def wrapper(*args, **kwargs):
        if not wrapper.has_run:
            wrapper.has_run = True
            return func(*args, **kwargs)
    wrapper.has_run = False
    return wrapper

@run_once
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
        },
        'loggers': {
            'kilosort': {  # module-level logger
                'handlers': ['file'],
                'level': 'DEBUG',
                'propagate': False,
            },
        }
    }
    logging.config.dictConfig(logging_config)
