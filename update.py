urlsg = "https://maps.wireless.utoronto.ca/stg/popUp.php?name="
urlmp = "https://maps.wireless.utoronto.ca/stg/popUp.php?name=0078"
urlab = "https://maps.wireless.utoronto.ca/stg/popUp.php?name=0036"
urlutsc = "https://utsc.utoronto.ca/webapps/wirelessmap/map/get_location_summary"

ids = ["X073 ", "0047 ", "0131 ", "0049 ", "0036 ", "0078 ", "0075 ", "0073 ", "0003 ", "0072 ", "A068 ", "0033 ", "0064 ", "0068 ", "0146 ", "0032 ", "X033 ", "0028 ", "0079 ", "0143 ", "0930 ", "0067 ", "0080 ", "0110 ", "0104 ", "0103 ", "0042 ", "0089 ", "0077 ", "A006 ", "0088 ", "0038 ", "0006 ", "0106 ", "0066 ", "0134 ", "0133 ", "0132 ", "0128 ", "0127 ", "B006 ", "0130 ", "0052 ", "0016 ", "0065 ", "0194 ", "0145 ", "0062 ", "0061 ", "0056 ", "0057 ", "A061 ", "0161 ", "0154 ", "0083 ", "0160 ", "0192 ", "0155 ", "0024 ", "0020 ", "0011 ", "0022 ", "0007 ", "0009 ", "0027 ", "0026 ", "0172 ", "0043 ", "0021 ", "0019 ", "0008 ", "0153 ", "A008 ", "0010 ", "A010 ", "0575 ", "0070 ", "0508 ", "0675 ", "A098 ", "0455 ", "0603 ", "0453 ", "0608 ", "0505 ", "0443 ", "0435 ", "0434 ", "0429 ", "0418 ", "0602 ", "0501 ", "0507 ", "0509 ", "0514 ", "A030 ", "0504 ", "0098 ", "0515 ", "B012 ", "0012 ", "0518 ", "0503 ", "0502 ", "0506 ", "0600 ", "0417 ", "0030 ", "0123 ", "0101 ", "0051 ", "0034 ", "0001 ", "0528 ", "0053 ", "0023 ", "0041 ", "0029 ", "505A ", "0013 ", "0002 ", "0411 ", "0401 ", "0415 ", "0405 ", "0050 ", "0152 ", "XINN ", "0004 ", "097A ", "0092 ", "A005 ", "0196 ", "0025 ", "XMSB ", "XMUS ", "0005 ", "0014 ", "XXSU ", "XXFC ", "XXBC ", "XWDW ", "XVIC ", "XLAW ", "XVAR ", "XSMC ", "XROB ", "XNEW ", "B010 ", "XESC ", "A032 ", "0138 ", "0142 ", "0156 ", "0158 ", "0171 ", "0195 ", "0430 ", "0407 ", "0426 ", "0423 ", "0421 ", "0420 ", "0419 ", "0129 ", "0125 ", "0087 ", "0040 ", "0530 ", "0054 ", "0071 ", "0082 ", "0090 ", "0091 ", "0097 ", "0105 ", "0111 ", "0115 ", "0120 ", "0416 "]

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
    psw = int(contents["data"]["records"]["sw"]["numStations"])
except:
    print("error sw")
    psw = 0
try:
    pev = int(contents["data"]["records"]["ev"]["numStations"])
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


s = 0
for i in ids:
    print(i)
    contents = urllib.request.urlopen(urlsg+i.strip()).read()
    r = contents.decode("utf-8").split("Number of people : <BQ>")[1].split("<P><font")[0]
    print(r)
    try: 
        n = int(r)
    except:
        n = 0
    s += n
print("St George", s)
os.system("gmetric -n \"People in St George\" -v %d -t \"uint32\""%s)
