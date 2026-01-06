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