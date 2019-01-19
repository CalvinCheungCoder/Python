# 根据课程分类拉取分类下的数据并存储到数据库
import urllib.request
import json
import ssl
import pymysql

import os
import re

connection = pymysql.connect(host = 'localhost',
                             user = 'root',
                             password = '123456',
                             database = 'ylyk',
                             charset = 'utf8')

cursor = connection.cursor()
context = ssl._create_unverified_context()

with open('ylyk.json','r') as f:
    data = json.load(f)
    data_listArr = data['data']
    for data_detail in data_listArr:
        children_arr = data_detail['children']
        # print(children_arr)
        for children in children_arr:
            children_id = children['id']
            children_classname = children['class_name']
            url = 'http://api.ylyk.com/v1/album/classalbums/{0}'.format(children_id)
            req = urllib.request.Request(url)
            with urllib.request.urlopen(req,context=context) as response:
                detail_data = response.read()
                json_data = detail_data.decode()
                jsonStr = json.loads(json_data)
                jsonDataArr = jsonStr['data']
                for listdata in jsonDataArr:
                    id = listdata['id']
                    name = listdata['name']
                    desc = listdata['desc']
                    cover_url = listdata['cover_url']
                    goods_id = listdata['goods_id']
                    paytype_id = listdata['paytype_id']
                    value = (id,name,desc,cover_url,goods_id,paytype_id)
                    sql = "INSERT INTO ylyk_sourselist (id, name, des, coverurl, goods_id, paytype_id) values(%s, '%s', '%s', '%s', %s, %s)" % value
                    try:
                        cursor.execute(sql)
                        connection.commit()
                        print('插入成功\n')
                    except:
                        connection.rollback()
                        print('插入错误\n')
                        break