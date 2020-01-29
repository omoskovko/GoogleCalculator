from selenium import webdriver

def get_driver(dProfile='Firefox'):
    webDrivers = {}
    webDrivers["Chrome"] = webdriver.Chrome
    webDrivers["Firefox"] = webdriver.Firefox
        
    return webDrivers.get(dProfile, webdriver.Firefox)()
