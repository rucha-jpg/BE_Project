# MQ Sensor Testing (Using ZigBee)

## Objective
To measure air quality using an MQ gas sensor interfaced directly with a ZigBee S2C module and verify wireless transmission of analog data.

## Components Used
- ZigBee S2C Module (End Device)
- MQ Gas Sensor (Flying Fish type)
- Jumper Wires

## Connections

| Pin (MQ Sensor) | Connected To                |
|-----------------|----------------------------|
| VCC             | 5V                         |
| GND             | GND                        |
| AOUT            | Analog Input (DIO0/ADC) of ZigBee |

## Working Principle
The MQ sensor detects the presence of gases in the environment and outputs an analog voltage proportional to gas concentration.

- Low value → Clean air
- High value → Presence of gas / poor air quality

The analog output is connected to the ZigBee analog input pin (DIO0 configured as ADC).

## Data Transmission
- No microcontroller code is required
- ZigBee is configured in API mode (with escaping)
- Analog input (DIO0) is periodically sampled
- Data is transmitted as I/O data frames to the coordinator
- Values are received and decoded using XCTU and Raspberry Pi

## Observations
- Initial readings were unstable
- After warm-up (~2–3 minutes), readings stabilized
- Typical baseline values: ~300–350
- Values increase significantly in presence of strong odour or gases
- Real-time changes observed with environmental variation

## Issues Faced
- Sensor requires warm-up time before giving stable readings
- Minor fluctuations in readings due to environmental noise

## Observations After Stabilization
- Consistent analog readings obtained
- Noticeable spikes when strong odours are present
- Accurate representation of air quality levels

## Result
The MQ sensor successfully measures air quality and transmits analog data wirelessly through the ZigBee network.  
The system effectively detects changes in gas concentration, making it suitable for real-time air quality monitoring.
