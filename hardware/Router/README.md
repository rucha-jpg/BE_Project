# Router ZigBee Setup with Arduino and LED Indicator

## Objective
To configure a ZigBee Router with Arduino to indicate occupancy using an LED and forward sensor data to the coordinator (Raspberry Pi).

## Components Used
- ZigBee S2C Module (Router)
- Arduino (Uno)
- LED
- Resistors (22kΩ, 33kΩ)
- Breadboard
- Jumper Wires

---

## ZigBee - Arduino Connections

| ZigBee Pin | Connected To                          | Purpose                                  |
|------------|--------------------------------------|------------------------------------------|
| DOUT (TX)  | Arduino Pin 2 (RX)                   | Receive data from ZigBee                 |
| DIN (RX)   | Arduino Pin 3 (TX via voltage divider)| Send data to ZigBee (safe 3.3V input)    |
| VCC        | 3.3V (from Arduino)                  | Power supply for ZigBee                  |
| GND        | GND (Arduino)                        | Common ground                            |

---

## Voltage Divider Connection (ZigBee Protection)

| Component        | Connection                          | Purpose                      |
|------------------|------------------------------------|------------------------------|
| 22kΩ Resistor    | Between Arduino TX and output node | Reduce voltage               |
| 33kΩ Resistor    | Between output node and GND        | Complete voltage divider     |
| Output Node      | ZigBee DIN (RX)                    | Provides safe 3.3V input     |

---

## LED Indicator Connection

| Component | Connected To     | Purpose                          |
|----------|------------------|----------------------------------|
| LED      | Arduino Pin 13   | Indicates occupancy status       |
| LED GND  | GND              | Completes circuit                |

---

## Working Principle

- PIR sensor detects motion and sends data via ZigBee End Device
- Router ZigBee receives the data wirelessly
- Arduino reads incoming data through serial communication

### LED Behavior:
- Motion detected (HIGH) → LED ON
- No motion (LOW) → LED OFF

- The LED remains ON as long as motion is continuously detected
- Provides real-time visual indication of stall occupancy (Occupied / Vacant)

---

## Data Forwarding

- Arduino processes incoming ZigBee data
- Simultaneously forwards the data to the ZigBee Coordinator
- Coordinator is connected to Raspberry Pi for further processing

---

## Result

The ZigBee Router successfully:
- Receives sensor data wirelessly
- Controls LED indicator based on motion detection
- Forwards data reliably to the coordinator

This setup provides a real-time visual indication of occupancy and ensures seamless data transmission in the ZigBee network.
