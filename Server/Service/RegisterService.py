# coding=utf-8

from json import *
from random import *

from Server.Configure import *
from Server.DAO.User import UserDAO


def register(email, name, password, password2, client: tuple, serverSocket: socket):
    server = serverSocket

    uid = "".join([choice("1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM") for _ in range(10)])

    result = UserDAO().register(
        uid,
        email,
        name,
        password,
        password2,
        [],
        str(randint(1, 100))
    )

    resultJ = dumps({
            "result": result
    })

    server.sendto(resultJ.encode(), client)
