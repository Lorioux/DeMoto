#!/usr/bin/env

# update and upgrade
apk update && apk upgrade

# install python and packages
apk add python3 py3-pip

# upgrade pip
pip install --upgrade pip

# install dependencies from requirements.txt
if [ -f requirements.txt ]; then 
  pip install -r requirements.txt
fi


