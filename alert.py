import requests
import folium
import webbrowser
from location_data import lat, lng

from data import
API_KEY

def get_place_suggestions(api_key, query):
    if "," in query:
        try:
            lat, lng = map(float, query.split(","))
            reverse_geocode(api_key, lat, lng)
        except ValueError:
            print("Invalid coordinates format. Use 'latitude,longitude'")
        return
    
    url = f"https://maps.gomaps.pro/maps/api/place/autocomplete/json?input={query}&key={api_key}"
    response = requests.get(url)
    data = response.json()

    if data["status"] != "OK":
        print("Error:", data.get("error_message", "Invalid request"))
        return

    places = data["predictions"]

    if not places:
        print("No suggestions found.")
        return

    print("\nSuggested Places:")
    for i, place in enumerate(places):
        print(f"{i+1}. {place['description']}")

    choice = int(input("\nSelect a place (number): ")) - 1
    if choice < 0 or choice >= len(places):
        print("Invalid choice.")
        return

    place_id = places[choice]["place_id"]
    details_url = f"https://maps.gomaps.pro/maps/api/place/details/json?place_id={place_id}&key={api_key}"
    details_response = requests.get(details_url)
    details_data = details_response.json()

    if details_data["status"] != "OK":
        print("Error fetching place details.")
        return

    details = details_data["result"]
    name = details.get("name", "N/A")
    address = details.get("formatted_address", "N/A")
    lat = details["geometry"]["location"]["lat"]
    lng = details["geometry"]["location"]["lng"]

    print("\nPlace Details:")
    print(f"Name: {name}")
    print(f"Address: {address}")
    print(f"Latitude: {lat}")
    print(f"Longitude: {lng}")

    show_map(lat, lng, name)

def reverse_geocode(api_key, lat, lng):
    url = f"https://maps.gomaps.pro/maps/api/geocode/json?latlng={lat},{lng}&key={api_key}"
    response = requests.get(url)
    data = response.json()

    if data["status"] != "OK":
        print("Error fetching reverse geocode data.")
        return

    result = data["results"][0]
    address = result.get("formatted_address", "N/A")

    print("\nReverse Geocode Result:")
    print(f"Address: {address}")
    print(f"Latitude: {lat}")
    print(f"Longitude: {lng}")
    print('http://127.0.0.1:5500/map.html')

    show_map(lat, lng, address)

def show_map(lat, lng, place_name):
    """Generate and display an interactive map using Folium."""
    map_obj = folium.Map(location=[lat, lng], zoom_start=15)
    folium.Marker([lat, lng], popup=place_name, tooltip="Click for details").add_to(map_obj)

    map_filename = "map.html"
    map_obj.save(map_filename)
    webbrowser.open(map_filename)

if __name__ == "__main__":
    if lat == "" or lng == "":
        while True:
            query = input("\nEnter a place name or coordinates (latitude,longitude) to search (or 'exit' to quit): ")
            if query.lower() == "exit":
                break
            get_place_suggestions(API_KEY, query)
    else:
        reverse_geocode(API_KEY, lat, lng)
