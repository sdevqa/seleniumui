import json
import pytest
from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.chrome.service import Service

# https://docs.pytest.org/en/6.2.x/fixture.html#conftest-py-sharing-fixtures-across-multiple-files
# Standard pytest file.

SUPPORTED_BROWSERS = ['chrome-headless','chrome-ui', 'randombrowser']

# If no argument is passed, will default to using local chrome via UI.
def pytest_addoption(parser):
    parser.addoption("--config_browser", action="store", default="chrome-ui")
    parser.addoption("--config_url", action="store", default="https://the-internet.herokuapp.com/challenging_dom")

#  If an argument is passed dynamically it will use the browser provided it matches.
@pytest.fixture(scope='session')
def config_browser(request):
    return request.config.getoption("--config_browser")

def pytest_configure(config):
    pytest.config_url = config.getoption('config_url')

@pytest.fixture(scope='function')
def browser(config_browser):
  if config_browser == 'chrome-headless':
    chrome_opt = webdriver.ChromeOptions()
    chrome_opt.add_argument('--headless')
    chrome_service = Service(chromedriver_autoinstaller.install())
    driver = webdriver.Chrome(service=chrome_service, options=chrome_opt)
  elif config_browser == 'chrome-ui':
    chrome_opt = webdriver.ChromeOptions()
    chrome_service = Service(chromedriver_autoinstaller.install())
    driver = webdriver.Chrome(service=chrome_service, options=chrome_opt)
  else:
    raise Exception(f'"{config_browser}" is not a supported browser')

  driver.implicitly_wait(10) 

  yield driver
  
  driver.quit()