from flask import Flask, jsonify, request
from weather import *
app = Flask(__name__)

@app.route("/weather")
def weather():
    # IP_addr is a placeholder
    lon, lat = get_location(request.remote_addr)
    temperature = weather_info(lon,lat)
    return jsonify({"temperature": f"{temperature}",
                    "coordinates": f"{lon, lat}"})

if __name__ == "__main__":
    app.run(debug=True)