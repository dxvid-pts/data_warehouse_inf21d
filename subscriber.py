import paho.mqtt.client as mqtt
def on_message(client, userdata, message):

#<JSON Message in DB-Tabelle staging.messung schreiben>

from db import create_table_if_not_exist


def main():
    # Your primary program logic goes here
    print("This is inside the main function")
    create_table_if_not_exist()
    print("This is the end of the main function")

if __name__ == "__main__":
    main()
