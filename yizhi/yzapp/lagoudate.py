#  encoding: utf-8
# coding=utf8
import requests
import json
import MySQLdb
# import urllib2,re
# from bs4 import BeautifulSoup as Bs
# import chardet
def get_header():
    headers = {
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
    return headers

# def get_content(company_id):
#     fin_url = r'https://www.lagou.com/jobs/%s.html' %company_id
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
#         'Host': 'www.lagou.com',
#         'Connection': 'keep-alive',
#         'Origin': 'http://www.lagou.com'
#     }
#     req = urllib2.Request(fin_url,headers=headers)
#     page = urllib2.urlopen(req).read()
#     content = page.decode('utf-8')
#     return content
#
#
# def get_description(content):
#     soup = Bs(content, 'lxml')
#     job_description = soup.select('dd[class="job_bt"]')
#     job_description = str(job_description[0])
#     rule = re.compile(r'<[^>]+>')
#     result = rule.sub(' ',job_description)
#     return result
#
# def get_address(content):
#     soup = Bs(content, 'lxml')
#     job_description = soup.select('dd[class="job-address clearfix"]')
#     job_description = str(job_description[0])
#     rule = re.compile(r'<[^>]+>')
#     address = rule.sub(' ', job_description)
#     address = address.lstrip().lstrip('工作地址')
#     address = address.strip().rstrip('查看地图')
#     address = address.replace(' ', '')
#     address = address.replace('\n','')
#     return address

class LagouSpiders(object):

    def __init__(self,datas):
        self.keyword=datas[0]
        self.keypn=datas[1]
        self.keycity=datas[2]

    def spider_run(self):
        s = requests.Session()
        s.keep_alive = False
        s.adapters.DEFAULT_RETRIES = 10
        url="https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false&isSchoolJob=0"
        pn=0

        while(pn<keypn):
            pn=pn+1
            datas = {"first": "true", "pn": str(pn), "kd": keyword, 'city': keycity}
            resp = s.post(url, data=datas, headers=get_header())
            resp.encoding = "utf-8"
            max_num = len(json.loads(resp.text)["content"]["positionResult"]["result"])
            for k in range(max_num):
                json_data = json.loads(resp.text)["content"]["positionResult"]["result"][k]

                city = json_data["city"]#城市
                companyShortName = json_data["companyShortName"],  # 公司名称
                craeteTime = json_data["createTime"],#发布时间
                education = json_data["education"],  # 学历
                positionId = json_data["positionId"], #拉勾网职位id
                positionName = json_data["positionName"],  # 岗位工作类型
                salary = json_data["salary"],  # 工资
                workYear = json_data["workYear"],#工作经验要求


                positionId = positionId[0]
                companyShortName = companyShortName[0].encode("utf-8")
                positionName = positionName[0].encode("utf-8")
                city = city[0].encode("utf-8")+city[1].encode("utf-8")
                salary = salary[0].encode("utf-8")
                education = education[0].encode("utf-8")
                workYear = workYear[0].encode("utf-8")
                craeteTime = craeteTime[0].encode("utf-8")

                # positionId=str(positionId)

                list=(positionId,companyShortName,positionName,city,salary,education,workYear,craeteTime)
                list=json.dumps(list,ensure_ascii=False)

                conn=MySQLdb.connect(host='127.0.0.1',port=3306,user='root',passwd='newpswd',db='test',charset='utf8')
                cur=conn.cursor()
                sqli = "select id from yzapp_position"
                cur.execute(sqli)
                results = cur.fetchall()

                #数据清理
                blean=False
                for row in results:
                    getId = row[0]
                    getId = int(getId)
                    if getId == positionId:
                        print("职位id重复,自动删除重复")
                        blean = True
                        break
                if blean:
                    continue

                # content = get_content(positionId)
                # description = get_description(content)
                # address = get_address(content)
                postedweb = r'https://www.lagou.com/jobs/%s.html' % positionId

                cur.execute("insert into yzapp_position values('%d','%s','%s','%s','%s','%s','%s','%s','%s')"%(positionId,positionName,companyShortName,city,salary,education,workYear,craeteTime,postedweb))#数据存储

                conn.commit()
                cur.close()
                conn.close()




if __name__=='__main__':
    keyword=raw_input("请输入要爬取的岗位:")
    keypn=int(raw_input("请输入要爬取的页数:"))
    keycity=raw_input("请输入要爬取的城市:")
    # position = ['Go']
    # city = ['厦门', '北京', '上海', '广州', '深圳', '杭州']
    #
    # try:
    #     for keyword in position:
    #         for keycity in city:
    #             keypn = 20
    #             datas = [keyword, keypn, keycity]
    #             spider = LagouSpiders(datas)
    #             spider.spider_run()
    # except Exception, e:
    #     print e.message
    datas=[keyword,keypn,keycity]
    spider=LagouSpiders(datas)
    spider.spider_run()