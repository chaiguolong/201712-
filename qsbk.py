#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import requests
import sys
from bs4 import BeautifulSoup as bs

#检查url是否为有效链接


#读取html页面
def getHtml(parm):
    Headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
    url='https://www.qiushibaike.com/hot/page/'+str(parm)
    reponse=requests.get(url,headers=Headers)
    html=reponse.text #读取服务器响应的内容,可通过reponse.encoding指定编码格式
    return html

#解析html页面
def parseHtml(parm):
    html=getHtml(parm)
    soup = bs(html,"html.parser") #新建BeautifulSoup对象
    
    #soup.find_all("p", "title")
    #[<p class="title"><b>The Dormouse's story</b></p>]
    cont=soup.find_all('div','content')
    #print(soup.find_all('div','content'))
   
    items=[]
    for x in cont:
        #get_text()方法：用来获取标签里面的文本内容，在括号里面加"strip=True"可以去除文本前后多余的空格
        items.append(x.get_text(strip=True))
    #print(items)
    return items

#按任意键逐条打印段子
def getAll(parm):
    num=0
    for x in parseHtml(parm):
        num += 1
        print("第%d页第%d条：\n%s\n" %(parm,num,x))
        
        #按任意键继续，python2中为raw_input
        if input("按回车键继续阅读下个段子..."):
            pass
    parm+=1
    getAll(parm)
    
    
if __name__ == '__main__':
    getAll(1)
    

