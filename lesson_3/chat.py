import argparse
import socket
import json

ADDRESS = 'localhost'
PORT = 7777
CONNECTIONS = 10


def get_server_socket(addr, port):
    s = socket.socket()
    s.bind((addr, port))
    s.listen(CONNECTIONS)
    return s


def get_client_socket(addr, port):
    s = socket.socket()
    s.connect((addr, port))
    return s


def send_data(recipient, data):
    recipient.send(json.dumps(data).encode('utf-8'))


def get_data(sender):
    return json.loads(sender.recv(1024).decode("utf-8"))


def create_parser():
    parser = argparse.ArgumentParser(
        add_help=False
    )
    parser_group = parser.add_argument_group(title='Parameters')
    # parser_group.add_argument('--help', '-h', action='help', help='Help')

    parser_group.add_argument('-addr', default=ADDRESS, help='IP address')
    parser_group.add_argument('-port', type=int, default=PORT, help='TCP port')
    parser_group.add_argument('-a', default='', help='IP address')
    parser_group.add_argument('-p', type=int, default=PORT, help='TCP port')

    return parser
