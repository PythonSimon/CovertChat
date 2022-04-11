# coding=utf-8

from enum import *
from socket import *


host = gethostbyname(gethostname())


@unique
class Command(IntEnum):
    LOGIN = 11
    REGISTER = 12
    SEND = 13


@unique
class LoginResult(IntEnum):
    SUCCESS = 21
    USER_NONE = -22
    PASSWORD_WRONG = -23


@unique
class RegisterResult(IntEnum):
    SUCCESS = 31
    USER_EXIST = -32
    SEND_CODE_FAIL = -33


class Client(object):
    CLIENT_IP = host
    CLIENT_PORT = ""
    CLIENT_ADDRESS = (CLIENT_IP, CLIENT_PORT)
    client = socket(AF_INET, SOCK_DGRAM)
    client.settimeout(5)


class Server(object):
    SERVER_IP = "162.14.67.9"
    SERVER_SERVICE_PORT = "3305"
    SERVER_DAO_PORT = "3306"
    SERVICE_ADDRESS = (SERVER_IP, SERVER_SERVICE_PORT)
    DAO_ADDRESS = (SERVER_IP, SERVER_DAO_PORT)
