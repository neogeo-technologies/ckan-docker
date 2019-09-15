#!/bin/bash

/idgo_venv/bin/python manage.py migrate && /idgo_venv/bin/python manage.py collectstatic

