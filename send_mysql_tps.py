__author__ = 'seckcoder'


import boto.ec2.cloudwatch
import subprocess
import time
from datetime import datetime
import sys

region = "us-east-1"
cw = boto.ec2.cloudwatch.connect_to_region(region)

metric_base = {
    "namespace" : 'SECK/EC2',
    "name" : 'TPSUtilization',
    "unit" : "Percent",
    "dimensions" : {"AutoScalingGroupName" : "seck-asg"}
}

max_tps = 500

def sendTPS(tps):
    cf = metric_base.copy()
    cf.update(value = (float(tps) / float(max_tps)) * 100,
              timestamp = datetime.utcnow())
    cw.put_metric_data(**cf)

prev_queries = None
prev_uptime = None

#uname = "echo"
#password = "15319"

uname = "root"
password = "db15319root"

print "start send..."
while True:
    try:
        print "inprocess...."
        sys.stdout.flush()
        output = subprocess.check_output("mysql -u %s -p%s -e \"show status like 'Queries'; show status like 'Uptime';\"" % (uname, password), shell=True)
        groups = output.split()
        queries = int(groups[3])
        uptime = int(groups[7])
        if prev_queries is not None:
            tps = (queries - 4 - prev_queries) / (uptime - prev_uptime)
            sendTPS(tps)
            print tps
            sys.stdout.flush()
        prev_queries = queries
        prev_uptime = uptime
        # tps = int(output.split()[3])
        time.sleep(1)
    except KeyboardInterrupt:
        print "keyboard interrupt"
        break
