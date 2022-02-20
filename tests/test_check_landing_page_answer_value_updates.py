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
def test_check_landing_page_answer_value_updates(browser):
  landing_page_object = LandingPage(browser)
  landing_page_object.load()
  initial_canvas_value = landing_page_object.get_page_source_answer_val()
  assert initial_canvas_value > 0 # GT > Zero means canvas element has rendered.

  landing_page_object.click_number_generation_button() # Perform UI/Action Change
  updated_canvas_value = landing_page_object.get_page_source_answer_val()
  assert initial_canvas_value != updated_canvas_value # Check answer number changes on button click/reload.

  print("DEBUG Intial Val: "+str(initial_canvas_value))
  print("DEBUG Updated Val: "+str(updated_canvas_value))

