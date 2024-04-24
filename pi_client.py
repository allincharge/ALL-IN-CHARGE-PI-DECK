import requests
import json

url = 'http://sending-raspberry-pi:5000/sync-data'
data = {
    "Charges": {
        "XYZ123": {
            "AmbientTemperature": "25C",
            "Current_SoC": "50%",
            "End_SoC": "80%",
            "Initial_SoC": "30%",
            "Plate_Number": "XYZ123",
            "StartTimestamp": "2023-04-01T12:00:00",
            "StopTimestamp": "2023-04-01T12:30:00",
            "currCurrent": "10A",
            "currVoltage": "400V",
            "deliveredEnergy": "5kWh"
        }
    }
}

response = requests.post(url, json=data)
if response.status_code == 200:
    print('Data sent successfully')
else:
    print('Error sending data')
