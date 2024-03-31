#!/usr/bin/python3
"""
fetch argv1
display content 
"""
import requests as req
import sys

url = sys.argv[1]
email = sys.argv[2]
payload = {'email': email}
reponse = req.post(url, data=payload)
print(reponse.text)
