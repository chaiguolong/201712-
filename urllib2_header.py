# coding=utf-8

import urllib2

url = "http://www.baidu.com"

# IE9.0的User-Agent
header = {"User-Agent" : "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;"}
request = urllib2.Request(url, headers = header)

# 也可以通过调用Request.add_header()添加/修改一个特定的header
request.add_header("Connection", "keep-alive")

# 也可以通过调用Request.get_header()来查看header信息
# get_head = request.get_head(header_name="Connection")
# print(request.get_header(header_name = "User-Agent"))

response = urllib2.urlopen(request)

print response.code
html = response.read()

print html
