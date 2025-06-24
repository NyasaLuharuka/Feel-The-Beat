# Generating Sine wave by MCP4725 DAC with Raspberry Pi

import time

# Import the MCP4725 module.
import math
import board
import busio
import adafruit_mcp4725

i2c = busio.I2C(board.SCL, board.SDA)

# Create a DAC instance.
dac = adafruit_mcp4725.MCP4725(i2c, address=0x60)

while True:

    for i in range(4095, 0, -50):
        dac.raw_value = 1400 + int(1240 * (math.sin(2 * math.pi * i / 4095)))
