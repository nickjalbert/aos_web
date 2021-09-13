# aos_web

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


# Heroku deployment
# https://medium.com/geekculture/how-to-deploy-a-django-app-on-heroku-4d696b458272
pip3 install gunicorn dj-database-url whitenoise psycopg2-binary
# Setup heroku CLI
curl https://cli-assets.heroku.com/install-ubuntu.sh | sh
# Bunch of settings.py updates from the medium article
heroku create aos-web

