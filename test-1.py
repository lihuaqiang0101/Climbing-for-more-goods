from bs4 import BeautifulSoup
import requests
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'
}
url = 'http://mobile.yangkeduo.com/goods.html?goods_id=2912007223&gallery_id=39676967198&refer_page_name=search_result&refer_page_id=10015_1554827784149_r31xPR26qg&refer_page_sn=10015&page_id=10014_1554829862210_SncDT7BPrH&sp=1300&is_back=1'
response = requests.get(url, headers=headers)
text = response.content.decode('utf-8')
soup = BeautifulSoup(text,'html5lib')
goods_mall_info = soup.find('div',class_ = 'goods-mall-info')
spans = goods_mall_info.find_all('span')
numberofgoods = spans[0].text
Sales_volume = spans[1].text