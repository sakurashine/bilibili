#coding:utf-8
import urllib
import urllib2
import re

page = "https://www.bilibili.com/"
headers = { 'User-Agent' : 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'}
request = urllib2.Request(page,headers=headers)
content = urllib2.urlopen(request).read()
pattern = re.compile(r'img src="(//i\d.hdslb.*?\.jpg)" alt')
links = re.findall(pattern,content)
i = 0
for link in links:
	url = "https:"+''.join(link)
	print url
	urllib.urlretrieve(url,'../img/home_card'+str(i)+'.jpg')
	i = i+1