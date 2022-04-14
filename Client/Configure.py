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
class Status(IntEnum):
    MAIN_USER = 21
    SPECIAL_USER = 22


@unique
class LoginResult(IntEnum):
    SUCCESS = 31
    USER_NONE = -32
    PASSWORD_WRONG = -33
    SERVER = -34


@unique
class RegisterResult(IntEnum):
    SUCCESS = 41
    USER_EXIST = -42
    SEND_CODE_FAIL = -43
    SERVER = -44


@unique
class UserDAOResult(IntEnum):
    SUCCESS = 51
    USER_NONE = -52
    USER_EXIST = -53
    FAIL = -54


class Client(object):
    CLIENT_IP = host
    CLIENT_PORT = ""
    CLIENT_ADDRESS = (CLIENT_IP, CLIENT_PORT)
    client = socket(AF_INET, SOCK_DGRAM)
    client.settimeout(5)


class Server(object):
    SERVER_IP = "162.14.67.9"

    SERVER_SERVICE_PORT = "3305"
    SERVER_SERVICE_ADDRESS = (SERVER_IP, SERVER_SERVICE_PORT)

    SERVER_DAO_PORT = "3306"
    SERVER_DAO_ADDRESS = (SERVER_IP, SERVER_DAO_PORT)
    DAO_USER = "wanghaobo"
    DAO_PASSWORD = "wanghaobo_2009"
    DAO_DATABASE = "CovertChat"
    DAO_CHARSET = "utf8"
