import machine
import utime
led_onboard = machine.Pin(25, machine.Pin.OUT)
for i in range(2):
	led_onboard.value(1)
	utime.sleep(1)
	led_onboard.value(0)
	utime.sleep(1) 