import pytest
import time
import chromedriver_autoinstaller
from selenium.common.exceptions import ElementNotVisibleException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class LandingPage():
  # Loc strategies
  LANDING_PAGE_HEADER_ELEMENT = (By.XPATH, '//*[@id="content"]/div/h3')
  UI_BUTTONS = (By.XPATH, "//*[contains(@id,'062f3f659484')]") 
  EDIT_LINK_TEXT = (By.XPATH, "//a[contains(text(),'edit')]") 
  DELETE_LINK_TEXT = (By.XPATH, "//a[contains(text(),'delete')]")

  def __init__(self, browser):
    self.browser = browser

  def load(self):
    self.browser.get(pytest.config_url)

  def click_number_generation_button(self):
    ui_buttons = self.browser.find_elements(*self.UI_BUTTONS)
    ui_buttons[2].click() # Click on 3rd button.

  def click_edit_link(self):
    edit_links = self.browser.find_elements(*self.EDIT_LINK_TEXT) 
    edit_links[0].click() # Load the first result.

  def delete_table_result(self):
    delete_links = self.browser.find_elements(*self.DELETE_LINK_TEXT)
    delete_links[0].click() # Delete the first result.
