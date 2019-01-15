#!/bin/bash

# Path to arp-scan utility
ARP_SCAN_PATH="/usr/local/bin/arp-scan"
# Path to python3 in the virtual env of the project
PYTHON3_PATH="/Users/laurent/.local/share/virtualenvs/WhoIsHere-LiYgw31X/bin/python3"
# Path to manage.py of the project
MANAGE_PATH="/Users/laurent/Documents/CarpeStudentem/WhoIsHere/manage.py"
# Number of retries for each host
RETRY="7"
# Name of the user running the project
USER="laurent"



if [[ "$UID" != "0" ]]; then
   echo "This script must be run as root!"
   exit 1
fi


scan="$($ARP_SCAN_PATH --retry=$RETRY --localnet)"

sudo -u $USER bash << EOF
  $PYTHON3_PATH $MANAGE_PATH add_online_logs "$scan"
EOF
