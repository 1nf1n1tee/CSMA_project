Version 1
CSMA/CD simulation

--> requires multithreading and process synchronisation
/---------------------------------------/

## A sender function
A sender function will take a string as an input. This is send each letter through the transmission channel to the reciever. 

def sender(msg):
	for i in msg:
		transmit letter
	print(f"{msg}  has been sent")
	
/---------------------------------------/

## A trasnmission function
this function will act as the channel the data is passing through. 

def transmission(letter):
	semaphore lock
		send to reciever
	semaphore unlock
	
/---------------------------------------/

## A reciever function
A reciever function will print what it has recieved.

def reciever(letter):
	print(f"Revieved {letter}")
	
/---------------------------------------/

#Version 1.1

I want to separate the client side and server side of the program. The haven't done anything like this before so I have to learn it first. I also have to update the file organisation before that to make it more production grade. 

The updated file structure will look like this
src/
test/
Readme.md
version_log.md

For the server and client side separation the server will handle the multi threading part. The client will be only be able to send and recieve msg. The client will have their own mailbox. 
Mailbox will be a queue data structure.

