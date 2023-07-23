#!/bin/bash
current_date_time=`date +%F-%T`
echo "Current date and time: $current_date_time"
filename="${1%%.*}"
filename='logs/'$filename'_'$current_date_time
echo "$filename"
logging=--log-cli-level=$2' '--capture=tee-sys' '--log-file=$filename'.log'
HTML=--html=$filename'.html '--self-contained-html
ALLURE=--alluredir="logs/allure"
#pytest $1 --log-cli-level=INFO --capture=tee-sys --log-file=$filename'.log' --html=$filename'.html' --self-contained-html
pytest $1 $logging $HTML $ALLURE