# -*- coding: utf-8 -*-
# @Time : 2019/6/7 9:44
# @Author : wangmengmeng
from configparser import ConfigParser
import os


class ReadConfig():
    # 实例化ConfigParser 并加载配置文件
    def __init__(self):
        path = os.path.dirname(os.path.abspath(__file__))
        configfile = os.path.join(path, 'config.ini')
        self.conf = ConfigParser()
        self.conf.read(configfile, encoding='utf8')

    def get(self, field, key):
        return self.conf.get(field, key)


if __name__ == '__main__':
    rc = ReadConfig()
    a = rc.get('db', 'host')
    print(a)
