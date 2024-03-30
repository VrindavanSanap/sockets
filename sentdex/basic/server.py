#!/usr/bin/python3

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "localhost"
port = 1234
s.bind((host, port))

s.listen(5)

while True:
  clientsocket, address = s.accept()
  print(f"Connection from {address} has been established!")
  clientsocket.send(bytes("Welcome to the server", "utf-8"))
  clientsocket.close()
