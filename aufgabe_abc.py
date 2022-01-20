from server import ServerA
from client import Client

server_a = ServerA()
server_a.start_async()

with Client(server_a.host, server_a.port) as c:
    c.send_text('hello server! ')
    c.send_text('jet another message! ')

with Client(server_a.host, server_a.port) as c:
    c.send_text('Even more messages.')
    c.send_text('jet another message! ')

server_a.stop()