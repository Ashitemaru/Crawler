# -*- coding: utf-8 -*-

# Global settings start

firstCookie: str = 'll="108288"; bid=m1mVUymNDOM; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1599552655%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DZCsdNfeUlqJPXvYH3-RYp6epL4oYoz5g8JvXwjrPEMBzdVdswjJ-Xt3ViN_jHET2%26wd%3D%26eqid%3Dff137da500040467000000035f573c8d%22%5D; _pk_ses.100001.4cf6=*; ap_v=0,6.0; __utma=30149280.1705845896.1599552656.1599552656.1599552656.1; __utmb=30149280.0.10.1599552656; __utmc=30149280; __utmz=30149280.1599552656.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utma=223695111.1242283030.1599552656.1599552656.1599552656.1; __utmb=223695111.0.10.1599552656; __utmc=223695111; __utmz=223695111.1599552656.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __yadk_uid=SOuevj3sPOLuIebHzpjholHqYwJcQ1oG; _vwo_uuid_v2=D48660C69DD7B895DAA354CAFDA0DC308|9bdfdac5f71d475c381b5749980fa5db; __gads=ID=7d4e4da2e656b7ca:T=1599552663:S=ALNI_MYd2ZjR88a-9uDZTrJgd-MGl4YSbw; _pk_id.100001.4cf6=7aea1f23f3e9fb63.1599552655.1.1599553263.1599552655.'

secondCookie: str = 'll="108288"; bid=m1mVUymNDOM; ap_v=0,6.0; __utmc=30149280; __utmc=223695111; __yadk_uid=SOuevj3sPOLuIebHzpjholHqYwJcQ1oG; _vwo_uuid_v2=D48660C69DD7B895DAA354CAFDA0DC308|9bdfdac5f71d475c381b5749980fa5db; __gads=ID=7d4e4da2e656b7ca:T=1599552663:S=ALNI_MYd2ZjR88a-9uDZTrJgd-MGl4YSbw; __utma=30149280.1705845896.1599552656.1599552656.1599555763.2; __utmb=30149280.0.10.1599555763; __utmz=30149280.1599555763.2.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utma=223695111.1242283030.1599552656.1599552656.1599555763.2; __utmb=223695111.0.10.1599555763; __utmz=223695111.1599555763.2.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1599555763%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DZCsdNfeUlqJPXvYH3-RYp6epL4oYoz5g8JvXwjrPEMBzdVdswjJ-Xt3ViN_jHET2%26wd%3D%26eqid%3Dff137da500040467000000035f573c8d%22%5D; _pk_ses.100001.4cf6=*; _pk_id.100001.4cf6=7aea1f23f3e9fb63.1599552655.2.1599556193.1599553263.'

doubanFirstUrl: str = 'https://movie.douban.com/j/search_subjects?type=movie&tag=%E8%B1%86%E7%93%A3%E9%AB%98%E5%88%86&sort=recommend&page_limit=1000&page_start=0'

doubanSecondUrl: str = 'https://movie.douban.com/j/search_subjects?type=movie&tag=%E5%86%B7%E9%97%A8%E4%BD%B3%E7%89%87&sort=recommend&page_limit=1000&page_start=0'

firstHeaders: dict = {
    'Accept': '*/*',
    # 'Accept-Encoding': 'gzip',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Cookie': firstCookie,
    'Host': 'movie.douban.com',
    'Referer': 'https://movie.douban.com/explore',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
}

secondHeaders: dict = {
    'Accept': '*/*',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Cookie': secondCookie,
    'Host': 'movie.douban.com',
    'Referer': 'https://movie.douban.com/explore',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
}

# Global settings over

from urllib.request import Request, urlopen
from html.parser import HTMLParser
import ssl
import json
import time

ssl._create_default_https_context = ssl._create_unverified_context

def fetchBasics(url: str, headers: dict):
    with urlopen(Request(url = url, headers = headers)) as f:
        data = f.read()
    return data.decode('utf-8')

def fetchDetail(url: str):
    header = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36',
    }
    with urlopen(Request(url = url, headers = header)) as f:
        data = f.read()
        if f.status == 403:
            return ''
        else:
            return data.decode('utf-8')

def main():
    basicsList = []

    firstBasic = fetchBasics(doubanFirstUrl, firstHeaders)
    secondBasic = fetchBasics(doubanSecondUrl, secondHeaders)

    basicFile = open('/Users/ashitemaru/Downloads/CodingFolder/FreshmanSummer/movies/crawler/database/basics.json', 'w')
    basicFile.write(firstBasic)
    basicFile.write(secondBasic)
    basicFile.close()

    for x in json.loads(firstBasic)['subjects']:
        basicsList.append(x)

    for x in json.loads(secondBasic)['subjects']:
        basicsList.append(x) 

    print('GET LIST!')
    
    for i, x in enumerate(basicsList):
        print('Now fetching: No', str(i), x['url'])
        file = open('/Users/ashitemaru/Downloads/CodingFolder/FreshmanSummer/movies/crawler/database/' + x['title'] + '.html', 'w')
        detailHTML = fetchDetail(x['url'])
        if detailHTML == '':
            print('IP banned!')
            break
        print('OK!')
        file.write(detailHTML)
        file.close()
        time.sleep(6)
    

if __name__ == '__main__':
    main()