#!/usr/bin/env python
# -*- coding:utf8 -*-

import urllib2
import re


class Spider:
    def __init__(self):
        # 初始化其实位置
        self.page = 1
        # 爬取开关，如果为true,继续爬取
        self.enable = True
    """
        内涵段子爬虫类
    """

    def loadPage(self, page):
        """
            @brief 定义一个url请求网页的方法
            @param page 需要请求的第一页
            @returns 返回页面html
        """

        url = "http://www.neihanshequ.com/bar/" + str(page) + "/"

        # User-Agent头
        user_agent = 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT \
        6.1; Trident/5.0'

        headers = {'User-Agent': user_agent}
        req = urllib2.Request(url, headers=headers)
        response = urllib2.urlopen(req)
        html = response.read()

        # <h1 class="title">
        # 找到所有段子内容<div class="upload-txt  no-mb"></div>
        # re.S 如果没有re.S 则只匹配一行有没有符合规则的字符串，如果没有则
        # 下一行重新匹配
        # 如果加上re.S则是将所有的字符串将一个整体进行匹配
        # pattern = re.compile(r'<div.*?class="upload-txt  no-mb">(.*?)</div>', re.S)
        pattern = re.compile(r'<h1.*?class="title">(.*?)</h1>', re.S)
        item_list = pattern.findall(html)

        return item_list

    def printOnePage(self, item_list, page):
        """
            @brief 处理得到的段子
            @param item_list 得到的段子列表
            @param page 处理第几页
        """
        print "******** 第%d页 爬去完毕.....*******" % page
        for item in item_list:
            item = item.replace("<p>", "").replace("</p>", "")
            self.writeToFile(item)

    def writeToFile(self, text):
        """"
            @brief 将数据追加写进文件中
            @param text文件内容
        """

        myFile = open("./duanzi.txt", 'a')  # 追加形式打开文件
        myFile.write(text)
        myFile.write("----------------------------")
        myFile.close()

    def doWork(self):
        """
            让爬虫开始工作
        """


        while self.enable:
            try:
                item_list = self.loadPage(self.page)
            except urllib2.URLError, e:
                print e.reason
                continue

            # 对得到的段子item_list处理
            self.printOnePage(item_list, self.page)
            self.page += 1 # 此页处理完毕，处理下一页
            print "按回车继续..."
            print "输入quit退出"
            command = raw_input()
            if (command == "quit"):
                self.enable = False
                break


if __name__ == '__main__':
    """
        ============================
               内涵段子小爬虫
        ============================
    """

    print "请按下回车开始"
    raw_input()

    # 定义一个Spider()
    mySpider = Spider()
    mySpider.doWork()
