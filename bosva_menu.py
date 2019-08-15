# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.4'
#       jupytext_version: 1.1.1
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

import requests
from bs4 import BeautifulSoup
from datetime import datetime
import pymysql
import itertools
import re

url = 'http://www.bosva.cn/'


def log(log, file):
    with open(file, 'a', encoding='utf8') as f:
        print('[' + datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ']' + log, file=f)


def load_html(url):
    r = requests.get(url)
    html = r.content
    soup = BeautifulSoup(html, "html.parser")
    weekly_menu = soup.find('div', attrs={'id':'hmtab1'})
    cells = weekly_menu.find_all('p', 'edt')
    
    # 采集
    date_pat = re.compile('\d{4}-\d{1,2}-\d{1,2}')
    date = []
    breakfast = [] # 早点
    lunch = [] # 午餐
    snack = [] # 午点
    nutrition = [] # 体弱儿营养菜
    comment = [] # 菜品冒号后面的内容
    for i,p in enumerate(cells):
        if i < 5: # 日期
            for string in p.stripped_strings:
                string = string.replace(' ', '') # 2019-05-15 发现日期中有多余的空格
                match = date_pat.match(string)
                if match:
                    date.append(datetime.strptime(string, '%Y-%m-%d'))
        elif i < 10: # 早点
            breakfast.append([string for string in p.stripped_strings])
        elif i < 15: # 午餐
            lunch.append([string for string in p.stripped_strings])
        elif i < 20: # 午点
            snack.append([string for string in p.stripped_strings])
        elif i < 25: # 体弱儿营养菜
            nutrition.append([string for string in p.stripped_strings])
        else:
            week = p.string
    
    # 转格式：将list转为<br/>连接的字符串
    breakfast = ['<br/>'.join(item) for item in breakfast]
    lunch = ['<br/>'.join(item) for item in lunch]
    snack = ['<br/>'.join(item) for item in snack]
    nutrition = ['<br/>'.join(item) for item in nutrition]
    
    # 拼接日期和菜品，适应数据库格式
    # 最后一个是历史遗留的comment，先留着吧
    row = []
    for d in date: 
        row.append([week, d, '早点', breakfast[date.index(d)], ''])
        row.append([week, d, '午餐', lunch[date.index(d)], ''])
        row.append([week, d, '午点', snack[date.index(d)], ''])
        row.append([week, d, '体弱儿营养菜', nutrition[date.index(d)], ''])
    
#     row = ([week, i, '早点', j, ''] if '：' not in j else
#        [week, i, '早点', j.split('：')[0], j.split('：')[1]] 
#        for i in date for j in breakfast[date.index(i)])
#     row = itertools.chain(row, ([week, i, '午餐', j, ''] if '：' not in j else
#                                 [week, i, '午餐', j.split('：')[0], j.split('：')[1]]
#                                 for i in date for j in lunch[date.index(i)]))
#     row = itertools.chain(row, ([week, i, '午点', j, ''] if '：' not in j else
#                                 [week, i, '午点', j.split('：')[0], j.split('：')[1]]
#                                 for i in date for j in snack[date.index(i)]))
#     row = itertools.chain(row, ([week, i, '体弱儿营养菜', j, ''] if '：' not in j else
#                                 [week, i, '体弱儿营养菜', j.split('：')[0], j.split('：')[1]]
#                                 for i in date for j in nutrition[date.index(i)]))
    
    return row


# +
def db_connect(host='localhost', user='root', password='mysql', db='test', charset='utf8'): # password='mysql'
    try:
        return pymysql.connect(host=host,
                             user=user,
                             password=password,
                             db=db,
                             charset=charset,
                             cursorclass=pymysql.cursors.DictCursor)
    except Exception as e:
        print(e)
        conn.close()
        
def to_database(row, conn):
    '''
    写入数据库
    '''
    with conn.cursor() as cur:
        insert_sql = '''insert ignore into kinder_foods values (%s,%s,%s,%s,%s)'''
        rows_affected = cur.executemany(insert_sql, row)
        conn.commit()
    return rows_affected


# -

if __name__ == '__main__' and '__file__' not in globals():
    log_file = 'bosva_menu.log'
    conn = None
    new_num_records = 0
    try:
        conn = db_connect()
        log('Database connected', log_file)
#         row = load_html(url)
        new_num_records = to_database(load_html(url), conn)
        log(str(new_num_records) + ' records updated.', log_file)
    except Exception as e:
        log(str(e), log_file)
    finally:
        if conn:
            conn.close()


