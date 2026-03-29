# Raspberry Pi XBee Project Setup Instructions

## 1. Create Virtual Environment

```bash
python3 -m venv xbee_env
```

## 2. Activate Environment

```bash
source ~/xbee_env/bin/activate
```

## 3. Install Dependencies

```bash
python3 -m pip install -r requirements.txt
```

## 4. Run Receiver (Display Data from Router)

```bash
python3 receiver.py
```

## 5. Send Data to AWS Cloud

```bash
python3 send_data.py
```

## Notes

* Make sure XBee is connected via GPIO/serial
* Update port if needed (e.g., /dev/ttyUSB0)

