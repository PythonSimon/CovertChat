# coding=utf-8

from pymysql import *

from Server.Configure import *


class BaseDAO(object):

    def __init__(self):
        self.connection = connect(
            host=Server.SERVER_IP,
            user=Server.DAO_USER,
            port=Server.SERVER_DAO_PORT,
            password=Server.DAO_PASSWORD,
            database=Server.DAO_DATABASE,
            charset=Server.DAO_CHARSET
        )

    def close(self):
        self.connection.close()
