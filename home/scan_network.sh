#!/bin/bash

if [[ "$UID" != "0" ]]; then
   echo "This script must be run as root!"
   exit 1
elif [[ "$#" -ne 1 ]]; then
   echo "This script can only have 1 argument!"
   exit 1
fi

NMAP=$(nmap -Pn $1)
echo "$NMAP" | grep -iq "Host is up"
