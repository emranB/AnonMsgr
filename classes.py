import sys, socket
from Crypto.PublicKey import RSA
from Crypto import Random
from Crypto.Cipher import PKCS1_OAEP


'''
Key Pairs
'''
class ClientObj():
  def __init__(self, UserName):
    RandomGen = Random.new().read
    PrivKey = RSA.generate(1024, RandomGen)
    PubKey = PrivKey.publickey()
    self.UserName = UserName
    self.Sock = ''
    self.PrivKey = PrivKey
    self.PubKey = PubKey

  def GetPubKey(self):
    return self.PubKey.export_key().decode()
    
  def GetPrivKey(self):
    return self.PrivKey.export_key().decode()

  def EncryptMsg(self, message):
    Encryptor = PKCS1_OAEP.new(self.PubKey)
    return Encryptor.encrypt(message.encode())

  def DecryptMsg(self, message):
    Decryptor = PKCS1_OAEP.new(self.PrivKey)
    return Decryptor.decrypt(message).decode()










'''
Create frame of messages
  - Type: 2-bits
        Connect         = 00 
        Disconnect      = 01 
        Data            = 10 
        Acknowledgement = 11
  - Length of message: 2-bits
        00 to FF = 255 bytes (max length of message)
  - From: 2 bits
        Server = 00
        Client = 01
  - To: 2 bits
        Server = 00
        Client = 01
  - Data: 0 or more bytes
        (length is counted and specified)
'''
  




