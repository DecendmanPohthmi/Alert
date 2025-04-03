import geocoder
from twilio.rest import Client
import requests
import folium
import webbrowser

import os

TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_PHONE_NUMBER = os.getenv("TWILIO_PHONE_NUMBER")
EMERGENCY_CONTACT = os.getenv("EMERGENCY_CONTACT")



def update_location():
    g = geocoder.ip("me")
    lat, lng = g.latlng if g.latlng else (None, None)

    if lat is not None and lng is not None:
        with open("location_data.py", "w") as file:
            file.write(f"lat = {lat}\nlng = {lng}\n")

    return lat, lng

def get_saved_location():
    try:
        from location_data import lat, lng
        return lat, lng
    except ImportError:
        return None, None

def send_alert(lat, lng):
    if lat is None or lng is None:
        print("❌ No valid location found!")
        return

    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    message_body = f"🚨 Emergency Alert!\nLive Location: Latitude={lat}, Longitude={lng}\nUser requested help!"

    client.messages.create(to=EMERGENCY_CONTACT, from_=TWILIO_PHONE_NUMBER, body=message_body)
    print("🚨 Emergency alert sent successfully!")

def main():
    user_input = input("Type 'Help me' to send an emergency alert: ").strip().lower()
    
    if user_input == "help me":
        print("🚨 'Help me' detected! Updating location...")

        update_location()
        lat, lng = get_saved_location()

        print(f"📍 Latest Location: Latitude={lat}, Longitude={lng}")
        send_alert(lat, lng)
    else:
        print("✅ No emergency detected.")

if __name__ == "__main__":
    main()
