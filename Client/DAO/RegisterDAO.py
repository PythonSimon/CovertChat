# coding=utf-8

from pymysql import *
from pymysql.err import *

CONNECTION_fAILED = -1
CREATE_FAILED = -2


def register(email, name, password, password2):
    try:
        connection = connect(
            host="",
            user="",
            password="",
            database="CovertChat",
            charset="utf8"
        )

        try:
            pass
        finally:
            connection.close()
    except OperationalError:
        return CONNECTION_fAILED


print(register("", "", "", ""))
