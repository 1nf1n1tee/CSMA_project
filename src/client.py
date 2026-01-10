# src/client.py
import server
from threading import Thread

class Client:
    def __init__(self, name):
        self.name = name
        self.msg_stack = []

    def send(self, receiver, message):
        t = Thread(target=server.send_message, args=(self, receiver, message))
        t.start()
        return t

    def receive(self):
        sender, message = self.msg_stack[-1]
        print(f"{self.name} received a new message from {sender}: {message}")

    def mail_box(self):
        for i in range(len(self.msg_stack), 0, -1):
            sender, message = self.msg_stack[i-1]
            print(f"Message {i} from {sender}: {message}")