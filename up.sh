#!/bin/bash

echo "Running server..."

export FLASK_APP=app/app.py

flask run --host 0.0.0.0 --no-reload
