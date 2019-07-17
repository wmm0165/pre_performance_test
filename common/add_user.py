# -*- coding: utf-8 -*-
# @Time : 2019/7/10 16:23
# @Author : wangmengmeng
"""用户中心批量添加用户"""
import hashlib
import requests
import json
from config.read_config import ReadConfig


class AddUser:
    def __init__(self):
        self.cf = ReadConfig()
        url = self.cf.get('login','address') + '/syscenter/api/v1/currentUser'
        username = self.cf.get('login','username')
        passwd = self.cf.get('login','password')
        m = hashlib.md5()  # 创建md5对象
        m.update(passwd.encode())  # 生成加密字符串
        password = m.hexdigest()
        params = {"name": username, "password": password}
        self.headers = {'Content-Type': "application/json"}
        self.session = requests.session()
        res = self.session.post(url, data=json.dumps(params), headers=self.headers).json()
        print(res)

    def add_user(self, count):
        url = self.cf.get('login','address') + '/syscenter/api/v1/auth/addUser'
        params = {
            "dtoUser": {
                "username": "cs" + str(count),
                "realname": "测试" + str(count),
                "password": "123456"
            },
            "drugIdList": [],
            "roleIdList": [88, 91, 89],
            "dtoUserDeptList": [],
            "resourceIdList": [],
            "dtoUserWorknumList": []
        }
        res = self.session.post(url, data=json.dumps(params), headers=self.headers).json()
        print(res)


if __name__ == '__main__':
    user = AddUser()
    for i in range(1, 5):
        user.add_user(i)