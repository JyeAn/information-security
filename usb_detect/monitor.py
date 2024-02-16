import pyudev
import os
import logging

context=pyudev.Context()
monitor=pyudev.Monitor.from_netlink(context)
monitor.filter_by(subsystem='usb')
logging.basicConfig(level=logging.DEBUG,
filename='./output.log',
datefmt='%Y/%m/%d %H:%M:%S',
format='%(asctime)s-%(name)s-%(levelno)s-%(message)s')
logger=logging.getLogger("monitor")

for device in iter(monitor.poll,None):
    if device.action == 'add' :
        print('{} connected)'.format(device))
        os.popen('gnome-screensaver-command --lock')
        logger.info('{} connected)'.format(device))
    elif device.action == 'remove' :
        print('{} removed)'.format(device))
        logger.info('{} removed)'.format(device))
    
