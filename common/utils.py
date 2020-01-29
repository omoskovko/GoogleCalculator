from selenium import webdriver

def get_driver(dProfile='Firefox'):
    if dProfile == 'Firefox':
        driver = webdriver.Firefox()
    else: 
        driver = webdriver.Chrome()
        
    return driver
