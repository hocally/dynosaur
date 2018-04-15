import serial

import time


class Node:
    def __init__(self, velocity, acceleration, previous):
        self.velocity = velocity
        self.acceleration = acceleration
        self.previous = previous
        self.next = None

    def setNext(self, node):
        self.next = node


head = Node(None, None, None)
tail = Node(None, None, head)

ser = serial.Serial('/dev/tty', 9600) # Establish the connection on a specific port

for x in range():
    tail = Node(x, x, tail)
    tail.previous.setNext(tail)

print(tail.velocity)