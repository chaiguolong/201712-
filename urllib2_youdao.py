# coding=utf-8
import urllib
import urllib2

# post请求的目标URL
url = "http://fanyi.youdao.com/translate?\
    smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null"

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}

formdata = {
    "type": "AUTO",
    "i": "我爱你",
    "doctype": "json",
    "xmlVersion": "1.8",
    "keyfrom": "fanyi.web",
    "ue": "UTF-8",
    "action": "FY_BY_ENTER",
    "typoResult": "true"
}

data = urllib.urlencode(formdata)

request = urllib2.Request(url, data=data, headers=headers)
response = urllib2.urlopen(request)
print response.read()
