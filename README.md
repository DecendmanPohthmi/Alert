# Emergency Alert System

## Overview
The **Emergency Alert System** is a Python-based application designed to send emergency messages with location updates when distress signals are detected. This project integrates **Twilio API** for SMS alerts and **Google Maps API** for geolocation tracking.

## Features
- Detects distress keywords (e.g., "Help me") and triggers an alert.
- Fetches the latest location coordinates.
- Uses Twilio API to send emergency SMS to a predefined contact.
- Reverse geocoding using Google Maps API.
- Displays an interactive map with the location.

## Installation

### Prerequisites
Ensure you have **Python 3.x** installed.

### Install Dependencies
Run the following command to install the required dependencies:
```sh
pip install -r requirements.txt
```

## Configuration
Create a `data.py` file in the project directory and add the following credentials:
```python
TWILIO_ACCOUNT_SID = "your_twilio_account_sid"
TWILIO_AUTH_TOKEN = "your_twilio_auth_token"
TWILIO_PHONE_NUMBER = "your_twilio_phone_number"
EMERGENCY_CONTACT = "your_emergency_contact_number"
API_KEY = "your_google_maps_api_key"
```

**Note:** Do not hardcode API keys in your code. Use environment variables or a `.env` file instead.

## Usage
Run the main script:
```sh
python alert_message.py
```
- Type **"Help me"** to send an emergency alert.
- The system fetches the current location and sends an SMS alert.
- A map with the location is displayed.

Run the alert.py to display the location
```sh
python alert.py
```

If the lat and lng is exist to the loaction.py the file will directly send and link to the browser by clicking on it

If the lat and lng is not exist in the location.py it will ask you to enter the lat and lng

## Troubleshooting
### Authentication Errors (Twilio)
If you get:
```
TwilioRestException: Authentication Error - No credentials provided
```
Make sure `TWILIO_ACCOUNT_SID` and `TWILIO_AUTH_TOKEN` are correctly set in `data.py`.

### Google Maps API Issues
If reverse geocoding fails:
- Verify the API key in `data.py`.
- Ensure that the **Geocoding API** and **Places API** are enabled in your Google Cloud Console.

## License
This project is licensed under the MIT License.

