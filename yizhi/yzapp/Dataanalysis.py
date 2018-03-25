# coding:utf-8
# -*- coding:utf-8 -*-
import MySQLdb
import pygal
# import sys
# reload(sys)
# sys.setdefaultencoding('utf8')


def mysql_con(name):
    conn = MySQLdb.connect(host='127.0.0.1', port=3306, user='root', passwd='newpswd', db='test', charset='utf8')
    cur = conn.cursor()
    sql = "select position_name from yzapp_position where position_name like '%s'" % name
    # sqli = "select position_name from yzapp_position where city='厦门' AND education='本科' AND position_name like'%s'" % name
    # sqli = "select education from yzapp_position where education like '%s'" % name
    # sqli = "select workyear from yzapp_position where workyear like '%s'" % name
    # sqli = "select salary from yzapp_position where workyear='不限' AND education='本科' AND salary like '%s' or workyear='不限' AND education='本科' AND salary like '%s' or workyear='不限' AND education='本科' AND salary like '%s' or workyear='不限' AND education='本科' AND salary like '%s' or workyear='不限' AND education='本科' AND salary like '%s'" % (names[0],names[1],names[2],names[3],names[4])
    cur.execute(sql)
    results = cur.fetchall()
    return results

def mysql_con2(names):
    conn = MySQLdb.connect(host='127.0.0.1', port=3306, user='root', passwd='newpswd', db='test', charset='utf8')
    cur = conn.cursor()
    # sqli = "select position_name from yzapp_position where city='厦门' AND (education='大专' OR education='不限') AND position_name like'%s'" % name
    # sqli = "select education from yzapp_position where education like '%s'" % name
    # sqli = "select workyear from yzapp_position where workyear like '%s'" % name
    sqli = "select salary from yzapp_position where workyear='1-3年' AND (education='大专' OR education='不限')  AND salary like '%s' or workyear='1-3年' AND (education='大专' OR education='不限')  AND salary like '%s' or workyear='1-3年' AND (education='大专' OR education='不限') AND salary like '%s' or workyear='1-3年' AND (education='大专' OR education='不限') AND salary like '%s' or workyear='1-3年' AND (education='大专' OR education='不限') AND salary like '%s'" % (
    names[0], names[1], names[2], names[3], names[4])
    cur.execute(sqli)
    results = cur.fetchall()
    return results

def pygal_run():
    #职位需求比例
    java = mysql_con('java')
    c = mysql_con('c')
    python = mysql_con('python')
    php = mysql_con('php')
    android = mysql_con('android')
    ios = mysql_con('ios')
    web = mysql_con('web')
    pie_chart = pygal.Bar()
    pie_chart.title = 'position analysis'
    pie_chart.add('Java', len(java))
    pie_chart.add('C++/C#', len(c))
    pie_chart.add('Python', len(python))
    pie_chart.add('Php', len(php))
    pie_chart.add('Android', len(android))
    pie_chart.add('Ios', len(ios))
    pie_chart.add('Web', len(web))
    pie_chart.render_to_file('position_date_analysis.svg')

    #学历要求比例
    # pie_chart2 = pygal.Pie()
    # dazhuan = mysql_con('大专')
    # benke = mysql_con('本科')
    # buxian = mysql_con('不限')
    # pie_chart2.title = 'position analysis'
    # pie_chart2.add('undergraduate',len(benke))
    # pie_chart2.add('college',len(dazhuan))
    # pie_chart2.add('There is no limit',len(buxian))
    # pie_chart2.render_to_file('position_date_analysis3.svg')

    #工作经验要求比例
    # pie_chart3 = pygal.Pie()
    # year1_3 = mysql_con('1-3年')
    # year3_5 = mysql_con('3-5年')
    # year5_10 = mysql_con('5-10年')
    # nolimit = mysql_con('不限')
    # pie_chart3.title = 'position analysis'
    # pie_chart3.add('1-3year', len(year1_3))
    # pie_chart3.add('3-5year', len(year3_5))
    # pie_chart3.add('5-10year',len(year5_10))
    # pie_chart3.add('no limit',len(nolimit))
    # pie_chart3.render_to_file('position_date_analysis4.svg')

    #工资待遇
    # pie_chart4 = pygal.Bar()
    # pie_chart4.title = 'XiaMen'
    # salaries = ["1k-5k", "6k-10k", "10k-15k", "15k-20k"]
    # names = ['1k%', '2k%', '3k%', '4k%', '5k%']
    # names2 = ['6k%', '7k%', '8k%', '9k%', '10k%']
    # names3 = ['11k%', '12k%', '13k%', '14k%', '15k%']
    # names4 = ['16k%', '17k%', '18k%', '19k%', '20k%']
    # data1 = mysql_con(names)
    # data2 = mysql_con(names2)
    # data3 = mysql_con(names3)
    # data4 = mysql_con(names4)
    # pie_chart4.x_labels = salaries
    # pie_chart4.add('1-5k', len(data1))
    # pie_chart4.add('6-10k', len(data2))
    # pie_chart4.add('11-15k', len(data3))
    # pie_chart4.add('16-20k', len(data4))
    # pie_chart4.render_to_file('position_date_analysis4.svg')

    #厦门本科与专科工资待遇对比
    # pie_chart5 = pygal.Bar()
    # pie_chart5.title = 'XiaMen'
    # salaries = ["1k-5k", "6k-10k", "10k-15k", "15k-20k"]
    # names = ['1k%', '2k%', '3k%', '4k%', '5k%']
    # names2 = ['6k%', '7k%', '8k%', '9k%', '10k%']
    # names3 = ['11k%', '12k%', '13k%', '14k%', '15k%']
    # names4 = ['16k%', '17k%', '18k%', '19k%', '20k%']
    # data1 = mysql_con(names)
    # data2 = mysql_con(names2)
    # data3 = mysql_con(names3)
    # data4 = mysql_con(names4)
    # data5 = mysql_con2(names)
    # data6 = mysql_con2(names2)
    # data7 = mysql_con2(names3)
    # data8 = mysql_con2(names4)
    #
    # pie_chart5.x_labels = salaries
    # pie_chart5.add('ZhuanKe', [len(data5), len(data6), len(data7), len(data8)])
    # pie_chart5.add('BenKe', [len(data1), len(data2), len(data3), len(data4)])
    # pie_chart5.render_to_file('position_date_analysis6.svg')

    #厦门本科与专科职位需求对比
    # pie_chart6 = pygal.Bar()
    # pie_chart6.title = 'XiaMen'
    # position = ["Java", "PHP", "Android", "IOS", ".NET", "C++", "Python"]
    # java = mysql_con('%Java%')
    # php = mysql_con('%php%')
    # android = mysql_con('%android%')
    # android2 = mysql_con('%安卓%')
    # ios = mysql_con('%ios%')
    # net = mysql_con('%.net%')
    # c = mysql_con('%c++%')
    # python = mysql_con('%python%')
    #
    # java2 = mysql_con2('%Java%')
    # php2 = mysql_con2('%php%')
    # android3 = mysql_con2('%android%')
    # android4 = mysql_con2('%安卓%')
    # ios2 = mysql_con2('%ios%')
    # net2 = mysql_con2('%.net%')
    # c2 = mysql_con2('%c++%')
    # python2 = mysql_con2('%python%')
    #
    # pie_chart6.x_labels = position
    # pie_chart6.add('DaZhuan', [len(java2), len(php2), (len(android3)+len(android4)), len(ios2), len(net2), len(c2), len(python2)])
    # pie_chart6.add('Benke', [len(java), len(php), (len(android)+len(android2)), len(ios), len(net), len(c), len(python)])
    # pie_chart6.render_to_file('position_date_analysis7.svg')

    #厦门专科与本科工作经验与工资待遇
    #厦门专科与本科工作经验为不限的工资待遇对比分析
    # pie_chart7 = pygal.Bar()
    # pie_chart7.title = 'ZhuanKe workyear = 1-3year & Benke workyear = nolimit'
    # X_title = ["1k-5k", "6k-10k", "10k-15k", "15k-20k"]
    # pie_chart7.x_labels = X_title
    # salary1 = ['1k%', '2k%', '3k%', '4k%', '5k%']
    # salary2 = ['6k%', '7k%', '8k%', '9k%', '10k%']
    # salary3 = ['11k%', '12k%', '13k%', '14k%', '15k%']
    # salary4 = ['16k%', '17k%', '18k%', '19k%', '20k%']
    # data_Z1 = mysql_con2(salary1)
    # data_Z2 = mysql_con2(salary2)
    # data_Z3 = mysql_con2(salary3)
    # data_Z4 = mysql_con2(salary4)
    # data_B1 = mysql_con(salary1)
    # data_B2 = mysql_con(salary2)
    # data_B3 = mysql_con(salary3)
    # data_B4 = mysql_con(salary4)
    # pie_chart7.add('ZhuanKe', [len(data_Z1), len(data_Z2), len(data_Z3), len(data_Z4)])
    # pie_chart7.add('BenKe', [len(data_B1), len(data_B2), len(data_B3), len(data_B4)])
    # pie_chart7.render_to_file('position_date_analysis10.svg')

    #厦门与北上广深杭等互联网一线城市的职位对比系列
    #厦门与北上广深杭的职位需求
    # pie_chart8 = pygal.Bar()
    # pie_chart8.title = 'XiaMen : Boss city'
    # position = ['Java', 'C/C++', '.Net', 'Python', 'PHP', 'Android', 'IOS', 'Go', 'Count']

if __name__=='__main__':
    pygal_run()
    # key_position = raw_input("请输入sql语句:")
    # java = mysql_con(key_position)
    # print(len(java))