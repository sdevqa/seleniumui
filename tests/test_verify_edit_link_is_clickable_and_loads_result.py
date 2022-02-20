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

@pytest.mark.edit
def test_verify_edit_link_is_clickable_and_loads_result(browser):
  landing_page_object = LandingPage(browser)
  landing_page_object.load()
  landing_page_object.click_edit_link()

  time.sleep(2) # For Demo Purposes.

  # Assert specific value is present on screen.
  url = browser.current_url
  assert url == "https://the-internet.herokuapp.com/challenging_dom#edit"
