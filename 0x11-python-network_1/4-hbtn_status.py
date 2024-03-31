#!/usr/bin/python3
"""
fetch argv1
display content 
"""
import requests as req

response = req.get("https://alx-intranet.hbtn.io/status")
print("Body reponse:")
print("\t- type: {}".format(type(response.text)))
print("\t- content: {}".format(response.text))
			
