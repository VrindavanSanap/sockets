#!/usr/bin/python3
import socket
import pickle

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "localhost"
port = 1234
s.connect((host, port))
HEADER_SIZE = 10
while True:
    full_msg = b""
    new_msg = True
    while True:
        msg = s.recv(8)
        if new_msg:
            msg_len = int(msg[:HEADER_SIZE])
            print(f"New msg len:{msg_len}")
            new_msg = False

        full_msg += msg
        if len(full_msg) - HEADER_SIZE == msg_len:
            print("full msg rcvd")
            d = pickle.loads(full_msg[HEADER_SIZE:])
            print(d)
            full_msg = b""
            new_msg = True
