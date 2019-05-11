from selenium import webdriver
from lxml import etree
import json
import csv
import time

driver = webdriver.Chrome()

url = [
    'http://mobile.yangkeduo.com/proxy/api/api/turing/mall/query_cat_goods?category_id=0&type=0&mall_id=256553930&page_no=1&page_size=20&sort_type=_sales&anticontent=0alAfxnZNNlo59mwMidoP8hE2K504_JOvHLnCUaRC-_9gD5slbPaq1jItX0eOZJrgvXW4JWar7J9s3uWsRlkT29Jockt9aCVOfS62usW-zk-TJ_fEytDnkK0niyHute-T-FFIFE_xXcXM7Nlbnok6B6mNcqxmvALJKFdAvx_9slUP1DCG3DY610XbpPdrEreI-HDRskeZ3LKfoqFyZgzETTktXJT9j9mbTKD6-Va3_CNH1FMVvfKiR_CgAXg_1rZ9DTTOOvS3Kas07k1noZiPT0tcwiKSifdHGU2HBuADPfNzBQ68yXZdgBc0JmnH4FoLIJfHivMXOCUVT-ORcBLA0lelqQK5jHUFpZ2LFtuwWWapcu_DnWNJDnDuACaXPhPVtLb4i061IjMddAvVc_FwhZcTHA3SzRp4WQ63QyNsdR5AbKdQ-8KwRIjMJhR-8R9tG2u_T&refer_page_param=&refer_page_sn=&list_id=mall_main_Gms7on&page_from=39&pdduid=0',
    'http://mobile.yangkeduo.com/proxy/api/api/turing/mall/query_cat_goods?category_id=0&type=0&mall_id=256553930&page_no=2&page_size=50&sort_type=_sales&anticontent=0alAfxnZyOtoY9EwhNlIp3J2aFgKgfnbKffgYHwG3VTtJIwN1yXUUUpXcMgfH7B2LWZOFxlTvx9pJWhJbol96_iSPhZgtESpiL_cZLQDGHoEkkvym5vXFWaaFZwtAa4kIYSbvfekv8SrNieazX-74BJqrFaeuDyS-btnkE9iYZM7d0W7AZNoZ6ty9gDXHKN351ir2V8hvX1VlXwwVaB4PsuFPkS984g4Sje6RclUKw66hveSOxVwYlwl93VYUNS408YsMzksVixawLkhMvVba7Adkj11WMPOfkjH95cqLfvDnJIR22C_Zoxoc8VlZlrueYpWsBzzHydlXF1zR4Vav8mMNosYRH2yF-crtjtmMl4INtyteTND6cG4ibeF00rG2lbqhJxBt4-3HRGcs-wEIHZh5m7HeU6Z8qxN6-qh6ra5qW7nBx4xjjT-ODAyQijWo4Z9MpF&refer_page_param=&refer_page_sn=&flip=0;&list_id=mall_main_Gms7on&page_from=39&pdduid=0',
    'http://mobile.yangkeduo.com/proxy/api/api/turing/mall/query_cat_goods?category_id=0&type=0&mall_id=256553930&page_no=3&page_size=50&sort_type=_sales&anticontent=0alAfxn5ONt8g9daUNBOa_rrrSIBk_dszoxUbMfMJ1dy-tsum7_16c8p0kpqe0fpOxn-65V-RUAWwa6rTBg9NN80IRhJ8C9J0Y0wUzlQ64q1oHkfEfwTwFMGtTZ8SGw6Uaw7eb77uui0JGBbOSSWb4IekjtAiHhD2XYYKVbtbWtILIBR6VDu7g_ZUCPF5GxuzQ78DoDzMv497kT1DE9R7Wun849On1MGg1P9NQEleGxDyTPMK4Trf9T9KNTNWSVWgBnozskKsafxVEfpmn_w7s4mysxp1VX_bI04nYOhX6fS8pxBWv8ji4nAMV9MuKXLkXjwCD4f8Vr1yAsWu5CxoapJKn5L9JwQreNa9RaqLEy3FDFgNYsCHdiZR2JmKbnGJ3oYD74WN_ZOSWJOsIDwCzaxROXHX_MfXpRe4M7i5YBwj5E5BuOXkaPY3NP-HagEzWehfLrWpKD7FqD1LQWn2ix78yzzdWWuai-7o4lV8-2&refer_page_param=&refer_page_sn=&flip=0;&list_id=mall_main_Gms7on&page_from=39&pdduid=0',
    'http://mobile.yangkeduo.com/proxy/api/api/turing/mall/query_cat_goods?category_id=0&type=0&mall_id=256553930&page_no=4&page_size=50&sort_type=_sales&anticontent=0alAfxnZyOtoY9EwhNXvTw8JPXXPOt4f5lpp43zPF3STFOw5n18X-U-pmZUULEKnMyoG_LGbw5s2WVYi0LlXT09iPTzZZXESpxbp3c1hG4HTUAeU-EObInma-OOpMvVsdtK__F-YUxITF8iqZqcXAbxDCmjlv8KepzK3FGjtX92d-UGYsmGuFRVBB7xZ0-gl93VF6-mcwJRKboLQ-6gEETTjgnKV9x9gyTSqPPJmt_CNO_M9dcU3RUYJHFQGStgwI4GsFl5DI9v0WDweIg0ah9T8FgFvxlNqeT_s5mfDINFryZRIR20Z4Ua_wm8ViOYrmeylhZ1GfvrUNgC1xacA3DOJhDCQVonqL0tmSMhb0p767xpGMdVGkRKpehDhUUforrZgmhHGJXqvtRkJqtcb3pEqgMC58-HaigU6qaNNBW0sR8Eh3vw6vbhoFT8NII3ORYnawbYjo&refer_page_param=&refer_page_sn=&flip=0;&list_id=mall_main_Gms7on&page_from=39&pdduid=0',
    'http://mobile.yangkeduo.com/proxy/api/api/turing/mall/query_cat_goods?category_id=0&type=0&mall_id=256553930&page_no=5&page_size=50&sort_type=_sales&anticontent=0alAfxnZNNtoq9mwMRnv9pWTEtPpfVOYZeu1J5J2ayHgr71u5W_nvyGY3zc6DkLr0MgtaRGaLBP0i0vJWHJao99JoH3t9KV5GfJUswvmzKecTbpfmyBG2Ae5nDkMlhmxSv_HYPHKfFdcDIJMzFYDMl7mru8xsBKvNzHkCKbpC6jUgS3CGJLHQY42xZviLe6WdSSmwFqQXiFfbwqbVBDXfHT95HS4eg2mPVxVzYRrKUdyf-8UwyGOiRwUXAXg_Ir-Pko5vLMwOnZPyIHShKy4JqQ08V0F_q6AKX1f_acgOxuKXOPhb7JQH4d-lTXOJWGqM0OH-nrzwwtp-TJp4cGl88pm7s8l95BSabzk_DaMeaMiVVWfxcu_3hWN1D06miUaXeQPVkIN4i06-ItLI_P-Z7f3x7ah_-QN0_EemQ6NNhs3sUR8nLTH9-c3Z0wIDjcR-8R963wuDX&refer_page_param=&refer_page_sn=&flip=0;&list_id=mall_main_Gms7on&page_from=39&pdduid=0',
    'http://mobile.yangkeduo.com/proxy/api/api/turing/mall/query_cat_goods?category_id=0&type=0&mall_id=256553930&page_no=6&page_size=50&sort_type=_sales&anticontent=0alAfxnZyOtoY9EwhNXvTp8PPlPvn2UI--ZZ6V2avKw5n18X-U-pmZUgNOP-q3JsKmFc2-0c94W0OR6lTJ9lfRTTdUX9y_UnyFuvYAAvNSJnNKOy6w_3lpuc-nDA1dxeF_KZ7kqc5_MhqnQpK5YKATVf8Oql3O6uvQKgo1oVdqz9WpvCWd7jgBb81emrf9PTZv5TSDHUgSK9HtPEPTTjg2e52x97vTkqXPUssKwQCbSxsGONoPkxy_YOTKpBHX3AVHLpEcvkIBfF-NIJ6qWoCGvA53o1NoEbd-7JlbIQU8HESLhPYxf_JbaAR5ZB4NNHERQ1HISva88rN1phlux68WLnN6CLC4Dhn0JzSrGcJrhHKUOOuuIAbuG6IZdXQxUd57GRqPJTXjrl3x_eUItbe_gov9-uVZnZhL5aN7ULOUi7s8_cPMlFys-zRcNRIWN9jKMueJ&refer_page_param=&refer_page_sn=&flip=0;&list_id=mall_main_Gms7on&page_from=39&pdduid=0'
]

goods_id = []
goods_name = []
sales_tip = []
def getgoods(page_size=300):
    for i in range(1,page_size//50+1):
        driver.get(url[i-1])
        source = driver.page_source
        html = etree.HTML(source)
        results = html.xpath('//pre/text()')
        result = str(results[0])
        sets = json.loads(result)
        goods_lists = sets['goods_list']
        for goods_list in goods_lists:
            print(goods_list)
            goods_id.append(goods_list['goods_id'])
            goods_name.append(goods_list['goods_name'])
            try:
                sales_tip.append(goods_list['sales_tip'])
            except:
                sales_tip.append('')
        time.sleep(1)

if __name__ == '__main__':
    getgoods()
    f = open('销量前300个商品.csv','w',encoding='utf-8')
    filedname = ['商品链接', '宝贝标题','商品销量']
    writer = csv.DictWriter(f, fieldnames=filedname)
    writer.writeheader()
    for i in range(len(goods_id)):
        goods_id[i] = 'http://mobile.yangkeduo.com/goods.html?goods_id={}&is_spike=0&refer_page_name=mall&refer_page_id=10039_1554794942359_rtBGA4czhY&refer_page_sn=10039'.format(str(goods_id[i]))
    for i in range(len(goods_id)):
        good = {'商品链接':goods_id[i], '宝贝标题':goods_name[i],'商品销量':sales_tip[i]}
        writer.writerow(good)
    f.close()