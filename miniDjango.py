from threading import Thread
from socket import socket, AF_INET, SOCK_STREAM

import logging

from response import http_response, http_error


def _handle_client(client_socket, address, app):
    try:
        req = b''
        recv_size = 4096

        while True:
            data = client_socket.recv(recv_size)
            req += data

            if len(data) < recv_size:
                break

        response = app(req)
        http_res = http_response(response)

        client_socket.sendall(http_res)

    except KeyboardInterrupt:
        raise

    except Exception as e:
        logging.error(str(e))
        error_res = http_error()
        client_socket.sendall(error_res)

    finally:
        client_socket.close()


def start_app(app, port=8000):
    server_socket = socket(family=AF_INET, type=SOCK_STREAM)
    server_socket.bind(('', port))
    server_socket.listen(5)

    try:

        while True:
            client_socket, address = server_socket.accept()
            print('Connection from {0}'.format(address))

            client_thread = Thread(target=_handle_client, args=(client_socket, address, app))
            client_thread.start()

    finally:
        server_socket.close()





