# src/server.py
from threading import Semaphore
from time import sleep

# Shared semaphore for channel access
semaphore = Semaphore(1)

def transmit(sender, receiver, letter):
    with semaphore:  # ensures only one sender at a time
        print(f"{receiver} received: {letter} from {sender}")
        sleep(1)