from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def get_driver(dProfile='Chrome'):
    options = Options()
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    webDrivers = {}
    webDrivers["Chrome"] = webdriver.Chrome
    webDrivers["Firefox"] = webdriver.Firefox
        
    if dProfilr == "Chrome":
        driver = webDrivers[dProfilr].(chrome_options=options)
    else:
        driver = webDrivers[dProfilr]()
        
    return driver
