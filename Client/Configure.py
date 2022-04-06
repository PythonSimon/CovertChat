# coding=utf-8

from enum import *


@unique
class Command(IntEnum):
    LOGIN = 11
    SEND = 12


@unique
class LoginResult(IntEnum):
    SUCCESS = 21
    USER_NONE = -22
    PASSWORD_WRONG = -23


@unique
class RegisterResult(IntEnum):
    SUCCESS = 31
    USER_EXIST = -32


class Server(Enum):
    # FIXME 待填写
    SERVER_IP = ""
    SERVER_SERVICE_PORT = 0
    SERVER_DAO_PORT = 0
    SERVICE_ADDRESS = (SERVER_IP, SERVER_SERVICE_PORT)
    DAO_ADDRESS = (SERVER_IP, SERVER_DAO_PORT)
