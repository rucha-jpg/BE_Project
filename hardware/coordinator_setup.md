# XBee Coordinator Setup (Raspberry Pi)

## 📌 Description

This document explains how to connect the XBee Coordinator module to the Raspberry Pi using GPIO (UART) for serial communication.

---

## 🧩 Components Required

* Raspberry Pi (any model with GPIO)
* XBee Module (Coordinator)
* XBee USB Adapter / XBee Breakout Board
* Jumper Wires
* Power Supply

---

## 🔌 GPIO Connections

### XBee → Raspberry Pi

| XBee Pin | Raspberry Pi Pin    | Description         |
| -------- | ------------------- | ------------------- |
| VCC      | 3.3V (Pin 1)        | Power supply        |
| GND      | GND (Pin 6)         | Ground              |
| TX       | RX (GPIO15, Pin 10) | XBee transmits data |
| RX       | TX (GPIO14, Pin 8)  | XBee receives data  |

---

## ⚠️ Important Notes

* Raspberry Pi GPIO works on **3.3V ONLY**
  → Do NOT connect 5V to XBee
* TX and RX are **cross-connected**:

  * XBee TX → Pi RX
  * XBee RX → Pi TX
* Ensure secure connections to avoid data loss

---

## ⚙️ Enable Serial Communication on Raspberry Pi

### 1. Open configuration tool

```
sudo raspi-config
```

### 2. Navigate:

```
Interface Options → Serial Port
```

### 3. Set options:

```
Login shell over serial? → No  
Enable serial port hardware? → Yes  
```

### 4. Reboot system

```
sudo reboot
```

---

## 🔍 Verify Serial Port

After reboot, check:
ls /dev/serial0

Expected output:
/dev/serial0

---

## 🚀 Usage

* Use `/dev/serial0` or `/dev/ttyS0` in your Python code
* Ensure baud rate matches XBee configuration (e.g., 9600)

---

## 🧠 Troubleshooting

### Issue: No data received

* Check TX/RX connections (crossed correctly)
* Verify serial port enabled
* Ensure correct baud rate

### Issue: Permission denied

* Add user to dialout group:
  sudo usermod -a -G dialout $USER
* Reboot after this

---

## 📁 Related Files

* `/software/receiver.py` → receives data from XBee
* `/software/send_data.py` → sends data
