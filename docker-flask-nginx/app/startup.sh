#!/bin/bash

cd /var/app

uwsgi --socket 127.0.0.1:3031 --chdir /var/app/ --wsgi-file app.py --callable app --master --processes 4 --threads 2 &

nginx -g "daemon off;"