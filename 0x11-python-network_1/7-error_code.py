#!/usr/bin/python3
"""
fetch argv1
display status code 
"""
import requests as req
import sys

url = sys.argv[1]

reponse = req.get(url)
if reponse.status_code >= 400:
	print("Error code:", response.status_code)
else:
	print(reponse.text)
