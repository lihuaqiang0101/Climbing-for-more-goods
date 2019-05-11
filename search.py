import requests
import re
import execjs
from urllib.parse import quote
from bs4 import BeautifulSoup
import csv

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'
}
with open('get_anticontent.js', 'r', errors='ignore') as f:
    js = f.read()
key = input('请输入要搜索的关键字：')
key_name = quote(key,'utf-8')  # 搜索的关键字
url = 'http://yangkeduo.com/search_result.html?search_key=' + key_name+'&page_id=10015_1554824443031_ELaPbtSIJC&list_id=fsFRcOyCoX&flip=20%3B4%3B0%3B0%3Ba977dbae-31bf-4d66-b80f-fc90a2a1a911&sort_type=price&price_index=-1'
response = requests.get(url, headers=headers)
print(response.text)
list_id = re.search('"listID":"([^"]+)"', response.text).group(1)
flip = re.search('"flip":"([^"]+)"', response.text).group(1)

ctx = execjs.compile(js)
anti_content = ctx.call('get_anti', url)
# 获取下一页
# next_url = 'http://apiv3.yangkeduo.com/search?page={0}&size=50&sort=default&requery=0&list_id={1}&q={2}&flip={3}&anti_content={4}&pdduid=0'
next_url = 'http://apiv3.yangkeduo.com/search?page={0}&size=50&sort=default&requery=0&list_id={1}&q={2}&flip={3}&sort_type=price&price_index=-1&anti_content={4}&pdduid=0'
# 获取下一页的参数有这几个，其中第一个参数为页数，最后一个参数为加密参数，其他的从搜索页第一页获取，上面代码获取，都是不变的
r = requests.get(next_url.format(1, list_id, key_name, flip, anti_content), headers=headers)
text = r.text
URLS = re.findall(r'"link_url.*?",',text)
URL = []#商品链接
MAIL = []#店铺链接
for Url in URLS:
    Url = Url[12:-2]
    URL.append('https://yangkeduo.com/'+Url)


# 不断获取下一页
def get_next_page(page, url):
    ctx = execjs.compile(js)
    anti_content = ctx.call('get_anti', url)  # 每一页的anti-content 都不一样
    url = next_url.format(page, list_id, key_name, flip, anti_content)
    r = requests.get(url, headers=headers)
    for item in r.json()['items']:
        Url = item['link_url']
        URL.append('https://yangkeduo.com/' + Url)
#
#
for i in range(2, 11):
    get_next_page(i, url)
n = int(input('你想要获取前几位店铺：'))
U = URL[:n]
numberofgoods = []
Sales_volume = []
for url in U:
    response = requests.get(url, headers=headers)  # 发起请求得到响应
    text = response.text  # 返回一个经过解码的字符串
    M = re.findall(r'"mallID.*?",', text)
    num = re.findall(r'[0-9][0-9]{1,}', M[0])[0]
    MAIL.append('http://mobile.yangkeduo.com/mall_page.html?mall_id={}&goods_id=6752326139&refer_page_name=goods_detail&refer_page_id=10014_1554853402085_t7nVqxEjh2&refer_page_sn=10014'.format(num))
    response = requests.get(url, headers=headers)
    text = response.content.decode('utf-8')
    soup = BeautifulSoup(text,'html5lib')
    goods_mall_info = soup.find('div',class_ = 'goods-mall-info')
    try:
        spans = goods_mall_info.find_all('span')
        numberofgoods.append(spans[0].text)
        Sales_volume.append(spans[1].text)
    except:
        pass
f = open('{}在各店铺中情况.csv'.format(key), 'w', encoding='utf-8')
filedname = ['店铺链接', '店铺商品数量', '店铺销量']
writer = csv.DictWriter(f, fieldnames=filedname)
writer.writeheader()
for i in range(len(numberofgoods)):
    good = {'店铺链接': MAIL[i], '店铺商品数量': numberofgoods[i], '店铺销量':Sales_volume[i]}
    try:
        if int(numberofgoods[i])>1000 and int(Sales_volume[i])>1000:
            print(good)
            writer.writerow(good)
    except:
        pass
f.close()