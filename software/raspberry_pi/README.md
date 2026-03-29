Raspberry Pi XBee Project
Setup Instructions:

1. Create virtual environment
  python3 -m venv xbee_env
2. Activate environment
  source ~/xbee_env/bin/activate
3. Install dependencies
  python3 -m pip install -r requirements.txt
4. Run the code to display data from router
  python3 receiver.py
5. Run the code to send the data to AWS Cloud
   python3 send_data.py

   
Notes
Make sure XBee is connected via GPIO/serial
Update port if needed (e.g., /dev/ttyUSB0)
