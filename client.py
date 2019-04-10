import socket, sys, json
from classes import * 


JOINED_SERVER = False
host = '192.168.56.1'
# host = socket.gethostname() 
port = 1111
BUFFER_SIZE = 2000 
Client = {}



'''
Close Client application
'''
def CloseClient(dummy=False):
  print("Closing client... \n")
  sys.exit(0)


'''
Join server by providing username, IP, port, and public key
'''
def JoinServer(username=False):
  if username is False or username == '':
    print("[!] Error! Invalid username!\n ")
    return
  
  # Establish connection with server
  global Client
  Client = ClientObj(username)
  Client.Sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  Client.Sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
  Client.Sock.connect((host, port))

  # Send request to server to CONNECT
  Message = {
    "From": Client.Sock.getsockname(), 
    "To": ("Server", port),
    "MsgType": "CONNECT", 
    "data": ""
  }
  Message = json.dumps(Message)
  print(Client.EncryptMsg(Message))
  Client.Sock.send(Message)     

  # Response from server
  Response = Client.Sock.recv(BUFFER_SIZE).decode('utf-8')
  print (" Received data:", Response)
  if Response == 'ok':
    print("[*] Joined server successfully!\n ")
    global JOINED_SERVER
    JOINED_SERVER = True
  else:
    Client.Sock.close()



ARGS_TBL = {
  'exit': CloseClient,
  'join': JoinServer
}



'''
Join the server by providing username and public key
- Ask user to commands
    - If command exists in function table
        - Run Command
    - Else
        - Print "Invalid command"
'''
while JOINED_SERVER != True:
  Message = input("Enter '<join> <username>' to join the server\n-> ")
  Args = Message.split(" ")
  if Args[0] in ARGS_TBL:
    if len(Args) == 1:
      ARGS_TBL[Args[0]]()
    elif len(Args) == 2:
      ARGS_TBL[Args[0]](Args[1])
    else:
      print("[!] Too many arguments\n")
  else:
    print("[!] Invalid command!\n")


'''
Messaging interface
'''
Message = input("Enter message: ")
while Message != 'exit':
  Client.Sock.send(Message.encode('utf-8'))     
  Response = Client.Sock.recv(BUFFER_SIZE).decode('utf-8')
  print (" Received data:", Response)
  Message = input("Enter message: ")

Client.Sock.close()