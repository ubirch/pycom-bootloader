print("SD bootloader")

import pycom
import time
import machine
import sys
import uos

### Functions ###
def mount_sd():
    try:
        sd = machine.SD()
        os.mount(sd, '/sd')
        return True
    except OSError:
        return False

### Main Code ###
pycom.heartbeat(False)
pycom.rgbled(0x060000) # red

if mount_sd():
    print("booting from SD")
    pycom.rgbled(0x030303) # white
    #add code and lib dir on sd to import path
    sys.path.append('/sd/code')
    sys.path.append('/sd/code/lib')
    #change working dir to code directory
    uos.chdir('/sd/code')
    print("sys.path:")
    print(sys.path)
    print("uos.getcwd():")
    print(uos.getcwd())
    execfile('/sd/code/main.py')

pycom.heartbeat(False)
while True:
    print("no SD found")
    pycom.rgbled(0x7f7f00) # yellow
    time.sleep(0.5)
    pycom.rgbled(0x7f0000) # red
    time.sleep(0.5)