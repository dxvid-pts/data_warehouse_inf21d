import paho.mqtt.client as mqtt
import json

from db import create_table_if_not_exist, write_row

create_table_if_not_exist()

def on_message(client, userdata, message):
    print("Received message: " + str(message.payload))
    # Write the message to the database
    write_row(json.loads(message.payload))

mqttc = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, "j@L&DFTofpqqZ2Vkuu3VJT6AxmNU3m7dTt&CVdaomPqdjxncbjhRVms62TQh8QPEtpCZpHndC@%T!JS8Q%g$QoQcD&!tCVe$nv@DpidnU8tTjzpKeP&NqkcymX*i8gJH", clean_session=False)
mqttc.on_message = on_message
mqttc.connect("broker.hivemq.com", 1883, 60)
mqttc.subscribe("DataMgmt", qos=1)

mqttc.loop_forever()
