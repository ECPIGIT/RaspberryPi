#!/usr/bin/env python3
# #Script to automatically turn the num lock on when Raspberry Pi boot
from pynput.keyboard import Key, Controller
keyboard = Controller()
print(keyboard.press(Key.num_lock))
print(keyboard.release(Key.num_lock))