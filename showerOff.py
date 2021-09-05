import miramode

# This is the BLE address of the device
address = "ce:d7:b8:34:aa:e4"
# See below for how to obtain the device_id and client_id
device_id = 4
client_id = 63519

# Turn on the 1st outlet with a 40C degrees water temperature
miramode.control_outlets(address, device_id, client_id, False, False, 39)

