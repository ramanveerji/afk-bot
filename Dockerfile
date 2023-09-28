FROM python:latest

# Installing Packages
RUN apt update && apt upgrade -y
RUN apt install git
RUN apt install curl

# Updating Pip Packages
RUN pip3 install -U pip
RUN apt-get update && apt-get install -y libffi-dev libssl-dev


# Copying Requirements
COPY requirements.txt /requirements.txt

# Installing Requirements
RUN cd /
RUN pip3 install --no-cache-dir -U -r requirements.txt
RUN mkdir /afkbot
WORKDIR /afkbot
COPY start.sh /start.sh

# Running MessageSearchBot
CMD ["/bin/bash", "/start.sh"]
