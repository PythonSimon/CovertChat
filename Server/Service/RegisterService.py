# coding=utf-8

from random import *

from Server.DAO.User import UserDAO


def register(email, name, password, password2, client, serverSocket):
    uid = "".join([choice("qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM") for _ in range()])
    result = UserDAO().register(
        uid,
        email,
        name,
        password,
        password2,
        [],
        ""
    )
