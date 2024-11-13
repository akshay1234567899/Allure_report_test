import pytest

class TestReRunFailed:

    def test_login(self):
        print("Verify login functionality of the application")
        assert True
    @pytest.mark.smoke
    def test_homepage(self):
        print("Verify homepage functionality of the application")
        assert False

    @pytest.mark.flaky(reruns=3, reruns_delay=2)
    def test_rerun(self):
        print("rerun failed test cases")
        assert False
