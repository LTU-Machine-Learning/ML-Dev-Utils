import time

from datetime import timedelta
from pytest import approx

from ml_dev_utils.Timer import Timer
from ml_dev_utils.Timer import MeasureTime
from ml_dev_utils.Timer import MeasureBlockTime


def test_timer_measuering():
    # given
    execution_time_sec = 2

    # when
    timer = Timer().start()
    time.sleep(execution_time_sec)
    timer.end()

    # then
    expected_time = timedelta(seconds=execution_time_sec).total_seconds()
    expected_time = approx(expected_time,
                           abs=timedelta(milliseconds=300).total_seconds())

    assert expected_time == timer.time.total_seconds()


def test_measure_block_execution_time():
    # given
    execution_time_sec = 2

    # when
    with MeasureBlockTime("test_measure_block_execution_time") as test_block:
        time.sleep(execution_time_sec)

    # then
    expected_time = timedelta(seconds=execution_time_sec).total_seconds()
    expected_time = approx(expected_time,
                           abs=timedelta(milliseconds=300).total_seconds())
    assert expected_time == test_block.timer.time.total_seconds()
