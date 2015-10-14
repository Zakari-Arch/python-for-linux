#!/usr/bin/python
#A system Information Gathering Script
import subprocess
print ( "If you want system information enter 'sys' ")
print ( "Else if you want diskspace information enter 'space' ")
print ( "If you want all info enter 'showall' ")
a = raw_input("enter the function command :")
a = str(a)

def sys():
    uname = "uname"
    uname_arg = "-a"
    print "Gathering system information with %s command:\n" % uname
    subprocess.call([uname, uname_arg])

#Command 2
def space():
    diskspace = "df"
    diskspace_arg = "-h"
    print "Gathering diskspace information with %s command:\n" % diskspace
    subprocess.call([diskspace, diskspace_arg])

def showall():
    sys()
    print " "
    space()

if a == "sys":
    def main():
        sys()

elif a == "space":
    def main():
        space()

elif a == "showall":
    def main():
        showall()

main()
