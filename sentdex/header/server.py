#!/usr/bin/python3

import socket
import time

HEADER_SIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "localhost"
port = 3000 
s.bind((host, port))

s.listen(5)

while True:
  clientsocket, address = s.accept()
  print(f"Connection from {address} has been established!")

  msg = "Welcome to the server!!"
  msg = f"{len(msg):<{HEADER_SIZE}}" + msg 
  print(msg)
  clientsocket.send(bytes(msg, "utf-8"))
  while True:
    time.sleep(2)
    msg = f"The time is {time.time()}"
    msg = f"{len(msg):<{HEADER_SIZE}}" + msg 
    clientsocket.send(bytes(msg ,"utf-8"))

