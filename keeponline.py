from pynput.keyboard import Controller, Key
import signal
import time

keyboard = Controller()

#============below part can handle Ctrl + C cmd and make sure the cap_lock can be cleared================
def signal_handler(sig, frame):
    keyboard.press(Key.caps_lock)
    keyboard.release(Key.caps_lock)
    keyboard.press(Key.caps_lock)
    keyboard.release(Key.caps_lock)
    exit(0)

signal.signal(signal.SIGINT, signal_handler)
#===========end of the Ctrl + C CMD part=================================================================

while True:
    print('=')
    keyboard.press(Key.caps_lock)
    keyboard.release(Key.caps_lock)
    keyboard.press(Key.caps_lock)
    keyboard.release(Key.caps_lock)
    time.sleep(60)
