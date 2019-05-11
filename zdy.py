import requests
import re
import execjs
print(execjs.get().name)
from urllib.request import quote  # py3: from urllib import quote 会失败

headers = {
    'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"
}
with open('get_anticontent.js', 'r', encoding='utf-8') as f:
    js = f.read()

url = 'http://mobile.yangkeduo.com/mall_page.html?mall_id=256553930&sort_type=1'

response = requests.get(url, headers=headers)
# list_id = re.search('"listID":"([^"]+)"', response.text).group(1)
# flip = re.search('"flip":"([^"]+)"', response.text).group(1)

ctx = execjs.compile(js)
anti_content = ctx.call('anticontent',url)
# 获取下一页
next_url = 'http://mobile.yangkeduo.com/proxy/api/api/turing/mall/query_cat_goods?category_id=0&type=0&mall_id=256553930&page_no={0}&page_size=50&sort_type=_sales&anticontent={1}&refer_page_param=&refer_page_sn=&list_id=mall_main_xCIKSv&page_from=39&pdduid=0'.format(2,str(anti_content))
# 获取下一页的参数有这几个，其中第一个参数为页数，最后一个参数为加密参数，其他的从搜索页第一页获取，上面代码获取，都是不变的
r = requests.get(next_url, headers=headers)
print(r.text)

# 不断获取下一页
# def get_next_page(page, url):
#     ctx = execjs.compile(js)
#     anti_content = ctx.call('get_anti', url)  # 每一页的anti-content 都不一样
#     url = next_url.format(page, list_id, key_name, flip, anti_content)
#     r = requests.get(url, headers=headers)
#     for item in r.json()['items']:
#         print(item)
#
#
# for i in range(2, 11):
#     get_next_page(i, url)