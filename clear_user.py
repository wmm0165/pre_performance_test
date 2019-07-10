# -*- coding: utf-8 -*-
# @Time : 2019/7/10 17:13
# @Author : wangmengmeng
"""清除数据库中用户代码以cs开头的用户数据"""
import pymysql
from config.read_config import ReadConfig

class clear_user:
    def __init__(self):
        cf = ReadConfig()
        self.host = cf.get('db', 'host')
        self.port = cf.get('db','port')
        self.username = cf.get('db','username')
        self.passwd = cf.get('db','password')
        self.dbname = cf.get('db','dbname')
        self.connect = pymysql.Connect(host=self.host, port=int(self.port), user=self.username, passwd=self.passwd,
                                       db=self.dbname,
                                       charset='utf8')
        self.cur = self.connect.cursor()

    def clear_user(self):
        sql = "select CONCAT('truncate table ',  table_name, ';')  from information_schema.`TABLES` where TABLE_SCHEMA= %s"
        self.cur.execute(sql)
        res = self.cur.fetchall()
        print(res)
        print(type(res))
        for s in res:
            self.cur.execute(s[0])
            print(s[0])


if __name__ == '__main__':
    a = clear_user()
    a.clear_user()
