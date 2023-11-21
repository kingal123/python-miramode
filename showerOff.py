import miramode

# This is the BLE address of the device
address = "c1:73:51:1a:08:ec"
# See below for how to obtain the device_id and client_id
device_id = 1
client_id = 5559

# Turn on the 1st outlet with a 40C degrees water temperature
miramode.control_outlets(address, device_id, client_id, False, False, 39)

