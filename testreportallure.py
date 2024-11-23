import time
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
import allure
from selenium.webdriver.common.by import By


class TestWebsite:
    @pytest.fixture(scope="class")
    def setup(self):
        # Initialize WebDriver for all tests in this class
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        yield self.driver  # Provide the driver to the tests
        self.driver.quit()  # Close the browser after the tests are done

    @allure.feature("Login Tests")
    @allure.story("Login with valid credentials")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_login(self, setup):
        self.driver = setup
        with allure.step("Open the login page"):
            self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        with allure.step("Enter username and password"):
            time.sleep(9)
            self.driver.find_element(By.XPATH,"//input[@placeholder='Username']").send_keys("Admin")
            self.driver.find_element(By.XPATH,"//input[@placeholder='Password']").send_keys("admin123")
        with allure.step("Click login button"):
            self.driver.find_element(By.XPATH, "//button[@type='submit']").click()

    @allure.feature("Homepage Tests")
    @allure.story("Verify homepage title")
    @allure.severity(allure.severity_level.NORMAL)
    def test_homepagetitle(self, setup):
        time.sleep(8)
        self.driver = setup
        allure.attach(self.driver.get_screenshot_as_png(),name="takescreenshot",attachment_type=AttachmentType.PNG)
        with allure.step("Get page title"):
            title = self.driver.title
        expected_title = "OrangeHRM"
        with allure.step(f"Verify if title matches expected value '{expected_title}'"):
            assert title == expected_title, f"Expected title: {expected_title}, but got: {title}"

    @allure.feature("Logout Tests")
    @allure.story("Logout from the application")
    @allure.severity(allure.severity_level.MINOR)
    def test_logout(self, setup):
        self.driver = setup
        with allure.step("Click on user profile dropdown"):
            time.sleep(8)
            self.driver.find_element(By.XPATH, "//p[@class='oxd-userdropdown-name']").click()
        with allure.step("Click on logout link"):
            self.driver.find_element(By.XPATH, '//a[contains(text(),"Logout")]').click()


# allure report : pytest -v -s --alluredir="C:\Users\Mysense\PycharmProjects\Python_Basic\Reports" allurereportpytest\testreportallure.py
# allure serve C:\Users\Mysense\PycharmProjects\Python_Basic\Reports
# allure serve .\Reports
# npm install -g allure-commandline

# allure serve /Users/akshaydhiman/Desktop/Pytest-XYZBank/Allure_Report

