# coding=utf-8

from pymysql import *

from .Base import BaseDAO
from Server.Configure import *


class UserDAO(BaseDAO):
    
    def __init__(self):
        super(UserDAO, self).__init__()

    def finUserByEmail(self, email):
        try:
            with self.connection.cursor() as cursor:
                sqlOrder = "select uid, email, name, password, password2, friends, avatar" \
                           "from User where email=%s"
                cursor.execute(sqlOrder, email)
                user = cursor.fetchone()
        finally:
            self.close()

    def findUserByUid(self, uid):
        pass
