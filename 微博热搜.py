# --*-- coding:utf-8 --*--
# @FileName      : 微博热搜.py
# @DateTime      : 2022/11/24 17:51
# @Author        : SXS
# @Email         : sxs1316@outlook.com
# @description   : 微博热搜排行
# @Version       : 1.0

# 导入模板
import json
import requests
from urllib.parse import quote


def get_rank():
    # 爬取资源站点
    URL = 'https://weibo.com/ajax/statuses/hot_band'

    # 获取微博排行数据
    result = requests.get(URL)
    _ = json.loads(result.text)['data']
    data_hot_list = _['band_list']

    # 处理数据
    data = []
    for i in data_hot_list:
        dict = {}
        dict['hot_rank'] = i['rank']+1
        dict['hot_title'] = i['note']
        dict['hot_value'] = i['num']
        dict['hot_url'] = 'https://s.weibo.com/weibo?q='+quote("#"+i['note']+"#")
        data.append(dict)

    return data


if __name__ == '__main__':
    print(get_rank())
