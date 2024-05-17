import machine
import utime
led_onboard = machine.Pin(25, machine.Pin.OUT)
speed = 4
for zeichen in [1, 1, 1, 1, 0, 1, 3, 0, 1, 3, 1, 1, 0, 1, 3, 1, 1, 0, 3, 3, 3]:
 	led_onboard.value(1)
 	utime.sleep(zeichen/speed)
 	led_onboard.value(0)
 	utime.sleep(1/(speed/2)) 