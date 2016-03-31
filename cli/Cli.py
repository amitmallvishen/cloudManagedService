#!/usr/bin/python

import sys
import requests

#Reading the attributes from file
with open('CliConfig.json','r') as f:
    output = f.read()
exec_code = 'payload = ' + output
exec exec_code

#Creating a URL with user input
print "sys.argv[1] ", sys.argv[1]
cliRequest = requests.post(sys.argv[1], params=payload)
print(cliRequest.text)


