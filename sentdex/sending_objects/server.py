#!/usr/bin/python3

import socket
import time
import pickle
HEADER_SIZE = 10
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "localhost"
port = 1234
s.bind((host, port))

s.listen(5)

while True:
  clientsocket, address = s.accept()
  print(f"Connection from {address} has been established!")

  while True:
    time.sleep(2)
 
    d = {1: "Hey", 2:"There"}
    msg = pickle.dumps(d)
    msg = bytes(f"{len(msg):<{HEADER_SIZE}}", "utf-8") + msg 
    clientsocket.send(msg)


