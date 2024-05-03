import requests
import json

# Server URLs
VERIFY_URL = 'http://192.168.1.117:5000/verify-vin'
DATA_URL = 'http://192.168.1.117:5000/add-data'
SYNC_URL = 'http://192.168.1.117:5000/sync-data'

def check_vin(VIN_number):
    """
    Check if the provided VIN number exists in the database.
    Returns True if the VIN number exists, False otherwise.
    """
    data = {
        'VINnumber': VIN_number
    }

    try:
        response = requests.post(VERIFY_URL, json=data)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return response.json()

def insert_data(VIN_number, plate_number):
    """
    Insert the provided VIN number and plate number into the database.
    Returns True on success, False on failure.
    """
    data = {
        'VINnumber': VIN_number,
        'plateNumber': plate_number
    }

    try:
        response = requests.post(DATA_URL, json=data)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return response.json()

def sync_data(data):
    """
    Insert the provided VIN number and plate number into the database.
    Returns True on success, False on failure.
    """

    try:
        response = requests.post(SYNC_URL, json=data)
        response.raise_for_status()
        return True
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return False

if __name__ == '__main__':
    VIN_number = '9259587890abcde5'
    plate_number = 'ABC123'
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

    result = sync_data(data)
    print(f"Server response: {result}")
