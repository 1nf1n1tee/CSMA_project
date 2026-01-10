# from time import sleep
# from threading import Semaphore, Thread

# # Shared semaphore for all threads
# semaphore = Semaphore(1)

# def sender(person_send, person_rec, msg):
#     for i in msg:
#         transmit(person_send, person_rec, i)
#         sleep(1)
#     print(f"{person_send} finished sending message to {person_rec}")

# def transmit(person_send, person_rec, letter):
#         # semaphore lock
#         semaphore.acquire()
#         receiver(person_send, person_rec, letter)
#         sleep(1)
#         semaphore.release()
#         # semaphore unlock

# def receiver(person_send, person_rec, letter):
#     print(f"{person_rec} received: {letter} from {person_send}")
#     sleep(1)

# if __name__ == "__main__":
#     t1 = Thread(target=sender, args=("Alice", "Bob", "HELLO"))
#     t2 = Thread(target=sender, args=("Charlie", "Dave", "WORLD"))
#     t3 = Thread(target=sender, args=("Eve", "Frank", "PYTHON"))
#     t4 = Thread(target=sender, args=("Grace", "Heidi", "THREADS"))
    
#     t1.start()
#     t2.start()
#     t3.start()
#     t4.start()

#     t1.join()
#     t2.join()
#     t3.join()
#     t4.join()
