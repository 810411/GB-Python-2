import sys
import json
from chat import get_client_socket, create_parser, ADDRESS
from jim import PRESENCE, MESSAGE

CLIENT_NAME = 'C0deMaver1ck'
PRESENCE['user']['account_name'] = MESSAGE['from'] = CLIENT_NAME
address = ADDRESS

parser = create_parser()
namespace = parser.parse_args()

s = get_client_socket(address, namespace.port)

serv_addr = s.getpeername()
print(f'Connected to server: {serv_addr[0]}:{serv_addr[1]}')

s.send(json.dumps(PRESENCE).encode('utf-8'))

data = json.loads(s.recv(1024).decode("utf-8"))

if data['response'] in ['200', '400']:
    print(f'{data["time"]} - {data["from"]}: {data["response"]} - {data["alert"]}')

    while True:
        msg = input('Введите сообщение: ')
        MESSAGE['message'] = msg
        s.send(json.dumps(MESSAGE).encode('utf-8'))

        data = json.loads(s.recv(1024).decode("utf-8"))
        if data['response'] != '200':
            break

else:
    print(f'{data["time"]} - {data["from"]}: {data["response"]} - {data["alert"]}')

s.close()

# Сообщение для сервера 'exit' для завершения сеанса чата.
