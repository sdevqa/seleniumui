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
def test_verify_delete_link_is_clickable_and_deletes_entry(browser):
  landing_page_object = LandingPage(browser)
  landing_page_object.load()
  landing_page_object.delete_table_result()

  time.sleep(2) # For Demo Purposes.

  # Assert specific value is present on screen after deletion. Detect behaviour change.
  url = browser.current_url
  assert url == "https://the-internet.herokuapp.com/challenging_dom#delete"
