#!/usr/bin/python3
import socket
import select
import errno
import sys
HEADER_LENGTH = 10


def decode(message): return message.decode('utf-8')
def encode(message): return message.encode('utf-8')
def get_header(message): return encode(f"{len(message):<{HEADER_LENGTH}}")
def apply_header(message): return get_header(message) + encode(message)


IP = "127.0.0.1"
PORT = 3000
my_username = input("Username: ")

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((IP, PORT))
client_socket.setblocking(False)
username = my_username
client_socket.send(apply_header(username))


while True:

    message = input(f'{my_username} > ')
    if message:
        client_socket.send(apply_header(message))
    try:
        while True:
            username_header = client_socket.recv(HEADER_LENGTH)
            if not len(username_header):
                print('Connection closed by the server')
                sys.exit()
            username_length = int(decode(username_header))
            username = decode(client_socket.recv(username_length))
            message_header = client_socket.recv(HEADER_LENGTH)
            message_length = int(decode(message_header))
            message = decode(client_socket.recv(message_length))
            print(f'{username} > {message}')

    except IOError as e:
        if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
            print(f'Reading error: {str(e)}')
            sys.exit()
        continue
    except Exception as e:
        print(f'Reading error: {str(e)}')
        sys.exit()
