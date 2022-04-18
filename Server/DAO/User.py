# coding=utf-8

from pymysql import *

from .Base import BaseDAO
from Server.Configure import *


class UserDAO(BaseDAO):
    
    def __init__(self):
        super(UserDAO, self).__init__()

    def findUser(self, simple=False, **condition):
        try:
            with self.connection.cursor() as cursor:
                if "uid" in condition:
                    sql = "select uid, email, name, password, password2, friends, avatar" \
                               "from UidUser where uid = %s"

                    cursor.execute(sql, condition["uid"])
                elif "email" in condition:
                    sql = "select uid, email, name, password, password2, friends, avatar" \
                               "from EmailUser where uid = %s"

                    cursor.execute(sql, condition["uid"])

                result = cursor.fetchone()

                if result is None:
                    return UserDAOResult.USER_NONE
                else:
                    if simple:
                        user = {
                            "uid": result[0],
                            "email": result[1],
                            "name": result[2],
                            "avatar": result[6],
                        }
                    else:
                        user = {
                            "uid": result[0],
                            "email": result[1],
                            "name": result[2],
                            "password": result[3],
                            "password2": result[4],
                            "friends": [self.findUser(simple=True, uid=uid) for uid in result[5]],
                            "avatar": result[6],
                        }

                    return user
        finally:
            self.close()

    def register(self, uid, email, name, password, password2, friends, avatar) -> UserDAOResult:
        try:
            with self.connection.cursor() as cursor:
                sql = "search email from EmailUser where email=%s"
                user = cursor.execute(sql, uid)

                if user is not None:
                    return UserDAOResult.USER_EXIST

                sql = "insert into UidUser (uid, email, name, password, password2, friends, avatar)" \
                      "value (%s, %s, %s, %s, %s, %s %s)"

                cursor.execute(sql, (uid, email, name, password, password2, friends, avatar))

                sql = "insert into EmailUser (email) value %s"

                cursor.execute(sql, email)

                self.connection.commit()
        except DatabaseError:
            self.connection.rollback()

            return UserDAOResult.FAIL
        else:
            return UserDAOResult.SUCCESS
        finally:
            self.close()
