import requests
from lxml import etree
import csv
import json

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'
}
id = input('请输入id:')
# url = 'http://mobile.yangkeduo.com/mall_groups.html?mall_id=256553930&mall_name=%E8%93%93%E4%B9%90%E4%BC%81%E4%B8%9A%E5%BA%97&refer_page_name=mall&refer_page_id=10039_1554802658296_Z4TSE1O7kl&refer_page_sn=10039&sp=0&page_id=10098_1554802663463_xMpH75dg52&is_back=1'
url = 'http://mobile.yangkeduo.com/mall_groups.html?mall_id={}&mall_name=%E7%BB%BF%E5%8A%A8%E4%BD%93%E8%82%B2%E6%9C%8D%E9%A5%B0&refer_page_name=mall&refer_page_id=10039_1554995965510_KMTzqZtZOH&refer_page_sn=10039&sp=0'.format(id)
groupOrderId = []
goodsId = []
goodsName = []
salesTip = []
goods_link = []

def get_onepage(url):
    response = requests.get(url, headers=headers)
    text = response.text
    html = etree.HTML(text)
    result = html.xpath('//script/text()')[5]
    datasets = json.loads(str(result).split('=')[2][1:-6])['store']['mallGroupInfo']['list']
    for dataset in datasets:
        groupOrderId.append(dataset['groupOrderId'])
        goodsId.append(dataset['goodsId'])
        goodsName.append(dataset['goodsName'])
        salesTip.append(dataset['salesTip'])
    for i in range(len(goodsId)):
        goods_link.append('http://mobile.yangkeduo.com/goods.html?group_order_id={0}&status=0&goods_id={1}&hide_sku_selector=1&refer_page_name=mall_groups&refer_page_id=10098_1554802663463_xMpH75dg52&refer_page_sn=10098'.format(groupOrderId[i],goodsId[i]))

if __name__ == '__main__':
    f = open('大家都在拼.csv', 'w', encoding='utf-8')
    filedname = ['商品链接', '宝贝标题', '商品销量']
    writer = csv.DictWriter(f, fieldnames=filedname)
    writer.writeheader()
    get_onepage(url)
    for i in range(len(goodsId)):
        good = {'商品链接': goods_link[i], '宝贝标题': goodsName[i], '商品销量': salesTip[i]}
        writer.writerow(good)
    f.close()