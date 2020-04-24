#!/usr/bin/python3
# -*- coding: utf-8 -*-
import re
import pymysql.cursors
import json
import sys

reload(sys)
sys.setdefaultencoding('utf8')

# 打开200数据库连接
db1 = pymysql.Connect(
    host='192.168.0.200',
    port=3307,
    user='root',
    passwd='DoctorAI#1234',
    db='ip_3.2.4_dev',
    charset='utf8'
)


# 打开阿里云数据库连接
# db2 = pymysql.Connect(
# host='39.98.192.75',
# port=3307,
# user='root',
# passwd='DoctorAI#1234',
# db='ip_3_database_template',
# charset='utf8'
# )

printText = "需要替换的{feature}: {value}"

# 检查是否包含中文
def is_Chinses(uchar):
    for ch in uchar.decode('utf-8'):
        if str.isalnum(uchar):
            return False
    return True


# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db1.cursor()
cursor.execute("SELECT ID FROM DA_MEDICAL_RECORD ORDER BY ID")
ids = cursor.fetchall()

member = []
for i in range(944, ids.__len__(), 1):
    member.append(ids[i][0])

    print(member)
#
# def is_Chinese(word):
# for ch in word:
# if '\u4e00' <= ch <= '\u9fff':
# return True
# return False


for each in member:
    print
each
pname = None
p13 = None
p801 = None
p100 = None
p17 = None
p802 = None
p14 = None
p15 = None
p18 = None
p20 = None
p21 = None
p231 = None
p261 = None
p431 = None
p432 = None
p433 = None
p434 = None
p819 = None
p435 = None
p437 = None
p438 = None
p4910 = None
p6891 = None

# 查出来患者出生地
cursor.execute("SELECT JSON_EXTRACT(CONTENT,'$.homePage.p100') FROM DA_MEDICAL_RECORD where ID=%.2f" % each)
p100Data = cursor.fetchone()
if p100Data != None:
    if p100Data[0] != None and p100Data[0] != '——' and p100Data[0] != '-':
        p100 = eval(p100Data[0])
        print("需要替换的患者出生地: %s " % p100)
        print(printText.format(feature="患者出生地",value=p100))
    else:
        p100 = p100Data[0]
# 查出来患者姓名
cursor.execute("SELECT JSON_EXTRACT(CONTENT,'$.homePage.p4') FROM DA_MEDICAL_RECORD where ID=%.2f" % each)
nameData = cursor.fetchone()
if nameData != None:
    if nameData[0] != None and nameData[0] != '——' and nameData[0] != '-':
        pname = eval(nameData[0])
        print("需要替换的患者名字: %s " % pname)
    else:
        pname = nameData[0]
#
# def checker(data, feature, value):
#     if data != None:
#         if data != ...
# 查出来患者身份证号
cursor.execute("SELECT JSON_EXTRACT(CONTENT,'$.homePage.p13') FROM DA_MEDICAL_RECORD where ID=%.2f" % each)
p13Data = cursor.fetchone()
if p13Data != None:
    if p13Data[0] != None and p13Data[0] != '——' and p13Data[0] != '-':
        p13 = eval(p13Data[0])
        print("需要替换的身份证号: %s " % p13)
    else:
        p13 = p13Data[0]
# 查出来患者现住址
cursor.execute("SELECT JSON_EXTRACT(CONTENT,'$.homePage.p801') FROM DA_MEDICAL_RECORD where ID=%.2f" % each)
p801Data = cursor.fetchone()
if p801Data != None:
    if p801Data[0] != None and p801Data[0] != '——' and p801Data[0] != '-':
        p801 = eval(p801Data[0])
        print("需要替换的现住址: %s " % p801)
    else:
        p801 = p801Data[0]
# 查出来患者户口地址
cursor.execute("SELECT JSON_EXTRACT(CONTENT,'$.homePage.p17') FROM DA_MEDICAL_RECORD where ID=%.2f" % each)
p17Data = cursor.fetchone()
if p17Data != None:
    if p17Data[0] != None and p17Data[0] != '——' and p17Data[0] != '-':
        p17 = eval(p17Data[0])
        print("需要替换的户口地址: %s " % p17)
    else:
        p17 = p17Data[0]
# 查出来患者电话
cursor.execute("SELECT JSON_EXTRACT(CONTENT,'$.homePage.p802') FROM DA_MEDICAL_RECORD where ID=%.2f" % each)
p802Data = cursor.fetchone()
if p802Data != None:
    if p802Data[0] != None and p802Data[0] != '——' and p802Data[0] != '-':
        p802 = eval(p802Data[0])
        print("需要替换的电话: %s " % p802)
    else:
        p802 = p802Data[0]
# 查出来患者工作单位及地址
cursor.execute("SELECT JSON_EXTRACT(CONTENT,'$.homePage.p14') FROM DA_MEDICAL_RECORD where ID=%.2f" % each)
p14Data = cursor.fetchone()
if p14Data != None:
    if p14Data[0] != None and p14Data[0] != '——' and p14Data[0] != '-':
        p14 = eval(p14Data[0])
        print("需要替换的工作单位及地址: %s " % p14)
    else:
        p14 = p14Data[0]
# 查出来患者单位电话
cursor.execute("SELECT JSON_EXTRACT(CONTENT,'$.homePage.p15') FROM DA_MEDICAL_RECORD where ID=%.2f" % each)
p15Data = cursor.fetchone()
if p14Data != None:
    if p15Data[0] != None and p15Data[0] != '——' and p15Data[0] != '-':
        p15 = eval(p15Data[0])
        print("需要替换的单位电话: %s " % p15)
    else:
        p15 = p15Data[0]
# 查出来患者联系人姓名
cursor.execute("SELECT JSON_EXTRACT(CONTENT,'$.homePage.p18') FROM DA_MEDICAL_RECORD where ID=%.2f" % each)
p18Data = cursor.fetchone()
if p14Data != None:
    if p18Data[0] != None and p18Data[0] != '——' and p18Data[0] != '-':
        p18 = eval(p18Data[0])
        print("需要替换的联系人姓名: %s " % p18)
    else:
        p18 = p18Data[0]
# 查出来患者地址
cursor.execute("SELECT JSON_EXTRACT(CONTENT,'$.homePage.p20') FROM DA_MEDICAL_RECORD where ID=%.2f" % each)
p20Data = cursor.fetchone()
if p14Data != None:
    if p20Data[0] != None and p20Data[0] != '——' and p20Data[0] != '-':
        p20 = eval(p20Data[0])
        print("需要替换的地址: %s " % p20)
    else:
        p20 = p20Data[0]
# 查出来患者单位电话
cursor.execute("SELECT JSON_EXTRACT(CONTENT,'$.homePage.p21') FROM DA_MEDICAL_RECORD where ID=%.2f" % each)
p21Data = cursor.fetchone()
if p21Data != None:
    if p21Data[0] != None and p21Data[0] != '——' and p21Data[0] != '-':
        p21 = eval(p21Data[0])
        print("需要替换的单位电话: %s " % p21)
    else:
        p21 = p21Data[0]
# 查出来患者入院病房
cursor.execute("SELECT JSON_EXTRACT(CONTENT,'$.homePage.p231') FROM DA_MEDICAL_RECORD where ID=%.2f" % each)
p231Data = cursor.fetchone()
if p231Data != None:
    if p231Data[0] != None and p231Data[0] != '——' and p231Data[0] != '-':
        p231 = eval(p231Data[0])
        print("需要替换的入院病房: %s " % p231)
    else:
        p231 = p231Data[0]
# 查出来患者出院病房
cursor.execute("SELECT JSON_EXTRACT(CONTENT,'$.homePage.p261') FROM DA_MEDICAL_RECORD where ID=%.2f" % each)
p261Data = cursor.fetchone()
if p261Data != None:
    if p261Data[0] != None and p261Data[0] != '——' and p261Data[0] != '-':
        p261 = eval(p261Data[0])
        print("需要替换的出院病房: %s " % p261)
    else:
        p261 = p261Data[0]
# 查出来患者手术记录科室主任
cursor.execute("SELECT JSON_EXTRACT(CONTENT,'$.homePage.p431') FROM DA_MEDICAL_RECORD where ID=%.2f" % each)
p431Data = cursor.fetchone()
if p431Data != None:
    if p431Data[0] != None and p431Data[0] != '——' and p431Data[0] != '-':
        p431 = eval(p431Data[0])
        print("需要替换的手术记录科室主任: %s " % p431)
    else:
        p431 = p431Data[0]
# 查出来患者手术记录主任医师
cursor.execute("SELECT JSON_EXTRACT(CONTENT,'$.homePage.p432') FROM DA_MEDICAL_RECORD where ID=%.2f" % each)
p432Data = cursor.fetchone()
if p432Data != None:
    if p432Data[0] != None and p432Data[0] != '——' and p432Data[0] != '-':
        p432 = eval(p432Data[0])
        print("需要替换的手术记录主任医师: %s " % p432)
    else:
        p432 = p432Data[0]
# 查出来患者手术记录主治医师
cursor.execute("SELECT JSON_EXTRACT(CONTENT,'$.homePage.p433') FROM DA_MEDICAL_RECORD where ID=%.2f" % each)
p433Data = cursor.fetchone()
if p433Data != None:
    if p433Data[0] != None and p433Data[0] != '——' and p433Data[0] != '-':
        p433 = eval(p433Data[0])
        print("需要替换的手术记录主治医师: %s " % p433)
    else:
        p433 = p433Data[0]
# 查出来患者手术记录住院医师
cursor.execute("SELECT JSON_EXTRACT(CONTENT,'$.homePage.p434') FROM DA_MEDICAL_RECORD where ID=%.2f" % each)
p434Data = cursor.fetchone()
if p434Data != None:
    if p434Data[0] != None and p434Data[0] != '——' and p434Data[0] != '-':
        p434 = eval(p434Data[0])
        print("需要替换的手术记录住院医师: %s " % p434)
    else:
        p434 = p433Data[0]
# 查出来患者手术记录负责护士
cursor.execute("SELECT JSON_EXTRACT(CONTENT,'$.homePage.p819') FROM DA_MEDICAL_RECORD where ID=%.2f" % each)
p819Data = cursor.fetchone()
if p819Data != None:
    if p819Data[0] != None and p819Data[0] != '——' and p819Data[0] != '-':
        p819 = eval(p819Data[0])
        print("需要替换的手术记录负责护士: %s " % p819)
    else:
        p819 = p819Data[0]
# 查出来患者手术记录进修医师
cursor.execute("SELECT JSON_EXTRACT(CONTENT,'$.homePage.p435') FROM DA_MEDICAL_RECORD where ID=%.2f" % each)
p435Data = cursor.fetchone()
if p435Data != None:
    if p435Data[0] != None and p435Data[0] != '——' and p435Data[0] != '-':
        p435 = eval(p435Data[0])
        print("需要替换的手术记录进修医师: %s " % p435)
    else:
        p435 = p435Data[0]
# 查出来患者手术记录实习医师
cursor.execute("SELECT JSON_EXTRACT(CONTENT,'$.homePage.p437') FROM DA_MEDICAL_RECORD where ID=%.2f" % each)
p437Data = cursor.fetchone()
if p437Data != None:
    if p437Data[0] != None and p437Data[0] != '——' and p437Data[0] != '-':
        p437 = eval(p437Data[0])
        print("需要替换的手术记录实习医师: %s " % p437)
    else:
        p437 = p437Data[0]
# 查出来患者手术记录手术编码员
cursor.execute("SELECT JSON_EXTRACT(CONTENT,'$.homePage.p438') FROM DA_MEDICAL_RECORD where ID=%.2f" % each)
p438Data = cursor.fetchone()
if p438Data != None:
    if p438Data[0] != None and p438Data[0] != '——' and p438Data[0] != '-':
        p438 = eval(p438Data[0])
        print("需要替换的手术记录手术编码员: %s " % p438)
    else:
        p438 = p438Data[0]
# 查出来患者麻醉师
cursor.execute("SELECT JSON_EXTRACT(CONTENT,'$.homePage.p4910') FROM DA_MEDICAL_RECORD where ID=%.2f" % each)
p4910Data = cursor.fetchone()
if p4910Data != None:
    if p4910Data[0] != None and p4910Data[0] != '——' and p4910Data[0] != '-':
        p4910 = eval(p4910Data[0])
        print("需要替换的麻醉师: %s " % p4910)
    else:
        p4910 = p4910Data[0]
# 查出来医疗机构
cursor.execute("SELECT JSON_EXTRACT(CONTENT,'$.homePage.p6891') FROM DA_MEDICAL_RECORD where ID=%.2f" % each)
p6891Data = cursor.fetchone()
if p6891Data != None:
    if p6891Data[0] != None and p6891Data[0] != '——' and p6891Data[0] != '-':
        p6891 = eval(p6891Data[0])
        print("需要替换的麻醉师: %s " % p6891)
    else:
        p6891 = p6891Data[0]

# 使用 execute() 方法执行 SQL 查询
cursor.execute("SELECT CONTENT FROM DA_MEDICAL_RECORD where ID=%.2f" % each)
# 使用 fetchone() 方法获取单条数据.
data = cursor.fetchone()
mydata = data[0]

if pname != None and pname != '——' and pname != '-' and is_Chinses(pname):
    mydata = mydata.replace(pname, "XXX")
if p13 != None and p13 != '——' and p13 != '-' and len(p13) > 6:
    mydata = mydata.replace(p13, "123xxxxxxxxxxxx45")
if p801 != None and p801 != '——' and p801 != '-' and is_Chinses(p801):
    mydata = mydata.replace(p801, "xxx省xx市xxx村xxx号")
if p100 != None and p100 != '——' and p100 != '-' and is_Chinses(p100):
    mydata = mydata.replace(p100, "xxx省xx市xxx村xxx号")
if p17 != None and p17 != '——' and p17 != '-' and is_Chinses(p17):
    mydata = mydata.replace(p17, "xxx省xx市xxx村xxx号")
if p802 != None and p802 != '——' and p802 != '-' and len(p802) > 6:
    mydata = mydata.replace(p802, "135xxxxx123")
if p14 != None and p14 != '——' and p14 != '-' and is_Chinses(p14):
    mydata = mydata.replace(p14, "xxx省xx市xxx村xxx号")
if p15 != None and p15 != '——' and p15 != '-' and is_Chinses(p15) and len(p15) > 6:
    mydata = mydata.replace(p15, "135xxxxx123")
if p18 != None and p18 != '——' and p18 != '-' and is_Chinses(p18):
    mydata = mydata.replace(p18, "xxx")
if p20 != None and p20 != '——' and p20 != '-' and is_Chinses(p20):
    mydata = mydata.replace(p20, "xxx省xx市xxx村xxx号")
if p21 != None and p21 != '——' and p21 != '-' and is_Chinses(p21):
    mydata = mydata.replace(p21, "135xxxxx123")
if p231 != None and p231 != '——' and p231 != '-' and is_Chinses(p231):
    mydata = mydata.replace(p231, "XXX病房")
if p261 != None and p261 != '——' and p261 != '-' and is_Chinses(p261):
    mydata = mydata.replace(p261, "XXX病房")
if p431 != None and p431 != '——' and p431 != '-' and is_Chinses(p431):
    mydata = mydata.replace(p431, "xxx")
if p432 != None and p432 != '——' and p432 != '-' and is_Chinses(p432):
    mydata = mydata.replace(p432, "xxx")
if p433 != None and p433 != '——' and p433 != '-' and is_Chinses(p433):
    mydata = mydata.replace(p433, "xxx")
if p434 != None and p434 != '——' and p434 != '-' and is_Chinses(p434):
    mydata = mydata.replace(p434, "xxx")
if p819 != None and p819 != '——' and p819 != '-' and is_Chinses(p819):
    mydata = mydata.replace(p819, "xxx")
if p435 != None and p435 != '——' and p435 != '-' and is_Chinses(p435):
    mydata = mydata.replace(p435, "xxx")
if p437 != None and p437 != '——' and p437 != '-' and is_Chinses(p437):
    mydata = mydata.replace(p437, "xxx")
if p438 != None and p438 != '——' and p438 != '-' and is_Chinses(p438):
    mydata = mydata.replace(p438, "xxx")
if p4910 != None and p4910 != '——' and p4910 != '-' and is_Chinses(p4910):
    mydata = mydata.replace(p4910, "xxx")
if p6891 != None and p6891 != '——' and p6891 != '-' and is_Chinses(p6891):
    mydata = mydata.replace(p6891, "xxx医院")
# count = 0
# while True:
# try:
# findindex = mydata.index("\"signature\": \"", count)
# findNextMark = mydata.index("\"", findindex+14)
#
# # print(mydata[findindex+14:findNextMark])
# if mydata[findindex + 14:findNextMark] != None and mydata[findindex + 14:findNextMark] != '——'and mydata[findindex + 14:findNextMark]!='-' :
# mydata = mydata.replace(mydata[findindex + 14:findNextMark], "xxx")
# count=count+1
# except ValueError:
# print("木有找到查询")
# print ("查询"+str(count)+"次")
# break

print("替换完的json: %s " % mydata)
updatesql = "UPDATE DA_MEDICAL_RECORD SET CONTENT = '{0}' WHERE ID={1} "
if mydata != None:
    sql = updatesql.format(pymysql.escape_string(mydata), each)
cursor.execute(sql)
print("最后执行的sql： %s " % sql)

db1.commit()
# print("最后执行的sql： %s " % sql)

# 关闭数据库连接
cursor.close()
db1.close()
