#!/usr/bin/python

#Information Gathering Script
import subprocess

print "Network exploration and Port Scanning with Nmap tool:\n" 
subprocess.call(["nmap" ,"192.168.1.1/24"])
#sudo="sudo"
nmap="nmap"
#nmap_arg="-PY"
nmap_arg2="192.168.1.1/24"

 
subprocess.call([nmap, nmap_arg2 ])

