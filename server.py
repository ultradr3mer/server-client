from socket import socket, gethostname
from threading import Thread
import json

encoding = 'utf-8'


class Server:
    def __init__(self, port):
        self.host = gethostname()
        self.port = port
        self.socket = socket()
        self.socket.bind((self.host, port))
        self._stop = False
        self._running = False

    def start_async(self):
        server_thread = Thread(target=self._start, args=())
        server_thread.start()

    def _start(self):
        self.socket.listen(5)
        self._running = True
        while not self._stop:
            self._print(f'listening on port {self.port}')
            try:
                accept_socket, addr = self.socket.accept()
                self._run(accept_socket)
                accept_socket.close()
            # tritt offenbar auf wenn der socket aus einem anderen
            # thread geschlossen wird
            except OSError:
                self._stop = True
                continue

        self._print(f'server stoped')
        self._running = False

    def _run(self, socket):
        pass

    def _print(self, message):
        print('[server] ', message)

    def stop(self):
        self.socket.close()
        self._stop = True


class ServerA(Server):
    def __init__(self):
        super().__init__(5000)

    def _run(self, socket):
        c_data = socket.recv(1024)
        self._print('Message: ' + c_data.decode(encoding))

class ServerE(Server):
    def __init__(self):
        super().__init__(6000)

    def _run(self, socket):
        c_data = socket.recv(1024)
        data = json.loads(c_data.decode(encoding))
        if data['type'] == 'command':
            if data['command'] == 'stop':
                self._stop = True
                return
            if data['command'] == 'restart':
                self._restart_dummy()
                return
        if data['type'] == 'message':
            self._print(data['content'])

    def _restart_dummy(self):
        self._print('System: Starte neu .... Fertig')