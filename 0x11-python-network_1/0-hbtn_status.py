#!/usr/bin/python3
"""
fetch <url>
use urllib module
"""
import urllib.request  # Importe le module urllib.request

url = 'https://alx-intranet.hbtn.io/status'  # Définit l'URL à récupérer

with urllib.request.urlopen(url) as response:  # Ouvre une connexion avec l'URL
    html = response.read()  # Lit le contenu de la réponse
    print("Body response:")  # Affiche un titre
    print("\t- type: {}".format(type(html)))  # Affiche le type du contenu
    print("\t- content: {}".format(html))  # Affiche le contenu brut
    print("\t- utf8 content: {}".format(html.decode('utf-8'))) 
