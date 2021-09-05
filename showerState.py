import miramode

# This is the BLE address of the device
address = "ce:d7:b8:34:aa:e4"

# get state
state = miramode.get_state(address)

print(state)

