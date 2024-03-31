#!/usr/bin/python3
"""
fetch argv1
post an email argv2
display the content
"""
import urllib.request
import sys

url = sys.argv[1]
email = sys.argv[2]

data = urllib.parse.urlencode({'email': email}).encode('utf-8')
req = urllib.request.Request(url, data=data, method='POST')

with urllib.request.urlopen(req) as response:
    html = response.read()
    print(html.decode('utf-8'))
