#!/usr/bin/env python3
'''
Install the following Operating system: Raspberry Pi OS with desktop
Availble here: https://www.raspberrypi.org/software/operating-systems/
'''

import os

'''
Update password
'''
os.system('passwd')
'''
Current password: Ecpi2021
New password: [Your new password here]
Retype new password:  [Your new password here]
'''

'''
Update and install dependencies
'''
os.system('sudo apt update')
os.system('sudo apt full-upgrade')
os.system('pip3 install gTTS')
os.system('cd .config/ && mkdir autostart/ && mkdir /home/pi/ECPI && mkdir /home/pi/ECPI/Motion && mkdir /home/pi/ECPI/Storage && mkdir /home/pi/ECPI/.autostart')
os.system('sudo apt install rpi-imager -y')
os.system('pip3 install pynput')
os.system('sudo apt install samba samba-common') #yes then no
os.system('sudo apt install fswebcam -y')
os.system('sudo usermod -a -G video pi')

'''
Set date/time: %a, %b %d, %Y  |  %r
Chromium: Set homepages to the following two:
https://inns.ecpi.net
https://projects.raspberrypi.org/en
'''

'''
NumLock on Startup
'''
os.system('cd /home/pi/ECPI/.autostart')
os.system('chmod +x numlock.py')

