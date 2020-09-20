#!/usr/bin/env python3

import socket
import threading

Port = 5050
Server = socket.gethostbyname(socket.gethostname()) #using hostname to find local ip
Address = (Server, Port)
HEADER = 64
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(Address) #binding IP and PORT together

def handle_client(conn, addr):
	print(f'New Connection: {addr} ')

	connected = True
	while connected: #while connection is persistent
		message_length = conn.recv(HEADER).decode(FORMAT) #setting recieving messages to 64 bits
		if message_length: #First message is always empty, this is avoiding errors for that message
			message_length = int(message_length) #casting to int format
			message = conn.recv(message_length).decode(FORMAT) #setting length for actual message using message_length

			if message == DISCONNECT_MESSAGE: #if message is !DISCONNECT, close connection with client
				connected = False

			print(f'{addr[0]}: {message}') #print decoded message

	conn.close() #if !DISCONNECT is used
	print(f'\nActive Connections: {threading.activeCount() - 2}')


def start():
	server.listen() #start listening for connections
	print(f'Listening on: {Server}\n')
	while True:
		conn, addr = server.accept() #when client has connected put name and IP of connecting client in variables
		thread = threading.Thread(target=handle_client, args=(conn, addr)) #set a thread for every client connecting
		thread.start() #start threads for clients, move to handle_client
		print(f'Active Connections: {threading.activeCount() - 1}')

print('Server Starting...')
start() #Server start here.



