# Use an official Python runtime as a parent image
FROM ubuntu:latest

RUN apt-get update && apt-get install -y locales && rm -rf /var/lib/apt/lists/* \
    && localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias en_US.UTF-8
ENV LANG en_US.utf8
RUN apt-get update \
    && apt-get install -y wget unzip gnupg2 ca-certificates libssl-dev python3 python3-pip
RUN sh -c "wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | gpg --dearmor > /usr/share/keyrings/google-chrome-archive-keyring.gpg"
RUN sh -c 'echo "deb [signed-by=/usr/share/keyrings/google-chrome-archive-keyring.gpg] http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list'
RUN apt-get update \
    && apt-get -y install google-chrome-stable python3 python3-pip python3-venv
# RUN wget --no-verbose -O /tmp/chrome.deb http://dl.google.com/linux/chrome/deb/pool/main/g/google-chrome-stable/google-chrome-stable_113.0.5672.92-1_amd64.deb \
#     && apt install -y /tmp/chrome.deb \
#     && rm /tmp/chrome.deb

RUN find / -name chromedriver -exec rm -f {} \;
RUN find / -name chromedriver

ARG USER_ID=999
RUN useradd -rm -d /home/uchrome -s /bin/bash -g root -G sudo -u ${USER_ID} uchrome
RUN chown -R uchrome /home/uchrome 
USER uchrome

WORKDIR /home/uchrome

# Copy the requirements file into the container
COPY requirements.txt .
RUN python3 -m venv venv
RUN . venv/bin/activate
RUN pip3 install -r requirements.txt
# ENV PATH="/home/uchrome/.local/bin:/usr/bin:$PATH"

RUN mkdir -p google_calc
WORKDIR /home/uchrome/google_calc

COPY . .
