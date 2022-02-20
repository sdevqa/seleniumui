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
def test_check_page_title_is_correct(browser):
  landing_page_object = LandingPage(browser)
  landing_page_object.load()

  time.sleep(2) # For Demo Purposes.

  # Assert page title is what we expect.
  page_title = browser.title
  assert page_title == 'The Internet'

