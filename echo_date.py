#! /usr/bin/env pyhton3
import os
import sys
import time
import datetime


CHECK_SPAN = int(os.environ.get('CHECK_SPAN', '10'))


while True:
    print('date: {}'.format(datetime.datetime.now()))

    time.sleep(CHECK_SPAN)
