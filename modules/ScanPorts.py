import socket
import threading
from os import system
from colorama import Style,Fore,Back,init


init()
class Port():

    def __init__(self,ip,port_max):
        self.ip = ip
        self.service = "None"

        if int(port_max) > 65536:
            self.port_max = 65536+1
        else:
            self.port_max = int(port_max)+1

    def Scan(self,id):
        sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        sock.settimeout(0.004)
        content = sock.connect_ex((self.ip,id))
       
        if content == 0:
            try:
                self.service = socket.getservbyport(id)
            except:
                self.service = "" 
            print(Style.BRIGHT+Fore.GREEN+f"Port open: {id} {self.service}")
        '''else:
            print(Style.BRIGHT+Fore.RED+f"Port NOT open: {id}")'''

    def Start(self):
        for i in range(0,self.port_max):
            self.Scan(i)
        return

