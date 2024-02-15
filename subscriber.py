import paho.mqtt.client as mqtt
def on_message(client, userdata, message):

#<JSON Message in DB-Tabelle staging.messung schreiben>
mqttc = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, "#ID DIFFERENT to subscriber", clean_session=False)
mqttc.on_message = on_message
mqttc.connect("broker.hivemq.com", 1883, 60)
mqttc.subscribe("DataMgmt", qos=1)