# pycom-bootloader
Simple bootloader for pycom devices to run code from SD instead of internal flash.
Simply copy your project as-is to a subfolder called 'src' on the SD root.
(So you end up with SD_root/src/main.py, SD_root/src/lib/yourlib.py, ... )

LED Color Codes:
Dim white: booting
Flashing yellow/red: SD card not found
Flashing purple/red: code folder not accessible
Flashing blue/red: can't execute main.py