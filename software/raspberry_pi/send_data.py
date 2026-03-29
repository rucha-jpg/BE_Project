from digi.xbee.devices import XBeeDevice
from digi.xbee.io import IOLine
import paho.mqtt.client as mqtt
import ssl
import json
import time
import threading


PORT = "/dev/serial0"
BAUD_RATE = 9600
device = XBeeDevice(PORT, BAUD_RATE)

ENDPOINT  = "a1j0iuinwazv7l-ats.iot.eu-north-1.amazonaws.com"
PORT_MQTT = 8883
CLIENT_ID = "basicPubSub"       
TOPIC     = "sdk/test/python"   
CERT_PATH = "/home/raspi/Downloads/"

connected = threading.Event()


client = mqtt.Client(client_id=CLIENT_ID)


client.tls_set(
    ca_certs=CERT_PATH + "root-CA.crt",
    certfile=CERT_PATH + "detector.cert.pem",
    keyfile=CERT_PATH + "detector.private.key",
    tls_version=ssl.PROTOCOL_TLSv1_2
)

def on_connect(client, userdata, flags, rc):
    print(f"on_connect called, rc: {rc}")
    if rc == 0:
        print("Connected to AWS IoT\n")
        connected.set()
    else:
        print("Connection failed, code:", rc)

def on_disconnect(client, userdata, rc):
    print(f"Disconnected, rc: {rc}")

def on_publish(client, userdata, mid):
    print(f"Message published, mid: {mid}")

client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_publish = on_publish

def io_sample_callback(sample, remote, timestamp):
    try:
        pir = sample.get_digital_value(IOLine.DIO1_AD1)
        mq  = sample.get_analog_value(IOLine.DIO0_AD0)

        pir_label = pir.name if pir is not None else "None"

        payload = json.dumps({
            "PIR": pir_label,
            "MQ": mq,
            "timestamp": int(time.time())
        })

        print(f"PIR: {pir_label} | MQ: {mq}")
        client.publish(TOPIC, payload, qos=0)

    except Exception as e:
        print("Error:", e)

try:
    print("Connecting to AWS IoT...")
    client.connect(ENDPOINT, PORT_MQTT, keepalive=60)
    client.loop_start()

    print("Waiting for connection...")
    is_connected = connected.wait(timeout=15)
    if not is_connected:
        print("Connection timed out!")
    else:
        device.open()
        print("Listening for IO samples...\n")
        device.add_io_sample_received_callback(io_sample_callback)
        input("Press Enter to exit...\n")

finally:
    if device is not None and device.is_open():
        device.close()
    client.loop_stop()
    client.disconnect()
    print("Disconnected.")
