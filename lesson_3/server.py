import json
from chat import get_server_socket, create_parser, ADDRESS
from jim import RESPONSE

SERVER_OK = ['200', 'OK']
RESPONSE['from'] = 'Server'
address = ADDRESS

parser = create_parser()
namespace = parser.parse_args()

s = get_server_socket(address, namespace.p)

serv_addr = s.getsockname()
print(f'Server started at {serv_addr[0]}:{serv_addr[1]}')

client, cl_addr = s.accept()
print(f'Client connected: {cl_addr[0]}:{cl_addr[1]}')

data = json.loads(client.recv(1024).decode("utf-8"))

if data['action'] == 'presence':
    if data["user"]["account_name"] is None:
        RESPONSE['response'], RESPONSE['alert'] = '401', 'Не авторизован'
        print(f'{data["time"]} - Анонимный пользователь')
    else:
        print(f'{data["time"]} - {data["user"]["account_name"]}: {data["user"]["status"]}')
        RESPONSE['response'], RESPONSE['alert'] = SERVER_OK
    client.send(json.dumps(RESPONSE).encode('utf-8'))

    while True:
        data = json.loads(client.recv(1024).decode("utf-8"))
        if data['action'] == 'msg':
            if data['message'] == 'exit':
                RESPONSE['response'], RESPONSE['alert'] = '404', 'Not found'
                client.send(json.dumps(RESPONSE).encode('utf-8'))
                client.close()
                break

            else:
                print(f'{data["time"]} - {data["from"]}: {data["message"]}')
                RESPONSE['response'], RESPONSE['alert'] = SERVER_OK
            client.send(json.dumps(RESPONSE).encode('utf-8'))

else:
    RESPONSE['response'], RESPONSE['alert'] = '400', 'Неправильный запрос/JSON-объект'
    client.send(json.dumps(RESPONSE).encode('utf-8'))

s.close()
