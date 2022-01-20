from socket import socket, gethostname
from threading import Thread
from server import encoding
import json


class Client:
    def __init__(self, host, port):
        self.port = port
        self.host = host
        self.socket = socket()
        self.socket.connect((self.host, self.port))

    def send_text(self, text):
        self.socket.send(text.encode(encoding))

    def __enter__(self):
        return self
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.socket.close()


class ClientE(Client):
    def __init__(self, host, port):
        super().__init__(host, port)

    def send_command(self, command):
        message = {
            'type': 'command',
            'command': command
        }
        self.send_text(json.dumps(message))

    def send_message(self, message):
        message = {
            'type': 'message',
            'content': message
        }
        self.send_text(json.dumps(message))
