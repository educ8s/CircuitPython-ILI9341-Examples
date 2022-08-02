import board, busio, displayio
import terminalio #Just a font
import adafruit_ili9341
from adafruit_display_text import label

displayio.release_displays()

mosi_pin = board.GP11
clk_pin = board.GP10
reset_pin = board.GP17
cs_pin = board.GP18
dc_pin = board.GP16

spi = busio.SPI(clock=clk_pin, MOSI=mosi_pin)

display_bus = displayio.FourWire(spi, command=dc_pin, chip_select=cs_pin, reset=reset_pin)

display = adafruit_ili9341.ILI9341(display_bus, width=240, height=320, rotation=270)
splash = displayio.Group()
display.show(splash)

color_bitmap = displayio.Bitmap(240, 320, 1)

color_palette = displayio.Palette(1)
color_palette[0] = 0x00FF00  # Bright Green

bg_sprite = displayio.TileGrid(color_bitmap, pixel_shader=color_palette, x=0, y=0)
splash.append(bg_sprite)

# Draw a smaller inner rectangle
inner_bitmap = displayio.Bitmap(230, 310, 1)
inner_palette = displayio.Palette(1)
inner_palette[0] = 0x000000  # Black
inner_sprite = displayio.TileGrid(inner_bitmap, pixel_shader=inner_palette, x=5, y=5)
splash.append(inner_sprite)

# Draw a label
text_group = displayio.Group(scale=1, x=11, y=24)
text = "Hello World!\n\nThis is a sample\ntext!\n\nEverything is \nworking fine."
text_area = label.Label(terminalio.FONT, text=text, color=0xFFFFFF)
text_group.append(text_area)  # Subgroup for text scaling
splash.append(text_group)