#!/usr/bin/env bash

target_fname=send_mysql_tps.py
mkdir -p ~/bin/
curl https://raw.githubusercontent.com/seckcoder/cloud-p7/master/send_mysql_tps.py -o ~/bin/$target_fname
mkdir -p ~/log/
python ~/bin/$target_fname 2>&1 1>~/log/send_mysql.log &
