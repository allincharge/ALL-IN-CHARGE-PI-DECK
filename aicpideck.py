from flask import Flask, request, jsonify
from deck_helper import post_data
import sqlite3

app = Flask(__name__)

DB_FILE = 'vehicle.db'

def create_database():
    """
    Create the SQLite3 database if it doesn't already exist.
    """
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS vehicles
                 (VINnumber TEXT, plateNumber TEXT)''')
    conn.commit()
    conn.close()

def insert_data(VINnumber, plateNumber):
    """ Insert the provided VIN number and plate number into the database.
    Returns a tuple (True, dict) on success, and (False, None) on failure.
    """
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    try:
        c.execute("INSERT INTO vehicles (VINnumber, plateNumber) VALUES (?, ?)", (VINnumber, plateNumber))
        conn.commit()
        result = {'VINnumber': VINnumber, 'plateNumber': plateNumber}
        conn.close()
        return True, result
    except sqlite3.Error:
        conn.close()
        return False, None
    
def check_vin(VINnumber):
    """
    Check if the provided VIN number exists in the database.
    Returns True if the VIN number exists, False otherwise.
    """
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("SELECT * FROM vehicles WHERE VINnumber = ?", (VINnumber,))
    result = c.fetchone()
    conn.close()
    return bool(result)

def check_vin_get_plate(VINnumber):
    """ Check if the provided VIN number exists in the database.
    Returns the plate number if the VIN number exists, an empty string otherwise.
    """
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("SELECT plateNumber FROM vehicles WHERE VINnumber = ?", (VINnumber,))
    result = c.fetchone()
    conn.close()
    if result:
        return result[0]  # Return the plate number
    else:
        return ''  # Return an empty string

@app.route('/add-data', methods=['POST'])
def add_data():
    """ Endpoint to add the provided VIN number and plate number to the database.
    Returns a JSON response with the 'status' field set to True or False, and the added data if successful.
    """
    data = request.get_json()
    VINnumber = data['VINnumber']
    plateNumber = data['plateNumber']
    success, result = insert_data(VINnumber, plateNumber)
    if success:
        return jsonify({'status': True, 'data': result}), 202
    else:
        return jsonify({'status': False}), 500
    
@app.route('/verify-vin', methods=['POST'])
def verify_vin():
    """ Endpoint to verify the provided VIN number.
    Returns the plate number and status if the VIN exists in the database,
    or a 'Not Found' message otherwise.
    """
    data = request.get_json()
    VINnumber = data['VINnumber']
    plate_number = check_vin_get_plate(VINnumber)
    if plate_number:
        return jsonify({'status': True, 'plateNumber': plate_number}), 202
    else:
        return jsonify({'status': False, 'plateNumber': 'Not Found'}), 500
    
@app.route('/sync-data', methods=['POST'])
def receive_data():
    """
    Endpoint to sync data.
    Returns a JSON response with the 'status' field set to 'success'.
    """

    data = request.get_json()
    # Process the received JSON data
    post_data(data)
    print(data)
    return jsonify({'status': 'success'})

if __name__ == '__main__':
    create_database()
    app.run(debug=True, host='0.0.0.0', port=5000)
