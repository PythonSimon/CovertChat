# coding=utf-8

from json import *
from socket import *
from .LoginService import login
from .RegisterService import register
from .SendService import send
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
                email = command["email"]
                password = command["password"]
                login(email, password, address)
            elif command == Command.REGISTER:
                email = command["email"]
                name = command["name"]
                password = command["password"]
                password2 = command["password2"]
                register(email, name, password, password2, address)
            elif command == Command.SEND:
                pass
        except Exception:
            pass
