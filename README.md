![Python application](https://github.com/omoskovko/GoogleCalculator/workflows/Python%20application/badge.svg)

# GoogleCalculator
Pytest project with test cases for Google Calculator


# Dependencies
[Chrome](https://www.google.com/chrome/) 
, [Python](https://www.python.org/)


# Run with Docker
```
docker build --build-arg USER_ID=$(id -u) -t google-calc .
mkdir -p output.png
chmod 777 ./output.png
docker run -u $(id -u) -v ./output.png:/home/uchrome/google_calc/output.png google-calc pytest -v --driver=Chrome --headless --session
```

# Installation Ubuntu
```
sudo apt-get update
sudo apt-get install -y wget unzip gnupg2 ca-certificates libssl-dev
sudo sh -c "wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | gpg --dearmor > /usr/share/keyrings/google-chrome-archive-keyring.gpg"
sudo sh -c 'echo "deb [signed-by=/usr/share/keyrings/google-chrome-archive-keyring.gpg] http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list'
sudo apt-get update
sudo apt-get install -y google-chrome-stable python3 python3-pip

python3 -m pip install --upgrade pip
pip3 install -r requirements.txt
# add ~/.local/bin to the PATH env
pytest [--junitxml=test.xml] [--driver=Chrome]
```
