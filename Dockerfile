FROM python:latest

# Installing Packages
RUN apt update && apt upgrade -y
RUN apt install git
RUN apt install curl
RUN apt install python3-pip

# Updating Pip Packages
RUN pip3 install -U pip

# Copying Requirements
COPY requirements.txt /requirements.txt

# Installing Requirements
RUN cd /
RUN pip3 install -U -r requirements.txt
RUN mkdir /afkbot
WORKDIR /afkbot
COPY start.sh /start.sh

# Running MessageSearchBot
CMD ["/bin/bash", "/start.sh"]
