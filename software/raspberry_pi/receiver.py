from digi.xbee.devices import XBeeDevice
from digi.xbee.io import IOLine

PORT = "/dev/serial0"
BAUD_RATE = 9600
device = XBeeDevice(PORT, BAUD_RATE)

def io_sample_callback(sample, remote, time):
    try:
        pir = sample.get_digital_value(IOLine.DIO1_AD1)
        mq  = sample.get_analog_value(IOLine.DIO0_AD0)
        pir_label = pir.name if pir is not None else "None"
        print(f"PIR: {pir_label} | MQ: {mq}")
    except Exception as e:
        print("Error:", e)

try:
    device.open()
    print("Listening for IO samples...\n")
    device.add_io_sample_received_callback(io_sample_callback)
    input("Press Enter to exit...\n")
finally:
    if device is not None and device.is_open():
        device.close()
