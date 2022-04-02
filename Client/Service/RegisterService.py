# coding=utf-8

from email.mime.text import *
from random import *
from smtplib import *


def sendCode(email):
    code = "".join([str(randint(0, 9)) for _ in range(6)])

    message = MIMEText(f"""Hi! 欢迎注册秘信！ 您的验证码为：
    {code}
，请妥善保管，不可告知他人，以防泄露！""")
    message["Subject"] = "秘信验证码"
    message["From"] = "8178778@qq.com"
    message["To"] = email

    try:
        server = SMTP("smtp.qq.com")
        server.login("8178778@qq.com", "akobqoctiqojcaic")

        server.sendmail("@qq.com", email, message.as_string())

        return code
    except SMTPException:
        return -1
