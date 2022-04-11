# coding=utf-8

from socket import *

from Server.Configure import *


def receiveRegister():
    serverSocket = socket(AF_INET, SOCK_DGRAM)
    serverSocket.bind(Server.SERVICE_ADDRESS)

    while True:
        try:
            data, address = serverSocket.recvfrom(1024)
            
        except Exception:
            pass
