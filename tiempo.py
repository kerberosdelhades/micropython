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
    

    