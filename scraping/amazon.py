import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get('https://www.amazon.com/deal/86924c50/?_encoding=UTF8&moreDeals=a192ebd8,762c493b,918396e7,f6ea50ea,64f189a5,25be8738,d8be7665,7659dee4,e451f4e0,3ec564f3,cc7dd8d0,4c9ead63,64662fae&_ref=dlx_gate_dd_dcl_tlt_25be8738_dt&pd_rd_w=0PzhV&content-id=amzn1.sym.def2f06c-d9a7-4927-8433-aa333a9fca53&pf_rd_p=def2f06c-d9a7-4927-8433-aa333a9fca53&pf_rd_r=H25D0YJKHMQ4DES5DYCF&pd_rd_wg=ZtBjQ&pd_rd_r=c6cc48c3-b0ce-4352-b3a8-77a4d798fa30&ref_=pd_gw_unk&language=en_US&currency=INR')
soup = BeautifulSoup(res.text, 'html.parser')

links = soup.select("a.a-size-base.a-color-base.a-link-normal.a-text-normal")
cost = soup.select("span.a-price-whole")
stars = soup.select('span.a-icon-alt')
reviews = soup.select("span.a-size-small.a-color-tertiary")


def sorted_list(links, cost, stars, reviews):
    li = []

    for index, item in enumerate(links):
        title_withspaces = links[index].getText()
        title = title_withspaces.strip()
        dir = links[index].get("href", None)
        href = f"amazon.com{dir}"
        buy_price = cost[index].getText()
        points_string = stars[index].getText()
        points = float(points_string[0:3])
        num_reviews = reviews[index].getText()
        revs = float(num_reviews.replace(",", ""))
        if revs > 500:
            if points > 4.3:

                li.append({'title': title, 'link': href, 'Buy_price': buy_price,
                           'Stars': points, 'Total reviews': revs})
    return li


a = sorted_list(links, cost, stars, reviews)
pprint.pprint(a)
