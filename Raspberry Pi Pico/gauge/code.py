import adafruit_ili9341
import board, busio
import displayio
from gauge import Gauge #get the library here: https://github.com/benevpi/Circuit-Python-Gauge

displayio.release_displays()

mosi_pin = board.GP11
clk_pin = board.GP10
reset_pin = board.GP17
cs_pin = board.GP18
dc_pin = board.GP16

spi = busio.SPI(clock=clk_pin, MOSI=mosi_pin)

display_bus = displayio.FourWire(spi, command=dc_pin, chip_select=cs_pin, reset=reset_pin)

display = adafruit_ili9341.ILI9341(display_bus, width=240, height=320, rotation=270)

gauge = Gauge(0,100, 120, 120, value_label="x:", arc_colour=0xFF0000, colour=0xFFFF00, outline_colour=0xFFFF00)
gauge.x = 60
gauge.y = 0

gauge2 = Gauge(0,100, 120, 120, value_label="y:", arc_colour=0xFF0000, colour=0xFFFF00, outline_colour=0xFFFF00)
gauge2.x = 60
gauge2.y = 150

group = displayio.Group(scale=1)

group.append(gauge)
group.append(gauge2)

display.show(group)
display.auto_refresh = True

x = 0
y = 100

while True:
    while x < 100:
        x += 2
        y -= 2
        gauge.update(x)
        gauge2.update(y)
        
    while x > 0:
        x -= 2
        y += 2
        gauge.update(x)
        gauge2.update(y)
        
    while x < 100:
        x += 5
        y -= 5
        gauge.update(x)
        gauge2.update(y)
        
    while x > 0:
        x -= 5
        y += 5
        gauge.update(x)
        gauge2.update(y)