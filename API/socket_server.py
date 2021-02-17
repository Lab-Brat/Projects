import socket, pickle, pprint, time
from search_csv import SearchCSV

PORT = 5050
SERVER = "127.0.0.1"
ADDR = (SERVER, PORT)

# setting up server socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)
print("[STARTING] server is starting...")

# server starts listening for a connection
server.listen(1)
print(f"[LISTETING] server is listening on {SERVER}")

# accept conneciton
conn, addr = server.accept()
print(f"[NEW CONNECTION] {addr} connected")

# receive data form client
data = conn.recv(4096)
data_rec = pickle.loads(data)

sku = data_rec[0]
sim = data_rec[1]

# process data
SC = SearchCSV()
data_proc = SC.get(sku, sim)
data_pick = pickle.dumps(data_proc)

# send data back to client
conn.send(data_pick)
print('[COMPLETE] data processed and sent')

conn.close()
print('[CLOSING] server terminated')
