# .. module:: API Documentation
"""[summary]
.. module:: API Documentation
.. ::noindex
"""

# Version of the ml-dev-utils package
__version__ = "0.0.1"


# define the 'public' accessible files
__all__ = ['Timer', 'log_handler']


# package logger
import logging

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
