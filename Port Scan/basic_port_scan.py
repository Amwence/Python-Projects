#!/bin/python3
# Doesn't really scan anything just kind of creates a connection to a port as like a test. You can use something like Netcat to listen and test this.
import socket


# scans our own computer and port of our choice
HOST = '127.0.0.1'
PORT = int(input( "Which port did you want to scan? 1-65535" \n))


#af_inet is ipv4 and SOCK_STREAM is a port

sox = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

sox.connect((HOST, PORT))


