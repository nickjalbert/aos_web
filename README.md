# aos_web

# Setup heroku CLI
curl https://cli-assets.heroku.com/install-ubuntu.sh | sh
# Create virtual env
virtualenv -p /usr/bin/python3.9 env
source env/bin/activate
# Setup Django
pip install Django
django-admin startproject aos_web
cd aos_web/
./manage.py startapp registry
# Follow tutorial:
# https://docs.djangoproject.com/en/3.2/intro/tutorial01/


# Setup postgres
sudo apt install postgresql postgresql-contrib
sudo passwd postgres # aabbccdd
sudo service postgresql start
sudo -u postgres psql
postgres=# create database aos_web;
CREATE DATABASE
postgres=# create user aos_web_user with encrypted password 'aabbccdd';
CREATE ROLE
postgres=# grant all privileges on database aos_web to aos_web_user;

# added models and updated settings

./manage.py makemigrations
./manage.py migrate
python manage.py createsuperuser



