from time import sleep
from os import system
from modules import ScanPorts
from colorama import Style,Fore,Back,init

init()


ip = input("[SCAN DE PORTAS] Digite o ip do dispositivo: ")
port_max = input("[APENAS NUMEROS] 'Scannear' ate essa porta: ")
system("cls")
port = ScanPorts.Port(ip,port_max)
port.Start()
print(Style.BRIGHT+Fore.WHITE+"\nFim do Scan de ports")
sleep(0.5)
print("CTRL + C para sair...")

while True:
    continue