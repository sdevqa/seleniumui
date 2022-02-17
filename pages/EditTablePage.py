import pytest
import time
import chromedriver_autoinstaller
from selenium.common.exceptions import ElementNotVisibleException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class EditTablePage():
  EDIT_PAGE_INPUT_ELEMENT = (By.XPATH, '')

  def __init__(self, browser):
    self.browser = browser

  def load(self):
    self.browser.get(pytest.config_url)

