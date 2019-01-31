import machine, micropython
micropython.alloc_emergency_exception_buf(100)
class ManejaLed(object):
    def __init__(self, timer, pin, periodo):
        self.pin = pin
        self.timer = timer
        self.timer.init(period=periodo, mode=machine.Timer.PERIODIC, callback=self.cb)
    def cb(self, timer):
        self.pin.value(not self.pin.value())
        # self.led.toggle()
    def deinit(self):
        self.timer.deinit()
azul = ManejaLed(machine.Timer(0) , machine.Pin(16,machine.Pin.OUT), 1000)
blanco = ManejaLed(machine.Timer(1), machine.Pin(12,machine.Pin.OUT), 333)
============ tiempo.py
import time, machine
class CuentaMs():
    def __init__(self, ms):
        self.ms = ms
        self.actual = time.ticks_ms()
        self.proximo = self.actual + self.ms
    def reset(self):
        self.actual = time.ticks_ms()
        self.proximo = self.actual + self.ms
    def comprueba(self):
        if self.proximo <= time.ticks_ms():
            return True
        else:
            return False
contador_ms = CuentaMs(1000)
pin = machine.Pin(14, machine.Pin.OUT)
while True:
    time.sleep(0.1)
    if contador_ms.comprueba():
        pin.value(not pin.value())
        print("Ha pasado un segundo")
        contador_ms.reset()
============ tiempo2.py
import time, machine
class CuentaMs():
	#como en tiempo.py
	pass
pin = [machine.Pin(14, machine.Pin.OUT), machine.Pin(12, machine.Pin.OUT), machine.Pin(13, machine.Pin.OUT)]
contador_ms = [CuentaMs(1000), CuentaMs(333), CuentaMs(698)]
while True:
    time.sleep(0.1)
    for i in range(len(contador_ms)):
        if contador_ms[i].comprueba():
            pin[i].value(not pin[i].value())
            print(" "* i, i, "ha pasado su tiempo")
            contador_ms[i].reset()
