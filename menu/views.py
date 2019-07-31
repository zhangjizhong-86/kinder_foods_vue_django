from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.core import serializers
import json
from datetime import datetime, timezone, timedelta
from collections import OrderedDict
import pymysql.cursors
from copy import deepcopy
from menu.models import Menu # Model
import locale
locale.setlocale(locale.LC_ALL, 'zh-CN')

# Create your views here.
def ajax(request):
    if request.method == 'POST':
        # 获取页面请求的日期，如果没有，则默认为当前日期（UTC+8）
        # 页面时区以浏览器自动调整
        query_date = request.POST.get('query_date', datetime.now(timezone(timedelta(hours=8))).strftime('%Y-%m-%d'))
        query_week = Menu.objects.filter(date=query_date)[0].week # 查符合日期的第一条记录，TODO，处理ObjectDoesNotExist异常
        query_week_menu = Menu.objects.filter(week=query_week).all()

        data = {}
        # week_menu_dict = {}
        # day_menu_dict = {'早点':[],'午餐':[],'午点':[],'体弱儿营养菜':[]}
        

        # for row in query_week_menu:
        #     date = row.date.strftime('%Y-%m-%d').replace('-0','-') # 去除补零，和js中的格式匹配
        #     if date not in week_menu_dict.keys():
        #         # 复制一个日级别的数据结构
        #         week_menu_dict[date] = deepcopy(day_menu_dict)
        #     week_menu_dict[date][row.diet].append(row.food if len(row.comment)==0 else row.food + '（{}）'.format(row.comment))

        # 数据结构：[{ 日期: '2019-7-1<br>星期一', 早点: '粥<br/>牛奶', 午餐: '饭<br/>汤', 午点: '饼干<br/>果汁', 体弱儿营养菜: '...' }, ... ]
        week_menu_list = []
        daily_menu_dict = {'日期':'', '早点':[], '午餐':[], '午点':[], '体弱儿营养菜':[]}
        for row in query_week_menu:
            date = row.date.strftime('%Y-%m-%d').replace('-0','-')  #去除补零，和js中的query_date格式匹配
            date_with_weekday = {'date': date, 'weekday': row.date.strftime('%A')}
            if date_with_weekday not in [daily_menu['日期'] for daily_menu in week_menu_list]:
                # 复制一个日级别的数据结构
                week_menu_list.append(deepcopy(daily_menu_dict))
                week_menu_list[-1]['日期'] = date_with_weekday
            week_menu_list[-1][row.diet].append(row.food if len(row.comment)==0 else row.food + '（{}）'.format(row.comment))
        for daily_menu in week_menu_list:
            daily_menu['早点'] = '<br/>'.join(daily_menu['早点'])
            daily_menu['午餐'] = '<br/>'.join(daily_menu['午餐'])
            daily_menu['午点'] = '<br/>'.join(daily_menu['午点'])
            daily_menu['体弱儿营养菜'] = '<br/>'.join(daily_menu['体弱儿营养菜'])
            if daily_menu['日期']['date'] == query_date:
                daily_menu['_rowVariant'] = 'success'

        
        data[query_week] = week_menu_list
        return HttpResponse(json.dumps(data), content_type='application/json')
