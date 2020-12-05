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

# make migration and migrate databases
python3 manage.py makemigrations
python3 manage.py migrate

