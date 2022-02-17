import pytest
import time
import chromedriver_autoinstaller
from pages.LandingPage import LandingPage
from selenium import webdriver
from selenium.common.exceptions import ElementNotVisibleException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select, WebDriverWait

@pytest.mark.smoke
def test_verify_specific_table_value_is_present(browser):
  landing_page_object = LandingPage(browser)
  landing_page_object.load()
  
  iuvaret5_table_value = browser.find_element(By.XPATH, "//td[contains(.,'Iuvaret5')]") # Good way to find specific values inside of td.

  time.sleep(2) # For Demo Purposes.
  
  # Assert specific value is present on screen.
  assert iuvaret5_table_value.text == "Iuvaret5"

