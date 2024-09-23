import logging
# Defines the root logger. The root logger from `__init__.py` defers to this outer defined value if uncommented
# logging.basicConfig(level=logging.INFO)

import testing_python_logging

logger=logging.getLogger("testing_python_logging")

testing_python_logging.main.main()
