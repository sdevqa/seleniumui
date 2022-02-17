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
def test_click_number_generation_button_and_verify_button_count(browser):
  landing_page_object = LandingPage(browser)
  landing_page_object.load()
  landing_page_object.click_number_generation_button()

  ui_btn_webelements = browser.find_elements(By.XPATH, "//*[contains(@id,'062f3f659484')]")
  ui_btn_webelements_count = len(ui_btn_webelements)

  time.sleep(2) # For Demo Purposes.

  # Assert amount of buttons on the UI is 3
  assert ui_btn_webelements_count == 3

