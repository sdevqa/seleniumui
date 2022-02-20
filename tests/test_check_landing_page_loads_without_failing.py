import pytest
import time
import chromedriver_autoinstaller
import re
from pages.LandingPage import LandingPage
from selenium import webdriver
from selenium.common.exceptions import ElementNotVisibleException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select, WebDriverWait

@pytest.mark.smoke
def test_check_landing_page_loads_without_failing(browser):
  landing_page_object = LandingPage(browser)
  landing_page_object.load()

  # If we can find the challenging DOM H3 text, we can assume the test is passing.
  page_header_text = WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.XPATH, "//*[@id='content']/div/h3")))
  assert page_header_text.text == 'Challenging DOM'
