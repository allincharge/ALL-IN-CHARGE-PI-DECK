import requests

# Server URL
BASE_URL = "https://fastapi.softvader.online"

# API Key
API_KEY = "YOUR_API_KEY"  # Use the correct API key that matches the server

# Data to be sent
data_to_send = {
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

def test_post_charges():
    """ Function to send data to the server using POST request """
    headers = {'x-api-key': API_KEY, 'Content-Type': 'application/json'}
    response = requests.post(f"{BASE_URL}/data", headers=headers, json=data_to_send)
    print("Response from server:", response.status_code, response.text)

def post_data(data):
    """ Function to send data to the server using POST request """
    headers = {'x-api-key': API_KEY, 'Content-Type': 'application/json'}
    response = requests.post(f"{BASE_URL}/data", headers=headers, json=data)
    print("Response from server:", response.status_code, response.text)

if __name__ == "__main__":
    test_post_charges()
