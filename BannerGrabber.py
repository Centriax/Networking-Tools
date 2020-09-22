#!/usr/bin/env python3

import socket

try:
	def main():
		IP = input("Target IP: ")
		PORT = str(input("Target Port: "))
		banner(IP, PORT)

	def banner(IP, PORT):
		s = socket.socket()
		s.connect((IP, int(PORT)))
		print(s.recv(1024))
	main()

except KeyboardInterrupt:
	print('\nQuitting...')

except ConnectionRefusedError:
	print('\nTarget is not responding.')

