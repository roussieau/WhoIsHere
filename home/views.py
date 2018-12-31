from django.shortcuts import render
import subprocess

SCRIPT_PATH = "./scan_network.sh"

def scan(ip):
   return subprocess.call([SCRIPT_PATH, ip])
