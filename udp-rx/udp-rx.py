# Receives and displays data from UDP packets
# 
# Example usage:  python udp-rx.py <port, e.g. 5005>
#
# Test in Linux using:  $ nc -u <ip address> <port>
#
# W. Newhall 12/2019

import socket
import argparse

# Get arguments from command line
parser = argparse.ArgumentParser(description='Receive a UDP message.')
parser.add_argument('myport', type=int, help="My port to listen on")
args = parser.parse_args()

UDP_IP = "0.0.0.0"
UDP_PORT = args.myport

print("Creating socket")
sock = socket.socket(socket.AF_INET,    # Internet
                     socket.SOCK_DGRAM) # UDP
print("Socket created")

myhostname = socket.gethostname()
print("My hostname is {}".format(myhostname))
print("My ip is {}".format(socket.gethostbyname(myhostname)))

print("Binding socket to {}:{}".format(UDP_IP, UDP_PORT))
sock.bind((UDP_IP, UDP_PORT))
print("Socket bound")

print("Listening for UDP on {}:{}".format(UDP_IP, UDP_PORT))

while True:
    data, (senderip, senderport) = sock.recvfrom(1024) # buffer size is 1024 bytes
    print("Received UDP from {}:{} {}".format(senderip, senderport, data.decode('utf-8')))

