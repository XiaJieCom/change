#!/usr/bin/env python3

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SALT_MASTER = 'localhost'

FILE_SERVER = {
    'http':'%s:8000' % SALT_MASTER.strip(),
    'salt':SALT_MASTER
}

FILE_SERVER_BASE_PATH = '/salt/file_center'
#file_server 文件路径

FILE_STORE_PATH = "%s/var/downloads/" % BASE_DIR
#下载目标路径

NEEDLE_CLIENT_ID = 1
#客户端ID

#MQ连接地址
MQ_CONN = {
    'host':'locahost',
    'port': 5672,
    'password':'',
}


