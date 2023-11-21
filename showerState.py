import miramode

# This is the BLE address of the device
address = "c1:73:51:1a:08:ec"

# get state
state = miramode.get_state(address)

print(state)

