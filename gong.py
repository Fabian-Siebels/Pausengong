#Gong by Fabian Siebels

import subprocess
import sys
from time import sleep


subprocess.Popen(["aplay","/home/pi/gong.wav"], stdin=subprocess.PIPE)
sleep()

sys.exit()

#Cronjobs

# Montag bis Donnerstag

# 7:15 Uhr:     0 15 7 ? * MON,TUE,WED,THU * /usr/bin/python /home/pi/gong.py >/dev/null 2>&1      
# 9:30 Uhr:     0 30 9 ? * MON,TUE,WED,THU * /usr/bin/python /home/pi/gong.py >/dev/null 2>&1

# 11:30 Uhr:    0 30 11 ? * MON,TUE,WED,THU * /usr/bin/python /home/pi/gong.py >/dev/null 2>&1   
# 14:45 Uhr:    0 45 14 ? * MON,TUE,WED,THU * /usr/bin/python /home/pi/gong.py >/dev/null 2>&1

# 16:15 Uhr:    0 15 16 ? * MON,TUE,WED,THU * /usr/bin/python /home/pi/gong.py >/dev/null 2>&1

# Freitag

# 7:00 Uhr:     0 0 7 ? * FRI * /usr/bin/python /home/pi/gong.py >/dev/null 2>&1
# 9:30 Uhr:     0 30 9 ? * FRI * /usr/bin/python /home/pi/gong.py >/dev/null 2>&1

# 12:00 Uhr:    0 0 12 ? * FRI * /usr/bin/python /home/pi/gong.py >/dev/null 2>&1
