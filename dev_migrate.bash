#!/usr/bin/env bash

./manage.py makemigrations --settings=config.settings.development
./manage.py migrate --settings=config.settings.development