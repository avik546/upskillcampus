import paho.mqtt.client as mqtt
import time
import random
import json

# --- CONFIGURATION ---
BROKER = "broker.hivemq.com" # Public industrial test broker
PORT = 1883
TOPIC = "uct/internship/env_monitor"

# --- AI LOGIC (Simple Threshold & Trend Analysis) ---
def detect_anomaly(value, threshold=75.0):
    """
    Simulates a basic AI decision engine.
    In a real scenario, this would be a trained ML model.
    """
    if value > threshold:
        return True, "CRITICAL: High Emission Detected!"
    return False, "Status: Normal"

# --- MQTT SETUP ---
client = mqtt.Client()
client.connect(BROKER, PORT)

print("--- AI-Enabled IoT Monitoring Started ---")

try:
    while True:
        # 1. SIMULATE EMBEDDED SENSOR DATA (PM2.5 and CO2)
        # In real life, this would come from a DHT11 or MQ-135 sensor
        aqi_value = round(random.uniform(20.0, 100.0), 2)
        temp_value = round(random.uniform(25.0, 35.0), 2)
        
        # 2. RUN AI ANOMALY DETECTION
        is_anomaly, message = detect_anomaly(aqi_value)
        
        # 3. PREPARE JSON PAYLOAD (Best practice for Industrial IoT)
        payload = {
            "timestamp": time.ctime(),
            "aqi": aqi_value,
            "temp": temp_value,
            "anomaly": is_anomaly,
            "alert": message
        }
        
        # 4. PUBLISH TO BROKER
        client.publish(TOPIC, json.dumps(payload))
        
        print(f"Sent: AQI {aqi_value} | {message}")
        
        # Frequency: Send data every 5 seconds
        time.sleep(5)

except KeyboardInterrupt:
    print("Monitoring Stopped.")
    client.disconnect()