#!/usr/bin/env bash

curl https://raw.githubusercontent.com/seckcoder/cloud-p7/master/send_mysql_tps.py -o ~/bin/send_mysql_tps.py
python ~/bin/send_mysql_tps.py &>~/log/mysql_tps.log &
