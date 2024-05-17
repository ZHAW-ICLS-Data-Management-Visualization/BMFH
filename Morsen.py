import machine
import utime
led_onboard = machine.Pin(25, machine.Pin.OUT)
for zeichen in [1, 1, 1, 1, 0, 1, 2, 0, 1, 2, 1, 1, 0, 1, 2, 1, 1, 0, 2, 2, 2]:
 	led_onboard.value(1)
 	utime.sleep(zeichen)
 	led_onboard.value(0)
 	utime.sleep(1) 