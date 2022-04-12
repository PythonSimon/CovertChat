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
                pass
        finally:
            self.close()

    def findUserByUid(self, uid):
        pass
