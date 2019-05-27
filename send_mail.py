import os
from django.core.mail import send_mail

os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'

if __name__ == '__main__':
    send_mail('今天有雨', '记得带伞！', 'zhangxueyun@sina.cn', ['maoxy925@qq.com'], )