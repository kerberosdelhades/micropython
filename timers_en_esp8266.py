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

