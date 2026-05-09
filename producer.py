import time
import json
import paho.mqtt.client as mqtt

# MQTT konexioa
client = mqtt.Client()
client.connect("localhost", 1883)

# rootpath 
rootpath = "wisdm-dataset/"
file_path = rootpath + "WISDM_ar_v1.1_raw.txt"

WAIT_TIME = 0.2
MAX_LINES = 100000

i = 0

with open(file_path, "r") as f:

    while True:
        line = f.readline()

        if not line:
            break

        try:
            line = line.split(",")

            # limpieza del dataset WISDM
            if len(line) < 6:
                continue

            msg = {
                "usid": line[0],
                "action": line[1],
                "ts": line[2],
                "x": line[3],
                "y": line[4],
                "z": line[5].replace(";", "").replace("\n", "")
            }

            # MQTT-ra bidali
            client.publish("smart", json.dumps(msg))

            time.sleep(WAIT_TIME)

            i += 1
            if i > MAX_LINES:
                break

        except:
            continue