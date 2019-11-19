import time, board, busio
import bq25883
 
i2c = busio.I2C(board.SCL, board.SDA) 
usb = bq25883.BQ25883(i2c)

usb.charging=False
usb.wdt=False
usb.led=True

while True:
    usb.status
    print('')

    time.sleep(1)
