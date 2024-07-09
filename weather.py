import requests as req
from flask import request
from flask import jsonify

def get_location(ip_addr):
    response = req.get(f"http://ip-api.com/json/{ip_addr}")
    lat = response.json()["lat"]
    lon = response.json()["lon"]
    print(lat)
    print(lon)
    return lon, lat


def weather_info(lon,lat):
    response = req.get(f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&hourly=temperature_2m&timezone=auto")
    temperature = response.json()
    return (temperature["hourly"]["temperature_2m"][-1])


if __name__ == "__main__":
    #ip_addr = request.remote_addr
    lon, lat = get_location("76.38.52.145")
    weather_info(lon,lat)