# coding=utf-8

from enum import *


@unique
class Command(IntEnum):
    LOGIN = 11
    SEND = 12

@unique
class Result(IntEnum):
    SUCCESS = 21
    FAIL = -22


class Server(IntEnum):
    # FIXME 待填写
    SERVER_IP = ""
    SERVER_SERVICE_PORT = 0
    SERVER_DAO_PORT = 0
    SERVICE_ADDRESS = (SERVER_IP, SERVER_SERVICE_PORT)
    DAO_ADDRESS = (SERVER_IP, SERVER_DAO_PORT)
