# -*- coding: utf-8 -*-
# @Time : 2019/7/17 16:25
# @Author : wangmengmeng
from add_user import AddUser
from delete_user import DeleteUser

def run():
    deleteuser = DeleteUser()
    deleteuser.delete_user()
    num = int(input("请输入需要新增的用户数;"))
    adduser = AddUser()
    for i in range(1, (num+1)):
        adduser.add_user(i)


if __name__ == '__main__':
    run()