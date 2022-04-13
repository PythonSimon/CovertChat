# coding=utf-8

from json import *
from socket import *

from Client.Configure import *


def login(email, password):
    client = Client.client

    requestJ = dumps({
        "command": Command.LOGIN,
        "email": email,
        "password": password
    })

    client.sendto(requestJ.encode(), Server.SERVER_SERVICE_ADDRESS)
