import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
# from webdriver_manager.microsoft import EdgeDriverManager


@pytest.fixture
def driver_init(request):
    browser = request.param


    if browser == "chrome":
        driver = webdriver.Chrome(ChromeDriverManager().install())
    elif browser == "firefox":
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    # elif browser == "edge":
        # driver = webdriver.Edge(EdgeDriverManager().install())
    else:
        raise ValueError("Browser not supported: {}".format(browser))

    yield driver
    driver.quit()
