from server import ServerE
from client import ClientE

server_e = ServerE()
server_e.start_async()

with ClientE(server_e.host, server_e.port) as c:
    c.send_command('restart')

with ClientE(server_e.host, server_e.port) as c:
    c.send_message('Hello World')

with ClientE(server_e.host, server_e.port) as c:
    c.send_command('stop')