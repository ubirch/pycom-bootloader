print("SD bootloader")

import pycom
import time
import machine
import sys
import uos


#LED colors
#for errors (full brightness)
C_YELLOW = 0xffff00
C_RED = 0xff0000
C_PURPLE = 0xff00ff
C_BLUE = 0x0000ff
#for normal boot (dimmed)
C_WHITE_DIM = 0x030303
C_RED_DIM = 0x060000

### Functions ###
def mount_sd():
    try:
        sd = machine.SD()
        os.mount(sd, '/sd')
        return True
    except OSError:
        return False

def endless_blink(color1: int, color2: int):
    pycom.heartbeat(False)
    while True:
        pycom.rgbled(color1) 
        time.sleep(0.5)
        pycom.rgbled(color2)
        time.sleep(0.5)

### Main Code ###
pycom.heartbeat(False)
pycom.rgbled(C_RED_DIM)

if mount_sd():
    print("booting from SD")
    pycom.rgbled(C_WHITE_DIM) 
    #add code and lib dir on sd to import path
    sys.path.append('/sd/code')
    sys.path.append('/sd/code/lib')
    #change working dir to code directory
    try:
        uos.chdir('/sd/code')
    except Exception:
        print("code folder not found")
        endless_blink(C_PURPLE,C_RED)

    print("sys.path:")
    print(sys.path)
    print("uos.getcwd():")
    print(uos.getcwd())

    try:
        execfile('/sd/code/main.py')
    except Exception:
        print("could not execute main.py")
        endless_blink(C_BLUE,C_RED)


#sd was not mounted
print("no SD found")
endless_blink(C_YELLOW,C_RED)
