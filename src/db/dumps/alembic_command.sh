#!/bin/bash

PROJECT_ROOT=/

cd /app 

DATE=$(date +%Y-%m-%d-%H:%M)


read -p "Enter migration message: " MESSAGE


alembic revision --autogenerate -m "${DATE}_${MESSAGE}"


alembic upgrade head
