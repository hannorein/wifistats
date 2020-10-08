urlmp = "https://maps.wireless.utoronto.ca/stg/popUp.php?name=0078"
urlab = "https://maps.wireless.utoronto.ca/stg/popUp.php?name=0036"
urlutsc = "https://utsc.utoronto.ca/webapps/wirelessmap/map/get_location_summary"

import urllib.request
import json
import os
contents = urllib.request.urlopen(urlmp).read()
r = contents.decode("utf-8").split("Number of people : <BQ>")[1].split("<P><font")[0]
pmp = int(r)
contents = urllib.request.urlopen(urlab).read()
r = contents.decode("utf-8").split("Number of people : <BQ>")[1].split("<P><font")[0]
pab = int(r)

req = urllib.request.Request(urlutsc)
req.add_header('X-Requested-With', 'XMLHttpRequest')
contents = json.loads(urllib.request.urlopen(req).read().decode("utf-8"))
try:
    psw = int(contents["data"]["records"]["sw"]["stations"])
except:
    print("error sw")
    psw = 0
try:
    pev = int(contents["data"]["records"]["ev"]["stations"])
except:
    print("error ev")
    pev = 0

print("MP", pmp)
print("AB", pab)
print("SW", psw)
print("EV", pev)
os.system("gmetric -n \"People in MP\" -v %d -t \"uint32\""%pmp)
os.system("gmetric -n \"People in AB\" -v %d -t \"uint32\""%pab)
os.system("gmetric -n \"People in SW\" -v %d -t \"uint32\""%psw)
os.system("gmetric -n \"People in EV\" -v %d -t \"uint32\""%pev)
