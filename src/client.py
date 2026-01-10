# src/client.py
import sys
from threading import Thread
import server
from time import sleep

class Client:
    def __init__(self, name):
        self.name = name

    def send(self, receiver, message):
        # Create a thread for this sending action
        t = Thread(target=self._send_message, args=(receiver, message))
        t.start()
        return t

    def _send_message(self, receiver, message):
        for char in message:
            server.transmit(self.name, receiver, char)
            sleep(1)
        print(f"{self.name} finished sending message to {receiver}")


if __name__ == "__main__":
    # Expecting 3 arguments: sender, receiver, message
    if len(sys.argv) != 4:
        print("Usage: python client.py <sender> <receiver> <message>")
        sys.exit(1)

    sender = sys.argv[1]
    receiver = sys.argv[2]
    message = sys.argv[3]

    client = Client(sender)
    t = client.send(receiver, message)
    t.join()