import logging
# logging.basicConfig(level=logging.DEBUG, force=True)

import testing_logging

logger=logging.getLogger("testing_logging")
# logger=logging.getLogger("testing_logging")
# logger.propagate=True
# logging.basicConfig(level=logging.DEBUG, force=True)

testing_logging.main.main()