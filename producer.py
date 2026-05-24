import time
import json
import paho.mqtt.client as mqtt

client = mqtt.Client()
client.connect("20.19.224.211", 1883)
client.loop_start()

file_path = "wisdm-dataset/WISDM_ar_v1.1_raw.txt"
WAIT_TIME = 0.2
MAX_LINES = 100000

with open(file_path, "r") as f:
    for i, line in enumerate(f):
        if i >= MAX_LINES:
            break
        try:
            line = line.split(",")
            msg = {
                "usid": line[0],
                "action": line[1],
                "ts": line[2],
                "x": line[3],
                "y": line[4],
                "z": line[5].replace(";", "").replace("\n", "")
            }
            client.publish("smart", json.dumps(msg))
            print(msg)
            time.sleep(WAIT_TIME)
        except Exception as e:
            print(f"Errorea: {e}")
            continue

client.loop_stop()
client.disconnect()