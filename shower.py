import miramode
import sys

# This is the BLE address of the device
address = "ce:d7:b8:34:aa:e4"
# See below for how to obtain the device_id and client_id
device_id = 4
client_id = 63519

try:
    state = miramode.get_state(address)
except:
    print("Data Exception")
    exit()

if len(sys.argv) == 1:
    print(state)
elif len(sys.argv) == 2 or len(sys.argv) == 0:
    print("Not enough arguments")
elif len(sys.argv) == 3:
    if sys.argv[1] == '1':
        if sys.argv[2] == '0':
            miramode.control_outlets(address, device_id, client_id, False, False, 39)
        else:
            miramode.control_outlets(address, device_id, client_id, True, False, 39)
    elif sys.argv[1] == '2':
        if sys.argv[2] == '0':
            miramode.control_outlets(address, device_id, client_id, False, False, 39)
        else:
            miramode.control_outlets(address, device_id, client_id, False, True, 39)
    else:
        print("Incorrect output", sys.argv[1])
else:
    print("Too many arguments")