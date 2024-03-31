#!/usr/bin/python3
"""
fetch argv1
display status code 
"""
import requests as req
import sys

url = "http://1d464bb1ad40.115532cb.alx-cod.online/search_user" 
if len(sys.argv) < 2:
	q = ""
else:
	q = sys.argv[1]

try:
	response = req.post(url, data={'q': q})
	data = response.json()
	if data:
		print("[{}] {}".format(data['id'], data['name']))
	else:
		print("No result")
except ValueError:
	print("Not a valid JSON")
