import socket
import requests

#co ords

university_lat = 51.4659
university_lon = -0.0147


brit_lib_lat = 51.5299
brit_lib_lon = -0.1277

# api
base_url = "https://api.open-meteo.com/v1/forecast"

# Set parameters for each location to fetch current weather data
params_uni = {
    "latitude": university_lat,
    "longitude": university_lon,
    "current_weather": "true"
}

params_lib = {
    "latitude": brit_lib_lat,
    "longitude": brit_lib_lon,
    "current_weather": "true"
}

#weather data for the University
response_uni = requests.get(base_url, params=params_uni)
#weather data for the british Library
response_lib = requests.get(base_url, params=params_lib)

if response_uni.status_code == 200 and response_lib.status_code == 200:
    weather_data_uni = response_uni.json()
    weather_data_lib = response_lib.json()

    temp_uni = weather_data_uni["current_weather"]["temperature"]
    temp_lib = weather_data_lib["current_weather"]["temperature"]

    # Create the message comparing both temperatures
    message = f"University Temp: {temp_uni}°C, British Library Temp: {temp_lib}°C. "
    if temp_uni > temp_lib:
        message += "The University is warmer than the British Library."
    elif temp_uni < temp_lib:
        message += "The British Library is warmer than the University."
    else:
        message += "Both locations have the same temperature."
else:
    message = "Failed to fetch weather data."

# Send the weather data using UDP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('localhost', 65433)
client_socket.sendto(message.encode(), server_address)
print("Weather data sent!")
client_socket.close()
