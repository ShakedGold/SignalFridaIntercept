import socket

HOST, PORT = "localhost", 9999 

def send_to_server(message):
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
      sock.connect((HOST, PORT))
      print("Sending message: {} to server".format(message))
      
      sock.sendall(bytes("Messaged received in Signal: " + str(message) + "\n", "utf-8"))