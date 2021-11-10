from check.check_pytest import CheckPytest


"""
    This script can check the pytest setup. Please delete it in your project if
    setup is correct.
"""


def test_random_number_is_in_range():
    # given
    check_pytest = CheckPytest()

    # when
    random_number = check_pytest.random_number()

    # then
    assert random_number > 0 and random_number <= 100
