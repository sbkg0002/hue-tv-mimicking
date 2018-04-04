#!/usr/bin/env python3
##############################
# Requirements:
# * phue: install via `pip install phue`
# * Philips Hue Bridge
# Hue API: https://www.developers.meethue.com/documentation/core-concepts
##############################
from phue import Bridge
import random
from time import sleep
##############################
bridgeIP='192.168.178.33'
mimickLampId=2
##############################
# Connect to bridge
b = Bridge(bridgeIP)

# If running for the first time, press button on bridge and run with b.connect() uncommented
# b.connect()

# Save the state so we can re-set it upon exit
save_state = {
              'on': b.get_light(mimickLampId, 'on'),
              'hue': b.get_light(mimickLampId, 'hue'),
              'bri': b.get_light(mimickLampId, 'bri')
             }

try:
    print ("Starting mimicking, use <Ctrl-C> to stop")
    while True:
        # hue range = 0 - 65280
        # But both max and min are red.
        command =  {
                    'transitiontime': 0,
                    'on': True,
                    'bri': 254,
                    'hue': random.randint(100, 60000)
                   }
        b.set_light(mimickLampId, command)

        # Generate a random sleep interval that is between 0.00001 and 5 seconds.
        sleep(random.randint(1,5) * random.random())
except KeyboardInterrupt:
    # Restore lamp state
    print ("Caught keyboard interruption, restoring state and exitting.")
    b.set_light(mimickLampId, save_state)

    exit()
