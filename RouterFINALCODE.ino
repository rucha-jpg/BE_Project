#include <SoftwareSerial.h>
SoftwareSerial xbee(2, 3);

int ledPin = 13;

byte readByte() {
  while (!xbee.available());

  byte b = xbee.read();

  // 🔥 Handle escape character
  if (b == 0x7D) {
    while (!xbee.available());
    b = xbee.read() ^ 0x20;
  }

  return b;
}

void setup() {
  Serial.begin(9600);
  xbee.begin(9600);
  pinMode(ledPin, OUTPUT);
}

void loop() {

  if (xbee.available()) {

    if (readByte() == 0x7E) {

      int length = (readByte() << 8) | readByte();

      byte frameType = readByte();

      if (frameType != 0x92) return;

      // Skip addresses + metadata
      for (int i = 0; i < 8; i++) readByte();
      readByte(); readByte();   // 16-bit
      readByte();               // options
      readByte();               // samples

      byte digitalMaskMSB = readByte();
      byte digitalMaskLSB = readByte();
      byte analogMask = readByte();

      int pirState = 0;
      int mqValue = 0;

      // DIGITAL (DIO1)
      if (digitalMaskLSB & 0x02) {
        byte dmsb = readByte();
        byte dlsb = readByte();
        pirState = (dlsb & 0x02) >> 1;
      }

      // ANALOG (AD0)
      if (analogMask & 0x01) {
        byte amsb = readByte();
        byte alsb = readByte();
        mqValue = (amsb << 8) | alsb;
      }

      Serial.print("MQ Value: ");
      Serial.println(mqValue);

      Serial.print("PIR: ");
      Serial.println(pirState);

      digitalWrite(ledPin, pirState);
    }
  }
}