from selenium import webdriver


def get_driver(use_headless, dProfile="Chrome"):
    webDrivers = {}
    webDrivers["Chrome"] = webdriver.Chrome
    webDrivers["Firefox"] = webdriver.Firefox

    if dProfile == "Chrome":
        from selenium.webdriver.chrome.options import Options

        options = Options()
        if use_headless:
            options.add_argument("--headless")

        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
    elif dProfile == "Firefox":
        from selenium.webdriver.firefox.options import Options

        options = Options()
        if use_headless:
            options.add_argument("--headless")

    return webDrivers[dProfile](options=options)
