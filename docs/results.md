# Results

The developed system was successfully implemented and tested for real-time occupancy detection and air quality monitoring using IoT and machine learning.

## 1. Sensor Testing Results

- PIR Sensor:
  - Output = 0 (No motion)
  - Output = 1 (Motion detected)
  - Successfully detected human presence

- MQ Gas Sensor:
  - Stable readings obtained after warm-up
  - Average baseline value: ~300–350
  - Higher values observed in poor air conditions

## 2. ZigBee Communication Results

- Successful wireless transmission of sensor data
- Data verified using XCTU console at coordinator
- No significant packet loss observed
- API mode ensured structured data reception

## 3. Raspberry Pi Processing

- Successfully received data via UART
- Correct decoding of API frames
- Real-time sensor values displayed:
  - PIR: 0/1
  - MQ: Analog values

## 4. Occupancy Detection Results

- System accurately detected occupancy using:
  - PIR sensor
  - ML model (combined logic)

- Reduced false positives compared to PIR-only system
- Example:
  - Door closed + no motion → Vacant (Correct)
  - Motion detected → Occupied

## 5. Air Quality Monitoring Results

- Air quality classified based on MQ sensor:
  - Good: Low values
  - Moderate: Medium values
  - Poor: High values

- System successfully identified poor ventilation conditions

## 6. Cloud Integration Results

- Data successfully uploaded to AWS:
  - DynamoDB: Real-time data storage
  - S3: Logs and backup storage

- Verified data retrieval from cloud

## 7. Dashboard Output

- Real-time display of:
  - Occupancy status
  - Air quality levels

- Dashboard updated dynamically with incoming data

## 8. Overall System Performance

- Real-time response achieved
- Reliable wireless communication
- Improved accuracy using ML
- Scalable architecture with cloud integration
