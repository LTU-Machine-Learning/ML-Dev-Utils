"""
log_handler
===========

``log_handler`` provides logging handlers for convenience to easily get a 
console or log file output. Additionally, a timezone format for log timestamps 
is provided.

**Attributes**

Attributes:
    console (StreamHandler): A console handler for logging using the TimezoneLogFormatter.

Examples::

    from ml_dev_utils import log
    from ml_dev_utils import log_handler

    log.addHandler(log_handler.console)

    log.info("Pizza Time!")
"""

import sys
import logging
import datetime
import pytz

from pathlib import Path
from tzlocal import get_localzone
from logging.handlers import RotatingFileHandler


class TimezoneLogFormatter(logging.Formatter):
    """%(asctime)s with timezone.

    This formatter overrides logging.Formatter to add the timezone to the 
    %(asctime)s in the log output. The format is ISO8601, e.g. 
    2009-06-30T18:30:00+02:00

    Args:
        timezone (str, optional): Set's the timezone. Defaults to "UTC".

    Example::

        import datetime
        from ml_dev_utils.log_handler import TimezoneLogFormatter

        timezone_formatter = TimezoneLogFormatter(timezone="UTC")

        now_timestamp = datetime.datetime.now().timestamp()
        print(timezone_formatter.converter(now_timestamp))
        # 2021-11-12 06:51:24.984044+00:00
    """

    def __init__(self, timezone: str = "UTC", *args, **kwargs):
        self.timezone = timezone
        super(TimezoneLogFormatter, self).__init__(*args, **kwargs)

    def converter(self, timestamp: float) -> datetime.datetime:
        """Convert a timestamp into the timezone format.

        Args:
            timestamp (float): The timestamp to convert.

        Returns:
            The timestamp with timezone.
        """
        return datetime.datetime.fromtimestamp(timestamp,
                                               tz=pytz.timezone(self.timezone))

    def formatTime(self, record, datefmt=None):
        created_time = self.converter(record.created)
        if datefmt:
            ct_formatted = created_time.strftime(datefmt)
        else:
            try:
                ct_formatted = created_time.isoformat(timespec='milliseconds')
            except TypeError:
                ct_formatted = created_time.isoformat()
        return ct_formatted


def _create_console_handler(log_level=logging.DEBUG):
    handler = logging.StreamHandler(sys.stdout)

    log_format = TimezoneLogFormatter(
        fmt='{asctime} {name:18s} {module}.{funcName:18s} {levelname:8s} {message}',
        style='{',
        timezone=str(get_localzone()))
    handler.setFormatter(log_format)
    handler.setLevel(log_level)

    return handler


console = _create_console_handler()


def rotating_file(log_file: str, log_level: int = logging.DEBUG) -> logging.handlers.RotatingFileHandler:
    """A RotatingFileHandler for logging.

    This handler uses the TimezoneLogFormatter.

    Args:
        log_file (str): The log filename.
        log_level (int, optional): The log level for the handler. Defaults to logging.DEBUG.

    Returns:
        A RotatingFileHandler log handler.

    Examples::

        from ml_dev_utils import log
        from ml_dev_utils import log_handler

        log.addHandler(log_handler.rotating_file('tmp/app.log'))

        log.info("Pizza Time!")
    """
    Path(log_file).parent.mkdir(parents=True, exist_ok=True)

    handler = RotatingFileHandler(log_file,
                                  mode='a',
                                  maxBytes=100000,
                                  backupCount=10)
    log_format = TimezoneLogFormatter(
        fmt='{asctime} {name:18s} {module}.{funcName:18s} {levelname:8s} {message}',
        style='{',
        timezone=str(get_localzone())
    )
    handler.setFormatter(log_format)
    handler.setLevel(log_level)

    return handler
