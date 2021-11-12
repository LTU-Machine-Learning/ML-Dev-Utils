ML-Dev Utils Documentation
==========================

This package contains general functions created out of the ML-Dev project.


************************************
Installation
************************************

You can install the newest release with pip:

.. code-block:: bash

    pip install ml_dev_utils


************************************
Quick Start
************************************

ML-Dev Utils provides various functionalities. You can find examples of how to 
use them in :doc:`API Documentation <api>`.


************************************
Logging
************************************

We are using a package logger with the name ``ml_dev_utils`` and log level 
``INFO``. The logger is initialized by the package ``__init__.py`` when you 
import the package in your application. The package does not set up any log 
handlers. Without any application log handlers, there will be no package log
output. Only the events of severity `WARNING` and greater will be printed to 
`sys.stderr` by default of the `Python Logging <https://docs.python.org/3/howto/logging.html#configuring-logging-for-a-library>`__.

You can define logging handlers at root level to propagated package log output,
for example:

.. code-block:: python

    import logging
    import sys

    # -- option with basic config
    logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s',
                        level=logging.DEBUG,
                        stream=sys.stdout)


    # -- option with root logger ('' = root logger)
    stream_handler = logging.StreamHandler()
    # ...
    logging.getLogger('').addHandler(stream_handler)


    # -- option with logging.ini
    # if 'disable_existing_loggers' is not set to False it will disable all 
    # existing loggers
    logging.config.fileConfig('your_logging.ini',
                              disable_existing_loggers=False)


If you want to configure the log level and/or handlers for the package logger 
directly you can do so by:

.. code-block:: python

    import logging
    from ml_dev_utils import log
   
    log.setLevel(logging.ERROR)

    stream_handler = logging.StreamHandler()
    # ...
    log.addHandler(stream_handler)


For more information on logging please have a look  at the `Python Logging <https://docs.python.org/3/howto/logging.html#>`_.


************************************
Indices and tables
************************************

* :ref:`genindex`
* :ref:`modindex`


************************************
Contents
************************************

.. toctree::
   api
   changelog
