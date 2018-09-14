#Gong by Fabian Siebels

import subprocess
import sys
from time import sleep


subprocess.Popen(["aplay","/home/pi/gong.wav"], stdin=subprocess.PIPE)
sleep(10)

sys.exit()

# Cronjobs werden mit root Rechten mit dem Befehl crontab -e eingegeben.

#Cronjobs

#Anfang MON-DON
#*/15 7 * * 1-4 /usr/bin/python /home/pi/gong.py >/dev/null 2>&1
#Fruehstueck
#*/30 9 * * 1-4 /usr/bin/python /home/pi/gong.py >/dev/null 2>&1
#*/45 9 * * 1-4 /usr/bin/python /home/pi/gong.py >/dev/null 2>&1
#Mittag
#*/30 11 * * 1-4 /usr/bin/python /home/pi/gong.py >/dev/null 2>&1
#*/ 12 * * 1-4 /usr/bin/python /home/pi/gong.py >/dev/null 2>&1
#Nachmittag
#*/45 14 * * 1-4 /usr/bin/python /home/pi/gong.py >/dev/null 2>&1
#*/ 15 * * 1-4 /usr/bin/python /home/pi/gong.py >/dev/null 2>&1
#Freitag
#Anfang
#*/ 7 * * 1-4 /usr/bin/python /home/pi/gong.py >/dev/null 2>&1
#Fruehstueck
#*/30 9 * * 5 /usr/bin/python /home/pi/gong.py >/dev/null 2>&1
#*/45 9 * * 1-4 /usr/bin/python /home/pi/gong.py >/dev/null 2>&1
#Frei
#*/ 12 * * 1-4 /usr/bin/python /home/pi/gong.py >/dev/null 2>&1
