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

pin = [machine.Pin(14, machine.Pin.OUT), machine.Pin(12, machine.Pin.OUT), machine.Pin(13, machine.Pin.OUT)]

contador_ms = [CuentaMs(1000), CuentaMs(333), CuentaMs(698)]

while True:
    time.sleep(0.1)
    for i in range(len(contador_ms)):
        if contador_ms[i].comprueba():
            pin[i].value(not pin[i].value())
            print(" "* i, i, "ha pasado su tiempo")
            contador_ms[i].reset()
        

    