from lxml import html
import csv, os, json
import requests
from exceptions import ValueError
from time import sleep


def AmzonParser(url, asin):
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36'}
    page = requests.get(url, headers=headers)
    while True:
        sleep(3)
        try:
            doc = html.fromstring(page.content)
            XPATH_NAME = '//h1[@id="title"]//text()'
            XPATH_SALE_PRICE = '//span[contains(@id,"ourprice") or contains(@id,"saleprice")]/text()'
            XPATH_ORIGINAL_PRICE = '//td[contains(text(),"List Price") or contains(text(),"M.R.P") or contains(text(),"Price")]/following-sibling::td/text()'
            XPATH_CATEGORY = '//a[@class="a-link-normal a-color-tertiary"]//text()'
            XPATH_AVAILABILITY = '//div[@id="availability"]//text()'
            XPATH_RANK = '//th[contains(text(), "Best Sellers Rank")]/following-sibling::td/child::node()/child::node()/text()'

            RAW_NAME = doc.xpath(XPATH_NAME)
            RAW_SALE_PRICE = doc.xpath(XPATH_SALE_PRICE)
            RAW_CATEGORY = doc.xpath(XPATH_CATEGORY)
            RAW_ORIGINAL_PRICE = doc.xpath(XPATH_ORIGINAL_PRICE)
            RAw_AVAILABILITY = doc.xpath(XPATH_AVAILABILITY)
            RAW_RANK = doc.xpath(XPATH_RANK)

            NAME = ' '.join(''.join(RAW_NAME).split()) if RAW_NAME else None
            SALE_PRICE = ' '.join(''.join(RAW_SALE_PRICE).split()).strip() if RAW_SALE_PRICE else None
            CATEGORY = ' > '.join([i.strip() for i in RAW_CATEGORY]) if RAW_CATEGORY else None
            ORIGINAL_PRICE = ''.join(RAW_ORIGINAL_PRICE).strip() if RAW_ORIGINAL_PRICE else None
            AVAILABILITY = ''.join(RAw_AVAILABILITY).strip() if RAw_AVAILABILITY else None
            RANK = ''.join(RAW_RANK).strip()

            if not ORIGINAL_PRICE:
                ORIGINAL_PRICE = SALE_PRICE

            if page.status_code != 200:
                raise ValueError('captha')
            data = {
                'ASIN': asin,
                'NAME': NAME,
                'SALE_PRICE': SALE_PRICE,
                'CATEGORY': CATEGORY,
                'ORIGINAL_PRICE': ORIGINAL_PRICE,
                'AVAILABILITY': AVAILABILITY,
                'RANK' : RANK,
                'URL': url,
            }

            print "done"
            return data
        except Exception as e:
            print e


def ReadAsin():
    # AsinList = csv.DictReader(open(os.path.join(os.path.dirname(__file__),"Asinfeed.csv")))
    AsinList = [
'B01CA1856W',
'B01CA1DLSY',
'B01CA1IGRU',
'B01CA1LUTG',
'B01CA1OTMG',
'B017EPG5RA',
'B01KYHNHIA',
'B01CA3435W',
'B01CA3BNK0',
'B01CA3EJH4',
'B01C78C62M',
'B01LWQH0JV',
'B01CA3UUCC',
'B01CA4383E',
'B01CA489EC',
'B01CA4D5EQ',
'B01M0BCBG4',
'B01CD9HGC0',
'B01CD9MKHQ',
'B01CEN9P1A',
'B01CDHROE2',
'B01CDHNOU0',
'B01CDA0IKG',
'B01CD9XXHW',
'B01CD9VHWA',
'B01CA78PDE',
'B00BS81QZ6',
'B00BS81RDC',
'B01CA7HWRE',
'B01M0B1XK9',
'B01CCVGCE2',
'B01CCVVQNE',
'B01CCW05L2',
'B01CCWBQ5Q',
'B01ALQDH6Q',
'B01LX1L8CI',
'B01LY0SCER',
'B01M0ASSZL',
'B01CE4IH90',
'B01CCZT26I',
'B01CE4GXWS',
'B01CCZYCBS',
'B01H2J1GUE',
'B01H2IYLY8',
'B01H2IWXCU',
'B01H2ISTS2',
'B01GS57BE8',
'B01GS6M0ZW',
'B01GS6JW58',
'B01H238MKM',
'B01H24036W',
'B01H2475A4',
'B01H2IN3L0',
'B01H24KGNW',
'B01GS6I8DA',
'B01GS6GIEG',
'B01GS6ERF8',
'B01GS9UTDE',
'B01H26DF06',
'B01H26PCJ8',
'B01LX24BRW',
'B01LY0SAW8',
'B01M0ASW1T',
'B01LXDD7MA',
'B01LZNCSQ1',
'B01M19W74V',
'B01LWPX1O1',
'B01M19FQAG',
'B01LYZWB03',
'B01M0AT0YK',
'B01M0ASTYB',
'B01M0CXGC1',
'B01M0OLVQ1',
'B01LZ22NO9',
'B01M1C3TSW',
'B01M0CY0RY',
'B01LWQK283',
'B01M0BFZQY',
'B01LZNZBEU',
'B01M0YQUCE',
'B01LXE052A',
'B01M0YAKKZ',
'B01M0YECDA',
'B01LZNHMDG',
'B01M0ATH9L',
'B01LZBP4IJ',
'B01LXP1IA7',
'B01LYCF5OS',
'B01LX1LECE',
'B01M0MG1JS',
'B01LZZ4MUD',
'B01LYZWKPI',
'B01LWQ21VE',
'B01LZNHPRS',
'B01LWQ21U8',
'B01M0ASVEG',
 'B01LZNCENK',
'B01LZB581Z',
'B01LXP1HCJ',
'B01M1J3A77',
'B01M0MGDME',
'B01LYC1NBD',
'B01LYNU930',
'B01M0ADRPH',
'B01LXOMWMD',
'B01LYZ4UJS',
'B01LYC1NB2',
'B01KZRZMZU',
'B01H24VVFE',
'B01H25FHQC',
'B01H27JW2U',
'B01H287HF8',
]

    extracted_data = []
    for i in AsinList:
        url = "http://www.amazon.com/dp/" + i
        print "Processing: " + url
        extracted_data.append(AmzonParser(url, i))
        sleep(5)
    f = open('data.json', 'w')
    json.dump(extracted_data, f, indent=4)


if __name__ == "__main__":
    ReadAsin()