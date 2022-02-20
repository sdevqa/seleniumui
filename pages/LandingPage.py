import pytest
import time
import re
import chromedriver_autoinstaller
from selenium.common.exceptions import ElementNotVisibleException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class LandingPage():
  # Loc strategies
  LANDING_PAGE_HEADER_ELEMENT = (By.XPATH, '//*[@id="content"]/div/h3')
  UI_BUTTONS = (By.XPATH, "//*[contains(@id,'7726')]") 
  EDIT_LINK_TEXT = (By.XPATH, "//a[contains(text(),'edit')]") 
  DELETE_LINK_TEXT = (By.XPATH, "//a[contains(text(),'delete')]")

  def __init__(self, browser):
    self.browser = browser

  def load(self):
    self.browser.get(pytest.config_url)

  def click_number_generation_button(self):
    ui_buttons = self.browser.find_elements(*self.UI_BUTTONS)
    ui_buttons[0].click() 
    
  def click_edit_link(self):
    edit_links = self.browser.find_elements(*self.EDIT_LINK_TEXT) 
    edit_links[0].click() # Load the first result.

  def delete_table_result(self):
    delete_links = self.browser.find_elements(*self.DELETE_LINK_TEXT)
    delete_links[0].click()  # Load the first result.

  def get_page_source_answer_val(self):
    browser_source = self.browser.page_source # Get Source Code 
    answer_text = re.findall("Answers*:(.\\d{3,5}|\\d{})", browser_source) # Use Regex to grab canvas number value.
    converted_answer_text = [str(i) for i in answer_text] #  Convert a list to a string
    converted_answer_text_joined = ','.join(converted_answer_text) # Convert a list to a string
    converted_string_to_int = int(converted_answer_text_joined) # Cast to numeric value. 
    
    return converted_string_to_int
    