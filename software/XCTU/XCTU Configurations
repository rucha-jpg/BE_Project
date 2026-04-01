# ZigBee Configuration using XCTU (Implementation)

## Objective
To configure ZigBee S2C modules for transmitting PIR (digital) and MQ (analog) sensor data wirelessly using End Device, Router, and Coordinator.

## Software Used
- XCTU


## Step 1: Device Setup

- Connected each ZigBee module to PC using USB-to-Serial adapter
- Added devices in XCTU using respective COM ports
- Verified communication at baud rate 9600


## Step 2: End Device Configuration (Sensor Node)

Configured ZigBee as End Device to read sensor data directly.

### Network & Mode Settings

| Parameter | Value |
|----------|------|
| PAN ID   | 5354 |
| SC (Scan Channels) | 7FFF |
| CE       | 0    |
| DH       | 0    |
| DL       | FFFF |
| AP       | 2    |

### I/O Configuration

| Parameter | Value | Purpose |
|----------|------|---------|
| D0       | ADC  | MQ Sensor (Analog Input) |
| D1       | Digital Input | PIR Sensor |

### Sampling Configuration

| Parameter | Value | Description |
|----------|------|-------------|
| IR       | 3E8  | Sampling rate (1000 ms) |
| IC       | 2    | Interrupt on D1 (PIR change detection) |

### Implementation Notes

- PIR connected to D1 (digital input)
- MQ sensor connected to D0 (ADC)
- ZigBee directly reads sensor values (no microcontroller used)
- Data is automatically transmitted as I/O sample frames


## Step 3: Router Configuration

Configured ZigBee as Router for data forwarding and Arduino interface.

| Parameter | Value |
|----------|------|
| PAN ID   | 5354 |
| CE       | 0    |
| DH       | 0    |
| DL       | FFFF |
| AP       | 2    |

### Implementation Notes

- Receives data from End Device
- Forwards data to Coordinator
- Connected to Arduino for LED indication


## Step 4: Coordinator Configuration

Configured ZigBee as Coordinator for receiving all network data.

| Parameter | Value |
|----------|------|
| PAN ID   | 5354 |
| CE       | 1    |
| DH       | 0    |
| DL       | FFFF |

### Implementation Notes

- Acts as central node of ZigBee network
- Connected to Raspberry Pi via serial communication
- Receives all sensor data for processing


## Step 5: Data Flow

End Device → Router → Coordinator → Raspberry Pi


## Step 6: Testing and Verification

- Opened XCTU console on Coordinator
- Observed incoming API frames

### Verified Outputs:

- D1 (PIR):
  - 0 → No motion
  - 1 → Motion detected

- D0 (MQ ADC):
  - ~300–350 → Normal air
  - Higher values → Strong odour detected


## Step 7: Issues Faced

- Incorrect readings initially due to misconfigured I/O pins
- ADC values not received until D0 set to ADC
- PIR delay due to Low Trigger Mode (fixed by switching to High Trigger Mode)


## Result

All ZigBee modules were successfully configured with the specified parameters.  
Sensor data was reliably transmitted from End Device to Coordinator via Router, and verified using XCTU console.
