#!/usr/bin/env python3

import time, os, sys
from threading import Thread
from keyring import get_credential as get_keyring_credential


password = os.getenv("LOGIN_PASS")
delay = 5 # Delay on automatic start, you may need to tune this on your system
if not password:
    os.system("notify-send 'You forgot to set your password!'")
    sys.exit()

time.sleep(delay)

def trigger_keyring_unlock_popup():
    try:
        get_keyring_credential("service", "login")
    except:
        os.system("notify-send 'Keyring unlock popup closed! (cancelled)'")

popup = Thread(target = trigger_keyring_unlock_popup)
popup.start()

def is_locked(): return popup.is_alive()

if (is_locked()):
    if (password == ""):
        os.system("notify-send 'You need to set the password!'")
        sys.exit()
    else:
        time.sleep(1)
        os.system("ydotool type " + password )
        os.system("ydotool key 28:1 28:0") # Pressing enter
        os.system("notify-send 'Keyring unlocked!'") # Give a notification

        time.sleep(0.1)
        if (is_locked()):
            os.system("notify-send 'Unlock unsuccessful, incorrect password!'")
