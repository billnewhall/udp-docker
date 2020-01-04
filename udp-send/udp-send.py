# Sends UPD message every 1 sec
#
# Example usage:  python udp-rx.py <ip adress> <port, e.g. 5005>
#
# Test in Linux by listening using netcat:  $ nc -kluv <port, e.g. 5005>
#
# W. Newhall 12/2019

import socket
import argparse
import time

# Get arguments from command line
parser = argparse.ArgumentParser(description='Sends UDP messages every 1 sec.')
parser.add_argument('destip', type=str, help="Destination IP address")
parser.add_argument('destport', type=int, help="Destination port")
args = parser.parse_args()

UDP_IP = args.destip
UDP_PORT = args.destport
MESSAGE = "Hello World "

print("Creating socket")
sock = socket.socket(socket.AF_INET,     # Internet
                     socket.SOCK_DGRAM)  # UDP

print("Socket created")

myhostname = socket.gethostname()
print("My hostname is {}".format(myhostname))
print("My ip is {}".format(socket.gethostbyname(myhostname)))

print("Sending UDP to {}:{} from {}".format(UDP_IP, UDP_PORT, UDP_IP))

n = 0
while True:
    n = n + 1
    message = MESSAGE + str(n)
    sock.sendto(message.encode('utf-8'), (UDP_IP, UDP_PORT))
    print("Sent UDP to {}:{}  {}{}".format(UDP_IP, UDP_PORT, MESSAGE, n))
    time.sleep(1)

