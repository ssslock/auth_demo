import time
import sys

__log_file__ = None

def init(fileName):
    global __log_file__
    if __log_file__:
        __log_file__.close()
    if fileName:
        __log_file__ = open(fileName, 'w+')

def log(data):
    timestr = time.strftime('%Y-%m-%d %A %X %Z  ',time.localtime(time.time()))
    __log_file__.write(timestr + data + '\n')