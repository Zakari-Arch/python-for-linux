#!/usr/bin/python

#Information Gathering Script
import subprocess

subprocess.call(["sudo","nmap","-PY","192.168.1.1/24"])
sudo="sudo"
nmap="nmap"
nmap_arg="-PY"
nmap_arg2="192.168.1.1/24"

print "Network exploration and Port Scanning with %s tool:\n" % nmap 
subprocess.call([sudo, nmap, nmap_arg, nmap_arg2 ])
