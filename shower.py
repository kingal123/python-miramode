import miramode
import sys

# This is the BLE address of the device
address = "ce:d7:b8:34:aa:e4"
# See below for how to obtain the device_id and client_id
device_id = 1
client_id = 24829

if len(sys.argv) > 1:
    if sys.argv[1] == '-h':
        print("Run command with no arguments to get current status\nFirst argument is the output 1=1,2=2,3=both\nSecond argument is control 0=OFF,anything else for ON\ne.g python3 shower.py 1 1 # Turn on output 1")
        exit()

device = miramode._connect(address)

try:
    state = miramode.get_state_noc(device)
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
            if state[1]:
                miramode.control_outlets_noc(device, device_id, client_id, False, True, 39)
            else:
                miramode.control_outlets_noc(device, device_id, client_id, False, False, 39)
        else:
            if state[1]:
                miramode.control_outlets_noc(device, device_id, client_id, True, True, 39)
            else:
                miramode.control_outlets_noc(device, device_id, client_id, True, False, 39)
    elif sys.argv[1] == '2':
        if sys.argv[2] == '0':
            if state[0]:
                miramode.control_outlets_noc(device, device_id, client_id, True, False, 39)
            else:
                miramode.control_outlets_noc(device, device_id, client_id, False, False, 39)
        else:
            if state[0]:
                miramode.control_outlets_noc(device, device_id, client_id, True, True, 39)
            else:
                miramode.control_outlets_noc(device, device_id, client_id, False, True, 39)
    elif sys.argv[1] == '3':
        if sys.argv[2] == '0':
            miramode.control_outlets_noc(device, device_id, client_id, False, False, 39)
        else:
            miramode.control_outlets_noc(device, device_id, client_id, True, True, 39)
    else:
        print("Incorrect output", sys.argv[1])
else:
    print("Too many arguments")
