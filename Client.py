#!/usr/bin/env python3

import socket 

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = '!DISCONNECT'
SERVER = "127.0.1.1"
Address = (SERVER, PORT)


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(Address) #connecting to server
isConnected = True

def send(msg):
	message = msg.encode(FORMAT) #Encoded version of msg in utf-8
	message_length = len(message) #Finding size of encoded message

	final_length = str(message_length).encode(FORMAT) #encoding and casting length of message to string
	final_length += b' ' * (HEADER - len(final_length))#padding the length of message to fit 64 bits to be allowed through server
	client.send(final_length) #sending the length of message
	client.send(message) #sending the actual message 

while isConnected:
	print('Enter Message:')
	naked_message = input()
	send(naked_message)

	if naked_message == DISCONNECT_MESSAGE:
		print("\nExiting...")
		isConnected = False


	  