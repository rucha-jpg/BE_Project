# System Architecture

The proposed system follows a layered architecture integrating sensing, communication, edge processing, cloud storage, and user interface components to achieve real-time occupancy detection and air quality monitoring.

## 1. Sensor Layer

This layer is responsible for collecting environmental and occupancy data:
- PIR Sensor: Detects human presence (motion-based)
- MQ Gas Sensor: Measures air quality levels
- (Optional) Temperature & Humidity Sensor

These sensors are connected to a ZigBee End Device:
- PIR → Digital Input (DIO1)
- MQ → Analog Input (ADC/DIO0)

## 2. Communication Layer

ZigBee protocol is used for wireless data transmission:
- End Device collects sensor data
- Router (optional) extends communication range
- Coordinator receives data

ZigBee operates in API mode (with escaping) for structured and reliable communication.

## 3. Edge Processing Layer

The ZigBee Coordinator is interfaced with a Raspberry Pi via UART.

The Raspberry Pi performs:
- Serial data acquisition
- API frame decoding
- Data preprocessing and filtering

## 4. Intelligence Layer (Machine Learning)

A machine learning model runs on the Raspberry Pi:
- Inputs: PIR + MQ sensor values
- Output: Occupancy status (Occupied / Vacant)

This enhances accuracy and reduces false detection.

## 5. Cloud Layer

The processed data is transmitted to cloud services:

- Amazon DynamoDB:
  - Stores real-time structured data (sensor values, occupancy, timestamps)

- Amazon S3:
  - Stores logs, historical datasets, and backups

This enables scalability and remote access.

## 6. Application Layer

A web-based dashboard (WordPress/React) is used to:
- Display real-time occupancy status
- Show air quality levels
- Provide alerts and historical trends

The dashboard retrieves data from the cloud.

## 7. User Layer

End users access the system via:
- Web browsers
- Mobile devices

They can monitor restroom usage and cleanliness in real time.

## 8. Overall Data Flow

Sensors → ZigBee End Device → Router → Coordinator → Raspberry Pi → ML Processing → AWS Cloud → Dashboard → User
