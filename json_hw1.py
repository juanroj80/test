import urllib.request, urllib.parse, urllib.error
import json

while True:
    address=input('Enter URL:  ')
    if len(address)<1:
        break
    uh=urllib.request.urlopen(address)
    data=uh.read().decode()

    cuenta=0

    try:
        js=json.loads(data)
    except:
        js=None

    for item in js['comments']:
        u=item['count']
        u=int(u)
        cuenta=cuenta+u

    print('El número de comentarios es: ',cuenta)
