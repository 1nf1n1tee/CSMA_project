# src/server.py
from threading import Semaphore
from time import sleep

# Shared semaphore for channel access
semaphore = Semaphore(1)

def send_message(sender, receiver, message):
    for char in message:
        transmit(sender, receiver, char)
        sleep(1)
    # Add message to receiver’s mailbox
    receiver.msg_stack.append((sender.name, message))
    print(f"{sender.name} finished sending message to {receiver.name}")
    receiver.receive()

def transmit(sender, receiver, letter):
    with semaphore:  # ensures only one sender at a time
        print(f"{receiver.name} received: {letter} from {sender.name}")
        sleep(1)