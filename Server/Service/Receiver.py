# coding=utf-8

from json import *
from socket import *
from .LoginService import *
from .RegisterService import *
from .SendService import *
from Server.Configure import *


def receiveRegister():
    serverSocket = socket(AF_INET, SOCK_DGRAM)
    serverSocket.bind(Server.SERVICE_ADDRESS)

    while True:
        try:
            data, address = serverSocket.recvfrom(1024)
            data = loads(data.decode())
            command = data["command"]

            if command == Command.LOGIN:
                pass
            elif command == Command.REGISTER:
                pass
            elif command == Command.SEND:
                pass
        except Exception:
            pass
