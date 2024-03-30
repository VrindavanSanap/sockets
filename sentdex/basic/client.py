#!/usr/bin/python3
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "localhost"
port = 1234
s.connect((host, port))
full_msg = ""
while True:
  msg = s.recv(8)
  if len(msg) <= 0:
    break


  full_msg += msg.decode("utf-8")
print(full_msg)

