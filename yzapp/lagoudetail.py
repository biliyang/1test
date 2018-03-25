# encoding:utf-8
import urllib, urllib2, re, json, lxml, requests
from bs4 import BeautifulSoup as Bs
import time
class RedirctHandler(urllib2.HTTPRedirectHandler):

    def http_error_301(self, req, fp, code, msg, headers):
        pass

    def http_error_302(self, req, fp, code, msg, headers):
        pass


def get_page(url, pn, keyword):
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Referer": "https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=",
        "X-Requested-With": "XMLHttpRequest",
        "Host": "www.lagou.com",
        "Connection": "keep-alive",
        "Cookie": "user_trace_token=20170522100918-4a05d3033a324bce998dc59f8b6490fe; LGUID=20170522100919-a9ef5612-3e93-11e7-a2c0-525400f775ce; index_location_city=%E5%85%A8%E5%9B%BD; JSESSIONID=ABAAABAAAGGABCB58BB7BFFEB7ED1EA0B93AC6E6DE68994; _gat=1; PRE_UTM=m_cf_cpt_baidu_pc; PRE_HOST=bzclk.baidu.com; PRE_SITE=http%3A%2F%2Fbzclk.baidu.com%2Fadrc.php%3Ft%3D06KL00c00f7Ghk60yUKm0FNkUsKki2ku00000PW4pNb00000LYoITL.THL0oUhY1x60UWdBmy-bIy9EUyNxTAT0T1d-mWI9mHbLm10snj01rAfz0ZRqn1PDwHcLwjwArjNjnWnYrHDsfWKDnjTvwWf3PDm1fH60mHdL5iuVmv-b5Hnsn1nznjR1njfhTZFEuA-b5HDv0ARqpZwYTZnlQzqLILT8UA7MULR8mvqVQ1qdIAdxTvqdThP-5ydxmvuxmLKYgvF9pywdgLKW0APzm1YYPWnkn6%26tpl%3Dtpl_10085_15730_11224%26l%3D1500117464%26attach%3Dlocation%253D%2526linkName%253D%2525E6%2525A0%252587%2525E9%2525A2%252598%2526linkText%253D%2525E3%252580%252590%2525E6%25258B%252589%2525E5%25258B%2525BE%2525E7%2525BD%252591%2525E3%252580%252591%2525E5%2525AE%252598%2525E7%2525BD%252591-%2525E4%2525B8%252593%2525E6%2525B3%2525A8%2525E4%2525BA%252592%2525E8%252581%252594%2525E7%2525BD%252591%2525E8%252581%25258C%2525E4%2525B8%25259A%2525E6%25259C%2525BA%2526xp%253Did%28%252522m6c247d9c%252522%29%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FH2%25255B1%25255D%25252FA%25255B1%25255D%2526linkType%253D%2526checksum%253D220%26wd%3D%25E6%258B%2589%25E5%258B%25BE%25E7%25BD%2591%26issp%3D1%26f%3D8%26ie%3Dutf-8%26tn%3Dbaiduhome_pg; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F%3Futm_source%3Dm_cf_cpt_baidu_pc; _ga=GA1.2.1091135522.1495418959; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1502537830,1502699986,1502776558,1504462889; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1504462913; LGSID=20170904022245-e1e1be15-90d4-11e7-90e8-5254005c3644; LGRID=20170904022310-f0aa103c-90d4-11e7-bece-525400f775ce; TG-TRACK-CODE=index_search; SEARCH_ID=be39e301ff324226994c10862d7990bb",
        "Origin": "https://www.lagou.com",
        # "Upgrade-Insecure-Requests": "1",
        "X-Anit-Forge-Code": "0",
        "X-Anit-Forge-Token": "None",
        "Accept-Encoding": "gzip,deflate,br",
        "Accept-Language": "zh-CN,zh;q=0.8"
    }
    if pn == 1:
        boo = 'true'
    else:
        boo = 'false'
    page_date = urllib.urlencode([
        ('first', boo),
        ('pn', pn),
        ('kd', keyword)
    ])
    # req =urllib2.Request(url, headers=header)
    # page = urllib2.urlopen(req, data=page_date.encode('utf-8')).read()
    # page = page.decode('utf-8')
    s = requests.Session()
    s.keep_alive = False
    s.adapters.DEFAULT_RETRIES = 10
    datas = {"dirst": "true", "pn": str(pn), "kd": keyword}
    resp = s.post(url, data=datas, headers=header)
    resp.encoding = "utf-8"
    return resp


def read_id(page):

    tag = 'positionId'
    # page_json = json.loads(page.text)
    json_data = json.loads(page.text)["content"]["positionResult"]["result"]
    company_list = []
    for i in range(15):
        company_list.append(json_data[i].get(tag))
    return company_list


def get_content(company_id):
    fin_url = r'https://www.lagou.com/jobs/%s.html' % company_id
    cookies = {'JSESSIONID': 'ABAAABAACBHABBIE18393D251B3E705D2B9F702F89C6B1B',
               '_gat': '1',
               'user_trace_token': '20170522100918-4a05d3033a324bce998dc59f8b6490fe',
               'PRE_UTM': '',
               'PRE_HOST': '',
               'PRE_SITE': '',
               'PRE_LAND': '',
               'LGUID': '20170522100919-a9ef5612-3e93-11e7-a2c0-525400f775ce',
               'SEARCH_ID': 'ef0e31e5ba644825907b62e949a2aaf6',
               'Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6': '1508750481,1508812633,1508827590,1508835340',
               'Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6': '1486066567',
               '_ga': 'GA1.2.1091135522.1495418959',
               'LGSID': '20171025140707-bb4a8e06-b94a-11e7-a7d0-525400f775ce',
               'LGRID': '20171025143719-f34e7e8e-b94e-11e7-a7d7-525400f775ce'}
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
        'Host': 'www.lagou.com',
        'Connection': 'keep-alive',
        'Origin': 'http://www.lagou.com',
        # 'Cookie': cookies
    }

    # response = urllib2.Request(fin_url, headers=headers)
    # # debug_handler = urllib2.HTTPHandler(debuglevel=1)
    # cj = cookielib.CookieJar()
    # openner = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    # req = openner.open(response)
    # content = req.read().decode('utf-8')
    # print len(content)
    # return content
    responese = requests.get(fin_url,headers=headers,allow_redirects=False)
    if(responese.status_code==404):
        responese=requests.get(url,headers=headers)
    if (responese.status_code == 302):
        redirectUrl = responese.headers['location']
        responese = requests.get(redirectUrl)
    content = responese.content
    # content=responese.content.decode('utf-8')
    # print content
    print len(content)
    # print responese.status_code
    time.sleep(5)
    return content


def get_result(content):
    soup = Bs(content, 'lxml')
    job_description = soup.select('dd[class="job_bt"]')
    job_description = str(job_description[0])
    rule = re.compile(r'<[^>]+>')
    result = rule.sub('', job_description)
    return result

def get_address(content):
    soup = Bs(content, 'lxml')
    job_description = soup.select('dd[class="job-address clearfix"]')
    job_description = str(job_description[0])
    rule = re.compile(r'<[^>]+>')
    address = rule.sub('', job_description)
    address = address.lstrip().lstrip('工作地址')
    address = address.strip().rstrip('查看地图')
    address = address.replace(' ', '')
    address = address.replace('\n','')
    return address


if __name__=='__main__':
    url = 'https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false&isSchoolJob=0'
    keyword = 'python'
    keypn = 1
    page=get_page(url, keypn, keyword)

    company_list=read_id(page)
    for company_id in company_list:
        content = get_content(company_id)
        result = get_result(content)
        address = get_address(content)
        print(result)
        print(address)