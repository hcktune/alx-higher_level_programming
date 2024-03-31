#!/usr/bin/python3
"""
fetch argv1
display content 
"""
import requests as req
import sys

url = sys.argv[1]
reponse = req.get(url)
print(reponse.headers.get('X-Request-Id'))
