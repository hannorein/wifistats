import MySQLdb
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
import sys
import time
ts = time.time()
db=MySQLdb.connect("127.0.0.1","wifistats","uoft","uoftwifistats",port=3306)
c = db.cursor()

locations=["MP","AB","EV","SW"]

fig, ax = plt.subplots(1,1,sharex=True, figsize=(4,4),squeeze=False)
scalex = 60*60
ax[0][-1].set_xlabel("time [hours]")

for location in locations:
    numrows = c.execute("SELECT UNIX_TIMESTAMP(date), count FROM stats WHERE date > (UNIX_TIMESTAMP() - 60*60*24) AND location='%s'"%location)
    A = np.zeros((numrows,2))
    for i,r in enumerate(c.fetchall()):
        A[i] = r
    ax[0][0].plot((A[:,0]-ts)/scalex,A[:,1], label=location)
ax[0][0].set_ylabel("users")
ax[0][0].legend()
fig.tight_layout() 

fig.savefig("users.png")


