# Projekt Pausengong

**Autor:** Fabian Siebels

Projekt: https://github.com/Fabian-Siebels/Pausengong

Download: `git clone https://github.com/Fabian-Siebels/Pausengong.git`

**Inhalt:**
 1. Aufbau
 2. Gongzeiten ändern
 3. Gongsound ändern

## 1. Aufbau

Der Pausengong besteht aus einem Raspberry Pi 3 und einem Python Script. Als Betriebssystem wird Raspian Stretch verwendet.
Der Pi wird per AUX Kabel an das Soundsystem angeschlossen.

## 2. Gongzeiten ändern

Das Script für den Gong wird mit einem Cronjob gesteuert.

Eingetragen sind die Gongzeiten in der Datei `crontab -e`.
Um diese aufzurufen, muss entweder als root `crontab -e` oder als user `sudo crontab` eingegeben werden.

| Uhrzeit | Cronjob |
|--|--|
|Mon-Don||
| 7:15 | `15 7 * * 1-4 /usr/bin/python /home/pi/Pausengong/gong.py >/dev/null 2>&1` |
| 9:30 | `30 9 * * 1-4 /usr/bin/python /home/pi/Pausengong/gong.py >/dev/null 2>&1` |
| 9:45 | `45 9 * * 1-4 /usr/bin/python /home/pi/Pausengong/gong.py >/dev/null 2>&1` |
|11:30 | `30 11 * * 1-4 /usr/bin/python /home/pi/Pausengong/gong.py >/dev/null 2>&1`|
|12:00 |`0 12 * * 1-4 /usr/bin/python /home/pi/Pausengong/gong.py >/dev/null 2>&1`|
|14:45 |`45 14 * * 1-4 /usr/bin/python /home/pi/Pausengong/gong.py >/dev/null 2>&1`|
|15:00 |`0 15 * * 1-4 /usr/bin/python /home/pi/Pausengong/gong.py >/dev/null 2>&1`|
|16:15 |`15 16 * * 1-4 /usr/bin/python /home/pi/Pausengong/gong.py >/dev/null 2>&1`|
|Fri||
|7:00 |`0 7 * * 5 /usr/bin/python /home/pi/Pausengong/gong.py >/dev/null 2>&1`|
|9:30 |`30 9 * * 5 /usr/bin/python /home/pi/Pausengong/gong.py >/dev/null 2>&1`|
|9:45 |`45 9 * * 5 /usr/bin/python /home/pi/Pausengong/gong.py >/dev/null 2>&1`| 
|12:00 |`0 12 * * 5 /usr/bin/python /home/pi/Pausengong/gong.py >/dev/null 2>&1`|   

## 3. Gongsound ändern

Der Gongsound wird in der Python Datei `Pausengong/gong.py` geändert, dazu muss der Sound in dem Verzeichnis `/home/pi/Pausengong` als **gongsound.wav** vorhanden sein. Falls das System verändert wird, muss der Pfad angepasst werden.

