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

 I have to update the file organisation before that to make it more production grade. 

The updated file structure will look like this
src/
test/
Readme.md
version_log.md

/---------------------------------------/

#Version 1.12

I want to separate the client side and server side of the program. The haven't done anything like this before so I have to learn it first.
For the server and client side separation the server will handle the multi threading part. The client will be only be able to send and recieve msg. The client will have their own mailbox. 
Mailbox will be a queue data structure.

A user will have the ability to send and recieve msg.
the send should be like main.send()
The actual send function will be in the server.
The server will have most of the code but it will have the power to control the threads.

The server will create a thread for each of the user. The only way I can think of is transforming the entire backend into OOP structured. I have to look if theres any other way to do it though. 


But the OOP structure will be like this ig. 

Class CSMA()
			--> send(reciever, msg) 
					for each letter in msg:
						*will trigger the transmit method*
					
			--> transmit()
						sem lock
				
						transmit
						
						sem unlock
			--> recieve() 
					*print(f"{$user} recieved a msg from {$sender}")
					print("msg")*
Class user(CSMA)
			[[from, msg, time]] a stack structure for all msg

			--> send(self, reciever, msg)

			--> recieve() 
					override with 
					msg.append(0)
			
			--> chk_mailbox() 
					print all items in msg stack
					print(f"recieved at {time} from {form}: {msg}")
			
