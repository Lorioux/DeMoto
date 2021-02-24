# update and upgrade
apk update && apk upgrade

# install git package
apk add git

# install python and packages
apk add python3 py3-pip

# upgrade pip
pip install --upgrade pip

cd /demoto
#source .venv/bin/activate

# install dependencies from requirements.txt
if [ -f requirements.txt ]; then 
  pip install -r requirements.txt
fi

# make migration and migrate databases
#python3 manage.py makemigrations
#python3 manage.py migrate

# run the webserver
python3 manage.py runserver 8000
