import paho.mqtt.client as mqtt
import json
import time
import random

fins = ["MS.CARRIAGE444", "FEFFEFEFEFEFE6969"]

mqttc = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, "K$PPfGKnJGaTqcEdPo^BDWQnDk##wgjyaC#7wCNT6^owmJu2sPx^PBM8qvERQCrmuL#iDC*zfm8cCuwVs&yxTbP@rNihE9ctAeY6$CwUom%aZtDA4%FpYikGYfbeC*m4", clean_session=False)
mqttc.connect("broker.hivemq.com", 1883, 60)
print("Connected to broker")

# Publish a message every 2 seconds
while True:
        start_time = time.time()

        currentmillissinceepoch = int(round(time.time() * 1000))

        msg = {
            "fin": random.choice(fins),
            "zeit": currentmillissinceepoch,
            "geschwindigkeit": random.randint(0, 3000),
        }
        mqttc.publish("DataMgmt", json.dumps(msg), qos=1)
        print("Published message: " + str(msg))

        # Calculate the time it took to run the function
        elapsed_time = time.time() - start_time

        # Calculate the sleep time and sleep
        sleep_time = max(0, 2 - elapsed_time)  # Ensure a minimum wait of 2 seconds
        time.sleep(sleep_time)
