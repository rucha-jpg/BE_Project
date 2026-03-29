# PIR Sensor Testing (Using ZigBee)

## Objective
To test motion detection using a PIR sensor interfaced directly with a ZigBee S2C module and verify wireless transmission of occupancy data.

## Components Used
- ZigBee S2C Module (End Device)
- PIR Sensor
- Jumper Wires

## Connections

| Pin (PIR Sensor) | Connected To                |
|------------------|----------------------------|
| VCC              | 5V                         |
| GND              | GND                        |
| OUT              | Digital Input (DIO1) of ZigBee |

## Working Principle
The PIR sensor detects changes in infrared radiation caused by human movement.

- LOW (0) → No motion detected
- HIGH (1) → Motion detected

The output is directly connected to the ZigBee digital input pin (DIO1).  
The ZigBee module samples this input and transmits the data wirelessly to the coordinator.

## Data Transmission
- No microcontroller code is required
- ZigBee is configured in API mode (with escaping)
- The digital input (DIO1) is periodically sampled
- Data is transmitted as I/O data frames to the coordinator
- Data is verified using XCTU and Raspberry Pi

## Observations
- PIR output successfully toggles between 0 and 1
- Motion detection is accurate and responsive
- Wireless transmission via ZigBee is reliable

## Issues Faced
- A delay of approximately 3 seconds was observed between transitions from LOW (0) to HIGH (1)
- During this delay, new motion events were not detected
- This issue occurred when the PIR sensor was set to Low Trigger Mode

## Solution
- The PIR sensor trigger mode was changed from Low Trigger Mode to High Trigger Mode

## Observations After Fix
- Delay was significantly reduced
- Sensor response became faster and more real-time
- Continuous motion is required to maintain HIGH output
- Overall detection became more precise

## Comparison of Trigger Modes

| Mode              | Behavior                          |
|------------------|----------------------------------|
| Low Trigger Mode | ~3 sec delay, less responsive    |
| High Trigger Mode| Fast response, needs motion      |

## Result
The PIR sensor successfully detects human motion and transmits occupancy data wirelessly through the ZigBee network.  
Switching to High Trigger Mode improved responsiveness and made the system suitable for real-time occupancy detection.
