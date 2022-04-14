# coding=utf-8

from json import *
from socket import *

from Server.DAO.User import *


def login(email, password, client: tuple, serverSocket: socket):
    server = serverSocket

    user = UserDAO().findUser(email=email)

    if isinstance(user, UserDAOResult):
        resultJ = dumps({
            "result": LoginResult.USER_NONE
        })

        server.sendto(resultJ.encode(), client)
    else:
        if password == user["password"]:
            resultJ = dumps({
                "result": LoginResult.SUCCESS,
                "status": Status.MAIN_USER,
                **user
            })

            server.sendto(resultJ.encode(), client)
        elif password == user["password2"]:
            resultJ = dumps({
                "result": LoginResult.SUCCESS,
                "status": Status.VICE_USER,
                **user
            })

            server.sendto(resultJ.encode(), client)
        else:
            resultJ = dumps({
                "result": LoginResult.PASSWORD_WRONG
            })

            server.sendto(resultJ.encode(), client)
