import pytest
from src import WebDriverHandler

class TestWebDriverHandler(object):

    @pytest.fixture
    def instance(self):
        return WebDriverHandler()

    # Test constractor
    def test_constract(self, instance):
       assert isinstance(instance, WebDriverHandler) == True

    # Test constractor
    def test_launch_firefox(self, instance):
        instance.launch_firefox()
        browser_name = instance.webdriver.capabilities['browserName']
        assert isinstance(instance, WebDriverHandler) == True
        assert browser_name == "firefox"
        instance.webdriver.quit()
