![Python application](https://github.com/omoskovko/GoogleCalculator/workflows/Python%20application/badge.svg)

# GoogleCalculator
Pytest project with test cases for Google Calculator


# Dependencies
Chrome - https://www.google.com/chrome/ 
, ChromeDriver - https://chromedriver.chromium.org/downloads

Firefox - https://www.mozilla.org/en-US/firefox/new/
, geckodriver - https://github.com/mozilla/geckodriver/releases


# Installation Ubuntu
```
wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | sudo apt-key add -
sudo sh -c 'echo "deb [arch=amd64] https://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list'
sudo apt-get -y update
sudo apt-get -y install firefox
sudo apt-get -y install google-chrome-stable
sudo apt-get -y install curl
wget $(curl -s 'https://api.github.com/repos/mozilla/geckodriver/releases/latest' | sed -n '/content_type/!b;:a;/browser_download_url/!{$!{N;ba}};{/application\/x\-gzip/p}'|sed -e 's/^[^:]*: *\"\(http[^\"]*\).*/\1/'|grep linux64)
tar -xvzf geckodriver*
chmod 755 geckodriver
sudo mv geckodriver /usr/bin/geckodriver
wget https://chromedriver.storage.googleapis.com/$(curl https://chromedriver.storage.googleapis.com/LATEST_RELEASE)/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
sudo mv chromedriver /usr/bin/chromedriver
sudo chmod 755 /usr/bin/chromedriver

pip install -r requirements.txt
pytest --junitxml=test.xml [--driver=WebDriver]
#                              where WebDriver is Chrome or Firefox
```
