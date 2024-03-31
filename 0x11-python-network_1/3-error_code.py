#!/usr/bin/python3
"""
fetch argv1
display the status error code 
"""
import sys
from urllib import request, error
url = sys.argv[1]
try:
	with request.urlopen(sys.argv[1]) as res:
		print(res.read().decode('UTF-8'))
except error.HTTPError as er:
	print('Error code:', er.code)
