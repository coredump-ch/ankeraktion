#!/usr/bin/env python3
from urllib.request import urlopen

url = 'http://www.aktionis.ch/coop,coop_megastore,denner/bier'
response = urlopen(url)
html = response.read()
if b'Anker Lagerbier' in html:
    print('Anker ist Aktion!')
else:
    print('Anker leider nicht Aktion')
