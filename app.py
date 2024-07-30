from flask import Flask, jsonify, request
from flask_cors import CORS
from pymongo import MongoClient
import json
import requests
import time
from datetime import datetime, timedelta
import tensorflow as tf
import numpy as np
from sklearn.preprocessing import StandardScaler
import urllib.parse

app = Flask(__name__)
CORS(app)

# Connect to MongoDB
username = urllib.parse.quote_plus("Keshav1910")
password = urllib.parse.quote_plus("Keshav@1910")
cluster = "cluster0.sncmunw.mongodb.net"
client = MongoClient(f'mongodb+srv://{username}:{password}@{cluster}/?retryWrites=true&w=majority&appName=Cluster0')
db = client['flight_status_db']
flights_collection = db['flights']

# OpenSky Network API URL
OPENSKY_API_URL = "https://opensky-network.org/api/states/all"

# Simple delay prediction model
model = tf.keras.Sequential([
    tf.keras.layers.Dense(64, activation='relu', input_shape=(4,)),
    tf.keras.layers.Dense(32, activation='relu'),
    tf.keras.layers.Dense(1)
])
model.compile(optimizer='adam', loss='mse')

scaler = StandardScaler()

def fetch_flight_data():
    response = requests.get(OPENSKY_API_URL)
    if response.status_code == 200:
        data = response.json()
        flights = []
        for state in data['states'][:50]:  # Increased to 50 flights
            flight = {
                "icao24": state[0],
                "callsign": state[1].strip() if state[1] else "N/A",
                "origin_country": state[2],
                "longitude": state[5],
                "latitude": state[6],
                "altitude": state[7],
                "on_ground": state[8],
                "velocity": state[9],
                "true_track": state[10],
                "vertical_rate": state[11],
                "updated": datetime.utcfromtimestamp(state[3]).isoformat(),
                "status": "In Air" if not state[8] else "On Ground"
            }
            flights.append(flight)
        return flights
    return []

def predict_delay(flight):
    features = np.array([[
        flight['velocity'],
        flight['altitude'],
        flight['vertical_rate'],
        flight['true_track']
    ]])
    features_scaled = scaler.fit_transform(features)
    delay = model.predict(features_scaled)
    return float(delay[0][0])

@app.route('/api/flights', methods=['GET'])
def get_flights():
    flights = fetch_flight_data()
    for flight in flights:
        flight['predicted_delay'] = predict_delay(flight)
        flights_collection.update_one({"icao24": flight["icao24"]}, {"$set": flight}, upsert=True)
    return jsonify(flights)

@app.route('/api/update_flight', methods=['POST'])
def update_flight():
    data = request.json
    icao24 = data['icao24']
    new_status = data['status']
    
    flights_collection.update_one(
        {"icao24": icao24},
        {"$set": {"status": new_status}}
    )
    
    return jsonify({"message": "Flight updated successfully"})

@app.route('/api/flight_history', methods=['GET'])
def get_flight_history():
    icao24 = request.args.get('icao24')
    history = list(flights_collection.find({"icao24": icao24}, {'_id': 0}).sort("updated", -1).limit(100))
    return jsonify(history)

if __name__ == '__main__':
    app.run(debug=True)