# coding=utf-8

from pymysql import *

from .Base import BaseDAO
from Server.Configure import *


class UserDAO(BaseDAO):
    
    def __init__(self):
        super(UserDAO, self).__init__()
