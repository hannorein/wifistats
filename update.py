urlmp = "https://maps.wireless.utoronto.ca/stg/popUp.php?name=0078"
urlab = "https://maps.wireless.utoronto.ca/stg/popUp.php?name=0036"

import urllib.request
contents = urllib.request.urlopen(urlmp).read()
r = contents.decode("utf-8").split("Number of people : <BQ>")[1].split("<P><font")[0]
pmp = int(r)
contents = urllib.request.urlopen(urlab).read()
r = contents.decode("utf-8").split("Number of people : <BQ>")[1].split("<P><font")[0]
pab = int(r)
print("MP", pmp)
print("AB", pab)
import os
os.system("gmetric -n \"People in MP\" -v %d -t \"uint32\""%pmp)
os.system("gmetric -n \"People in AB\" -v %d -t \"uint32\""%pab)
