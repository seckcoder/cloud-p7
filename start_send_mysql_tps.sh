#!/usr/bin/env bash

curl https://bitbucket.org/seckcoder/cloud-storage/raw/72e5dd4d97842c9fd2db40654bd585406db4ade9/send_mysql_tps.py -o /bin/send_msql_tps.py

(
python /bin/send_mysql_tps.py 2>1 1>/var/log/send_mysql
)

