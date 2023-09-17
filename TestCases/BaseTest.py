import pytest


# SPREADER:THIS SPREADER SPREAD FIXTURE TO ALL TESTCASE THAT INHERIT THIS CLASS
# NO NEED TO WRITW MANUAL DRIVER INITIALIZATION
# conftest.py-------->BaseTest.py-------inherit----->ANY TEST CASE


@pytest.mark.usefixtures("log_on_failure", "get_browser")
class DRIVER_INITIALIZATION_OVER_ALL_TESTCASE:
    pass
