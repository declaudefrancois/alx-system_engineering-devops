#!/bin/bash
# Start Gunicorn to serve web_dynamic/2-hbnb.py

export PATH=/bin:/usr/bin:/usr/local/bin:/home/ubuntu/.local/bin
export HBNB_MYSQL_USER=hbnb_dev
export HBNB_MYSQL_PWD=hbnb_dev_pwd
export HBNB_MYSQL_HOST=localhost
export HBNB_MYSQL_DB=hbnb_dev_db
export HBNB_TYPE_STORAGE=db

cd /home/ubuntu/AirBnB_clone_v2/ && gunicorn --bind 0.0.0.0:5000 web_flask.0-hello_route:app  --daemon
cd /home/ubuntu/AirBnB_clone_v2/ && gunicorn --bind 0.0.0.0:5001 web_flask.6-number_odd_or_even:app  --daemon
cd /home/ubuntu/AirBnB_clone_v3/ && gunicorn --bind 0.0.0.0:5002 api.v1.app:app  --daemon
cd /home/ubuntu/AirBnB_clone_v4/ && gunicorn --bind 0.0.0.0:5003 web_dynamic.2-hbnb:app  --daemon --access-logfile /tmp/airbnb-access.log --error-logfile /tmp/airbnb-error.log --workers 3

