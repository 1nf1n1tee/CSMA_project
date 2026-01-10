# src/client.py
import sys
from threading import Thread
import server
from time import sleep

class Client:
    def __init__(self, name):
        self.name = name
        self.msg_stack = []  # mailbox for received messages

    def send(self, receiver, message):
        # Create a thread for this sending action
        t = Thread(target=server.send_message, args=(self, receiver, message))
        t.start()
        return t
    
    def receive(self):
        sender, message = self.msg_stack[-1]  # latest message
        print(f"{self.name} received a new message from {sender}: {message}")
    
    def mail_box(self):
        # mailbox will print from stack top --> latest msg
        for i in range(len(self.msg_stack), 0, -1):
            sender, message = self.msg_stack[i-1]
            print(f"Message {i} from {sender}: {message}")


if __name__ == "__main__":
    # Expecting 3 arguments: sender, receiver, message
    if len(sys.argv) != 4:
        print("Usage: python client.py <sender> <receiver> <message>")
        sys.exit(1)

    sender_name = sys.argv[1]
    receiver_name = sys.argv[2]
    message = sys.argv[3]

    # Create both sender and receiver clients
    sender = Client(sender_name)
    receiver = Client(receiver_name)

    t = sender.send(receiver, message)
    t.join()

    # Show receiver’s mailbox after transmission
    receiver.mail_box()