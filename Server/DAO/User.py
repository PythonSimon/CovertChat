# coding=utf-8

from pymysql import *

from .Base import BaseDAO
from Server.Configure import *


class UserDAO(BaseDAO):
    
    def __init__(self):
        super(UserDAO, self).__init__()

    def findUser(self, **condition):
        try:
            with self.connection.cursor() as cursor:
                if "uid" in condition:
                    sqlOrder = "select uid, email, name, password, password2, friends, avatar" \
                               "from UidUser where uid = %s"
                    cursor.execute(sqlOrder, condition["uid"])
                elif "email" in condition:
                    sqlOrder = "select uid, email, name, password, password2, friends, avatar" \
                               "from EmailUser where uid = %s"
                    cursor.execute(sqlOrder, condition["uid"])

                result = cursor.fetchone()

                if result is None:
                    return UserDAOResult.USER_NONE
                else:
                    user = {
                        "uid": result[0],
                        "email": result[1],
                        "name": result[2],
                        "password": result[3],
                        "password2": result[4],
                        "friends": result[5],
                        "avatar": result[6],
                    }

                    return user
        finally:
            self.close()
