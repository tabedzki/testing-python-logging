import logging
logging.basicConfig(level=logging.DEBUG)

import testing_logging

logger=logging.getLogger("testing_logging")
# logger=logging.getLogger("testing_logging")
# logger.propagate=True

testing_logging.main.main()
