import paho.mqtt.client as mqtt

mqttc = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, " #COMPLEX unique ID ", clean_session=False)
mqttc.connect("broker.hivemq.com", 1883, 60)
mqttc.publish("DataMgmt", <JSON>, qos=1)