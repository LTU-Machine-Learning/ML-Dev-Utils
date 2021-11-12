import re
import sys
import logging

from ml_dev_utils.log_handler import TimezoneLogFormatter


def test_timezone_formatting_is_correct(capsys):
    # given
    stream_handler = logging.StreamHandler(sys.stdout)
    log_format = TimezoneLogFormatter(fmt='%(asctime)s', timezone="UTC")
    stream_handler.setFormatter(log_format)

    logger = logging.getLogger(__name__)
    logger.addHandler(stream_handler)

    # when
    logger.warning("Foo logger")
    stdout, _ = capsys.readouterr()

    # then
    expected_format = "^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}\.[0-9]{3}\+00:00\n"
    assert re.fullmatch(expected_format, stdout)
