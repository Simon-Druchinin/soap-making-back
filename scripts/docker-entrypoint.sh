#!/bin/sh

set -e

. /venv/bin/activate

exec python manage.py runserver 0.0.0.0:8000
