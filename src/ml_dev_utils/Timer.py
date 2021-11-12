"""
Timer
======

This module measures the execution time and provides three ways to do this:

* **MeasureTime**: Measure time as decorator ``@MeasureTime``.
* **MeasureBlockTime**: Measure as ``with MeasureBlockTime("my_block") as my_block:``.
* **Timer**: Measure as instance ``timer = Timer()``
"""
from __future__ import annotations

import timeit
import datetime

from functools import wraps

from ml_dev_utils import log


def MeasureTime(function):
    """Measure the execution time as a decorator.

    Returns:
        : The return of the wrapped function

    Example::

        from ml_dev_utils.Timer import MeasureTime

        @MeasureTime
        def my_function():
            print("my awesome code")

    The measured duration time will be written to ``log.debug``. Therefore to 
    see the output, you need to set up a handler for logging.

    Example with specific ``ml_dev_utils`` logger::

        import logging
        from ml_dev_utils import log
        from ml_dev_utils.log_handler import console
        from ml_dev_utils.Timer import MeasureTime

        log.addHandler(console)
        log.setLevel(logging.DEBUG)

        @MeasureTime
        def my_function():
            print("my awesome code")

        my_function()
    """

    @wraps(function)
    def _wrapper(*args, **kwargs):
        timer = Timer(function.__name__).start()

        try:
            result = function(*args, **kwargs)
        finally:
            timer.end()
            _log_execution_time(timer)

        return result
    return _wrapper


class MeasureBlockTime():
    """Measure the execution time of a code block.

    Args:
        name: A name for the timer instance. Defaults to "(block)".
        log_time: If true, it will write the execution time to ``log.debug``. Defaults to True.

    **Attributes**

    Attributes:
        timer (ml_dev_utils.Timer.Timer): Keeps the measured time.

    Example::

        from ml_dev_utils.Timer import MeasureBlockTime

        with MeasureBlockTime("my_block") as my_block:
            print("my code here")

        print(my_block.timer.time)
    """

    def __init__(self, name: str = "(block)", log_time: bool = True):
        self.timer = Timer(name)
        self.log_time = log_time

    def __enter__(self):
        self.timer.start()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.timer.end()

        if self.log_time:
            _log_execution_time(self.timer)

        # re-raise any exceptions
        return False


class Timer():
    """Measures the execution time.

    Args:
        name: A name for the timer instance. Defaults to "unnamed".

    **Attributes**

    Attributes:
        name (str): The name of the Timer.
        time (datetime.timedelta): The measured duration time.
        start_time (float): The start time of the measurement.

    Example::

        from ml_dev_utils.Timer import Timer

        timer = Timer().start()
        print(timer.end())
    """

    def __init__(self, name: str = "unnamed"):
        self.name = name
        self.time = None
        self.start_time = None

    def start(self) -> Timer:
        """Starts the measurement.

        Set's the start time in the ``start_time`` instance variable.

        Returns:
            Returns itself for fluent initialization.
        """
        self.start_time = timeit.default_timer()
        return self

    def end(self) -> datetime.timedelta:
        """Stops the measurement.

        Measures the time duration and set's it to the ``time`` instance variable.

        Returns:
            The measured time duration
        """
        self.time = timeit.default_timer() - self.start_time
        self.time = _format_time(self.time)
        return self.time


def _log_execution_time(timer: Timer):
    log.debug(f'Run time for "{timer.name}" is {timer.time}')


def _format_time(time_to_format):
    return datetime.timedelta(seconds=time_to_format)
