![Python application](https://github.com/omoskovko/GoogleCalculator/workflows/Python%20application/badge.svg)

# GoogleCalculator
Pytest project with test cases for Google Calculator


# Dependencies
[Chrome](https://www.google.com/chrome/) 
, [ChromeDriver](https://chromedriver.chromium.org/downloads)


# Installation Ubuntu
```
sudo apt-get update
sudo apt-get install -y wget gnupg2 ca-certificates
sudo sh -c "wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | gpg --dearmor > /usr/share/keyrings/google-chrome-archive-keyring.gpg"
sudo sh -c 'echo "deb [signed-by=/usr/share/keyrings/google-chrome-archive-keyring.gpg] http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list'
sudo apt-get -y update
sudo apt-get -y install google-chrome-stable
sudo apt-get -y install curl
wget https://chromedriver.storage.googleapis.com/$(curl https://chromedriver.storage.googleapis.com/LATEST_RELEASE)/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
sudo mv chromedriver /usr/bin/chromedriver
sudo chmod 755 /usr/bin/chromedriver
python -m pip install --upgrade pip
pip install flake8 pytest
pip install -r requirements.txt
pytest --junitxml=test.xml [--driver=WebDriver]
#                              where WebDriver is Chrome
```
