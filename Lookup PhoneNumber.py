from time import time
import socket
import phonenumbers
from phonenumbers import timezone, geocoder, carrier
from geopy.geocoders import Nominatim

def get_ip_address():
    # Get local machine's IP address
    host_name = socket.gethostname()
    ip_address = socket.gethostbyname(host_name)
    return ip_address

def validate_phone_number(number, region):
    try:
        phone = phonenumbers.parse(number, region)

        if not phonenumbers.is_valid_number(phone):
            raise ValueError("Invalid phone number.")

        return phone

    except phonenumbers.phonenumberutil.NumberParseException as e:
        raise ValueError(f"Error parsing phone number: {e}")

def get_location(phone):
    geolocator = Nominatim(user_agent="phone_location_app")
    location = geolocator.geocode(geocoder.description_for_number(phone, "en"))

    if location:
        return location.address
    else:
        return "Location information not available."

def get_phone_details():
    number = input("Enter Phone number: ")
    region = input("Enter the region code (e.g., 'US' for United States): ")

    try:
        phone = validate_phone_number(number, region)

        time_zone = timezone.time_zones_for_number(phone)
        car = carrier.name_for_number(phone, "en")
        reg = geocoder.description_for_number(phone, "en")
        location = get_location(phone)

        return phone, time_zone, car, reg, location

    except ValueError as e:
        print(f"Error: {e}")
        return None

if __name__ == "__main__":
    phone_details = get_phone_details()

    if phone_details:
        phone, time_zone, car, reg, location = phone_details
        ip_address = get_ip_address()

        print("Phone:", phone)
        print("Time Zone:", time_zone)
        print("Carrier:", car)
        print("Region:", reg)
        print("Location:", location)
        print("IP Address:", ip_address)

    # Adding a pause at the end
    input("Press Enter to exit...")
