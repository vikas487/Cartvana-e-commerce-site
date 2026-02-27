#!/bin/bash
echo "Building project..."
python3 -m pip install -r requirements.txt

echo "Make Migration..."
python3 ecommerce/manage.py makemigrations
python3 ecommerce/manage.py migrate

echo "Collect Static..."
python3 ecommerce/manage.py collectstatic --noinput --clear
