# Methodology

The proposed system follows a structured approach combining IoT-based sensing, wireless communication, edge processing, machine learning, and cloud integration for occupancy detection and air quality monitoring.

## 1. Data Acquisition

The system uses multiple sensors to collect real-time data:
- PIR Sensor: Detects human presence/motion
- MQ Gas Sensor: Measures air quality
- (Optional) Temperature & Humidity Sensor

Sensors are connected to a ZigBee End Device:
- PIR → Digital Input (DIO1)
- MQ → Analog Input (ADC/DIO0)

## 2. Wireless Communication

Sensor data is transmitted using ZigBee:
- End Device → Router (optional) → Coordinator
- API Mode (with escaping) ensures structured and reliable transmission

## 3. Edge Processing (Raspberry Pi)

The ZigBee Coordinator is connected to a Raspberry Pi via UART.

Raspberry Pi performs:
- Serial data reading
- API frame decoding
- Data filtering and preprocessing

## 4. Occupancy Detection using Machine Learning

A machine learning model is implemented on the Raspberry Pi:
- Inputs: PIR + MQ sensor values
- Output: Occupancy status (Occupied / Vacant)

This improves accuracy by reducing false positives.

## 5. Air Quality Analysis

MQ sensor readings are analyzed using threshold logic:
- Good / Moderate / Poor air quality classification
- Used to indicate cleanliness and ventilation needs

## 6. Cloud Data Storage

The system integrates with AWS cloud services:

- Amazon DynamoDB:
  - Stores structured real-time data (sensor values, occupancy status, timestamps)
  - Enables fast querying and scalability

- Amazon S3:
  - Stores logs, historical datasets, and backup files
  - Useful for analysis and model improvement

## 7. Visualization and Dashboard

A web-based dashboard (WordPress/React) is used:
- Fetches data from cloud (DynamoDB)
- Displays real-time occupancy and air quality
- Shows trends, alerts, and historical graphs

## 8. System Workflow

Sensors → ZigBee Network → Raspberry Pi → ML Processing → AWS Cloud → Dashboard → User

## 9. Testing and Validation

The system is tested in multiple stages:
- Sensor validation
- ZigBee communication testing
- Raspberry Pi data processing
- Cloud data upload verification
- End-to-end system testing

Performance is evaluated based on accuracy, latency, and reliability.
