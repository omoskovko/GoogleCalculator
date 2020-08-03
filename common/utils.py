from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def get_driver(dProfile='Chrome'):
    options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')

    webDrivers = {}
    webDrivers["Chrome"] = webdriver.Chrome
    webDrivers["Firefox"] = webdriver.Firefox
        
    if dProfile == "Chrome":
        driver = webDrivers[dProfile](chrome_options=options)
    else:
        driver = webDrivers[dProfile]()
        
    return driver
