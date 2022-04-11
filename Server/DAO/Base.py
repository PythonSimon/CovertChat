# coding=utf-8

from pymysql import *

from Server.Configure import *


class BaseDAO(object):

    def __init__(self):
        self.connect = connect(
            host=Server.SERVER_IP,
            user=""
        )
