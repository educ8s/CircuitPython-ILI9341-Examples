# This script supports the Raspberry Pi Pico board and the Lilygo ESP32-S2 board
# Raspberry Pi Pico: http://educ8s.tv/part/RaspberryPiPico
# ESP32-S2 Board: http://educ8s.tv/part/esp32s2

import adafruit_ili9341
import board, busio, os, displayio
from gauge import Gauge # get the library here: https://github.com/benevpi/Circuit-Python-Gauge

displayio.release_displays()

board_type = os.uname().machine
print(f"Board: {board_type}")

if 'Pico' in board_type:
    mosi_pin, clk_pin, reset_pin, cs_pin, dc_pin = board.GP11, board.GP10, board.GP17, board.GP18, board.GP16
elif 'ESP32-S2' in board_type:
    mosi_pin, clk_pin, reset_pin, cs_pin, dc_pin = board.IO35, board.IO36, board.IO38, board.IO34, board.IO37    
else:
    mosi_pin, clk_pin, reset_pin, cs_pin, dc_pin = board.GP11, board.GP10, board.GP17, board.GP18, board.GP16
    print("This board is not supported. Change the pin definitions above.")
    
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