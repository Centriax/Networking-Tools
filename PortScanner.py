#!/usr/bin/env python3

import socket
import threading
from queue import Queue
import sys


Target = input('Target IP: ')
queue = Queue()
open_ports = []

def portscan(Port):
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((Target, Port))
		return True
	except:
		return False

def worker():
 	while not queue.empty():
 		port = queue.get()
 		if portscan(port):
 			print(f'Port {port}: Open')
 			open_ports.append(port)


def fill_queue(port_list):
	for port in port_list:
		queue.put(port)

try:
	port_start_range = int(input('Starting Port Range (Default: 0): '))
except ValueError:
	port_start_range = 0

try:
	port_end_range = int(input('Ending port Range (Default: 65535): '))
except ValueError:
	port_end_range = 65536


print('\nScanning Ports...\n')


port_list = range(port_start_range, port_end_range)
fill_queue(port_list)

thread_list = []

for t in range(100):
	thread = threading.Thread(target=worker)
	thread_list.append(thread)

for thread in thread_list:
	thread.start()

for thread in thread_list:
	thread.join()

print('\nOpen Ports: ')

if not bool(open_ports):
	print('None\n')
	sys.exit()



for i in range(len(open_ports)):

		print(open_ports[i], end='')
		print(', ', end='')

print('\n')




