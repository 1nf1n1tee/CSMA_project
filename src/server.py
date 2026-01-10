# src/server.py
from threading import Semaphore
from time import sleep
from client import Client

semaphore = Semaphore(1)

class Server:
    def __init__(self):
        self.users = {}  # registry of clients

    def start(self):
        print("Server started. Commands: create <name>, delete <name>, list, send <sender> <receiver> <message>, quit")
        while True:
            cmd = input(">> ").strip().split()
            if not cmd:
                continue

            action = cmd[0].lower()

            if action == "create" and len(cmd) == 2:
                name = cmd[1]
                if name in self.users:
                    print(f"User {name} already exists.")
                else:
                    self.users[name] = Client(name)
                    print(f"User {name} created.")

            elif action == "delete" and len(cmd) == 2:
                name = cmd[1]
                if name in self.users:
                    del self.users[name]
                    print(f"User {name} deleted.")
                else:
                    print(f"User {name} not found.")

            elif action == "list":
                if self.users:
                    print("Users:", ", ".join(self.users.keys()))
                else:
                    print("No users created yet.")

            elif action == "send" and len(cmd) >= 4:
                sender_name, receiver_name = cmd[1], cmd[2]
                message = " ".join(cmd[3:])
                if sender_name in self.users and receiver_name in self.users:
                    sender = self.users[sender_name]
                    receiver = self.users[receiver_name]
                    t = sender.send(receiver, message)
                    t.join()
                else:
                    print("Both sender and receiver must exist.")

            elif action == "quit":
                print("Shutting down server.")
                break

            else:
                print("Invalid command.")

def send_message(sender, receiver, message):
    for char in message:
        transmit(sender, receiver, char)
        sleep(1)
    receiver.msg_stack.append((sender.name, message))
    print(f"{sender.name} finished sending message to {receiver.name}")
    receiver.receive()

def transmit(sender, receiver, letter):
    with semaphore:
        print(f"{receiver.name} received: {letter} from {sender.name}")
        sleep(1)

if __name__ == "__main__":
    server = Server()
    server.start()