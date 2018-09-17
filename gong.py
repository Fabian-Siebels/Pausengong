#Gong by Fabian Siebels

# Klassenimport
import subprocess
import sys
from time import sleep

#Öffnen und abspielen einer .wav Datei
# /home/pi/Pausengong/... ist der Pfad, wo sich die .wav Datei befindet.
subprocess.Popen(["aplay","/home/pi/Pausengong/gongsound.wav"], stdin=subprocess.PIPE)
sleep(10)

sys.exit()

# Cronjobs werden mit root Rechten mit dem Befehl crontab -e eingegeben.

#Cronjobs

#| Uhrzeit | Cronjob |
#|--|--|
#|Mon-Don||
#| 7:15 | `*/15 7 * * 1-4 /usr/bin/python /home/pi/Pausengong/gong.py >/dev/null 2>&1` |
#| 9:30 | `*/30 9 * * 1-4 /usr/bin/python /home/pi/Pausengong/gong.py >/dev/null 2>&1` |
#| 9:45 | `*/45 9 * * 1-4 /usr/bin/python /home/pi/Pausengong/gong.py >/dev/null 2>&1` |
#|11:30 | `*/30 11 * * 1-4 /usr/bin/python /home/pi/Pausengong/gong.py >/dev/null 2>&1`|
#|12:00 |`*/ 12 * * 1-4 /usr/bin/python /home/pi/Pausengong/gong.py >/dev/null 2>&1`|
#|14:45 |`*/45 14 * * 1-4 /usr/bin/python /home/pi/Pausengong/gong.py >/dev/null 2>&1`|
#|15:00 |`*/ 15 * * 1-4 /usr/bin/python /home/pi/Pausengong/gong.py >/dev/null 2>&1`|
#|16:15 |`*/15 16 * * 1-4 /usr/bin/python /home/pi/Pausengong/gong.py >/dev/null 2>&1`|
#|Fri||
#|7:00 |`*/ 7 * * 5 /usr/bin/python /home/pi/Pausengong/gong.py >/dev/null 2>&1`|
#|9:30 |`*/30 9 * * 5 /usr/bin/python /home/pi/Pausengong/gong.py >/dev/null 2>&1`|
#|9:45 |`*/45 9 * * 5 /usr/bin/python /home/pi/Pausengong/gong.py >/dev/null 2>&1`| 
#|12:00 |`*/ 12 * * 5 /usr/bin/python /home/pi/Pausengong/gong.py >/dev/null 2>&1`|   
