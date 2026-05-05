# upskillcampus
AI-Enabled Industrial Environmental Monitoring System | This repository contains an IoT-based edge intelligence solution developed to monitor real-time air quality (AQI) and emissions using the MQTT protocol, featuring automated anomaly detection for industrial safety
# Industrial Internship: IoT & AI Environmental Monitor

## Project Overview
This project was developed during a 6-week Industrial Internship at **UniConverge Technologies Pvt Ltd (UCT)**. It addresses the need for real-time, scalable environmental monitoring in "Smart Factory" environments.

## Key Features
* **Protocol:** Implements MQTT for lightweight, low-bandwidth data transmission.
* **Edge Intelligence:** Includes a Python-based logic engine to detect AQI anomalies in real-time.
* **Data Structure:** Uses JSON payloads for seamless integration with industrial dashboards.

## Hardware & Environment
* **Development Machine:** ASUS Vivobook (i5-12500H, 16GB RAM)
* **Language:** Python 3.x
* **Libraries:** `paho-mqtt`

## How it Works
1. The system simulates sensor data (PM2.5, CO2, Temperature).
2. Data is processed locally to check for safety threshold breaches.
3. Results are published to an MQTT Broker for remote monitoring and alerting.
