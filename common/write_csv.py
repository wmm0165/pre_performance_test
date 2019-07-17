# -*- coding: utf-8 -*-
# @Time : 2019/7/17 17:34
# @Author : wangmengmeng
import csv
import os


class WriteCsv:
    def __init__(self):
        self.csv_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'data', 'users.csv')

    def write_csv(self,*values):
        out = open(self.csv_path, 'w', newline='')  # 打开csv文件
        write_csv = csv.writer(out, dialect='excel')  # 定义文件类型为excel类型
        for v in values:
            write_csv.writerow(v)





if __name__ == '__main__':
    c = WriteCsv()
    c.write_csv([1,2,3])
