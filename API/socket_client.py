import socket, pickle, pprint, time

HEADER = 64
PORT = 5050
SERVER = "127.0.0.1"
ADDR = (SERVER, PORT)
INPUT = ['Ss01C6ny1O', 0.7]

start = time.time()

# set up client socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

# create and pickle input data
var_pick = pickle.dumps(INPUT)

# send data to the server
client.send(var_pick)

# receive processed data and print it out
proc_data = client.recv(4096)
data_depic = pickle.loads(proc_data)
pprint.pprint(data_depic)


client.close()

end = time.time()
print('it all tool {0:.2f} seconds'.format(end-start))










# def send(msg):
#     message = msg.encode(FORMAT)
#     msg_length = len(message)
#     send_length = str(msg_length).encode(FORMAT)
#     send_length += b' ' * (HEADER- len(send_length))
#
#     client.send(send_length)
#     client.send(message)
#
#     print(client.recv(2048).decode(FORMAT))

# send("Testing this client")
# input()
# send("Test #2")
# input()

# send(DISCONNECT_MESSAGE)
