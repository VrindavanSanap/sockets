#!/usr/bin/python3
import socket
import select

IP = "127.0.0.1"
PORT = 3000

HEADER_LENGTH = 10

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((IP, PORT))
server_socket.listen()
sockets_list = [server_socket]
clients = {}
print(f'Listening for connections on {IP}:{PORT}...')


def decode(message):
    return message.decode('utf-8')


def receive_message(client_socket):
    try:
        message_header = client_socket.recv(HEADER_LENGTH)
        if not len(message_header):
            return False
        message_length = int(decode(message_header))
        return {'header': message_header, 'data': client_socket.recv(message_length)}
    except:
        return False


while True:

    read_sockets, _, exception_sockets = select.select(
        sockets_list, [], sockets_list)

    for notified_socket in read_sockets:
        if notified_socket == server_socket:
            client_socket, client_address = server_socket.accept()
            user = receive_message(client_socket)
            if user is False:
                continue
            sockets_list.append(client_socket)
            clients[client_socket] = user
            print(
                f'Accepted new connection from {client_address}, username: {decode(user["data"])}')
        else:
            message = receive_message(notified_socket)
            if message is False:
                print(
                    f'Closed connection from: {decode(clients[notified_socket]["data"])}')
                sockets_list.remove(notified_socket)
                del clients[notified_socket]
                continue
            user = clients[notified_socket]

            print(
                f'Received message from {decode(user["data"])}: {decode(message["data"])}')
            for client_socket in clients:
                if client_socket != notified_socket:
                    client_socket.send(
                        user['header'] + user['data'] + message['header'] + message['data'])
