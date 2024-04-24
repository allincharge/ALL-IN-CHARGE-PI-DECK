# ALL-IN-CHARGE-PI-DECK

Welcome to the ALL-IN-CHARGE PI DECK repository! This project is designed to facilitate the monitoring and management of electric vehicle charging stations via a Raspberry Pi. Our solution provides real-time data collection and control functionalities, making it ideal for small to large EV charging infrastructure.

## Features

- **Real-Time Monitoring**: Track the status and performance of multiple charging stations.
- **Data Collection**: Gather data such as ambient temperature, state of charge (SoC), current, voltage, and energy delivered.
- **User-Friendly Interface**: Manage your charging stations through a simple and intuitive web interface.
- **High Compatibility**: Designed to work seamlessly with Raspberry Pi devices, ensuring easy deployment and maintenance.

## Installation

To get started with the ALL-IN-CHARGE PI DECK, follow these steps to install the necessary software on your Raspberry Pi. The installation process assumes you have Python installed on your Raspberry Pi. If not, please install Python and pip first.

### Step 1: Clone the Repository

First, clone the repository to your Raspberry Pi:

```bash
git clone https://github.com/allincharge/ALL-IN-CHARGE-PI-DECK.git
cd ALL-IN-CHARGE-PI-DECK
```

### Step 2: Install Required Python Packages

Install the required Python packages using pip:

```bash
pip install -r requirements.txt
```

### Step 3: Run the Application
After installing the dependencies, you can start the application by running:

```bash
python aicpideck.py
```

### Usage
Once the application is running, you can access the web interface by navigating to http://localhost:5000 on a web browser. This address might differ based on your setup and configuration, so adjust it accordingly.


## API Endpoints

The ALL-IN-CHARGE PI DECK provides several endpoints to manage and track electric vehicle charging data. Below are the key endpoints available:

### 1. `/verify-vin` - Verify Vehicle Identification Number (VIN)
This endpoint verifies the VIN of a vehicle to ensure it is registered in the system before data submission.

**Method:** POST  
**Data Requirements:** JSON object containing the VIN.  
**Example:**
```json
  {
    "VINnumber": "VIN12345678901234"
  }
```

### 2. /add-data - Add Charging Data
Submit charging data for a specific vehicle. This data includes various parameters like ambient temperature, charge levels, and energy delivered.

**Method:** POST  
**Data Requirements:** JSON object as described below.  
**Example:**
```json
  {
    "VINnumber": "VIN12345678901234",
    "plateNumber": "PLATE1234"
  }
```

### 3. /sync-data - Synchronize Data
This endpoint is used to synchronize or update charging data in bulk or after offline data collection.

**Method:** POST  
**Data Requirements:** JSON object as described below.  
**Example:**
```json
{
    "Charges": {
        "96ADFG898": {
            "AmbientTemperature": "25°C",
            "Current_SoC": "50%",
            "End_SoC": "80%",
            "Initial_SoC": "30%",
            "Plate_Number": "96ADFG898",
            "StartTimestamp": "2023-04-01T12:00:00",
            "StopTimestamp": "2023-04-01T12:30:00",
            "currCurrent": "10A",
            "currVoltage": "400V",
            "deliveredEnergy": "5kWh"
        }
    }
}

```
