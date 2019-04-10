import socket


class Socket_Obj:
  def __init__(self, Sock=None):
    if Sock is None:
      self.Sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    else:
      self.Sock = Sock

  def Bind(self, host, port):
    self.Sock.bind((host, port))

  def Listen(self, conns=1):
    self.Sock.listen(conns)

  def Accept(self):
    return self.Sock.accept()

  def Connect(self, host, port):
    self.Sock.connect((host, port))

  def Close(self):
    self.Sock.close()

  def GetSockDetails(self):
    return self.Sock

  def RecvMsg(self):
    msg = self.Sock.recv(1024)
    return msg

  def SendMsg(self, msg):
    self.Sock.send(msg)
  




