#coding=utf8
import urllib
from urllib.request import urlopen 
import requests
import re

#url = "http://kimerfly.blogspot.com/2012/10/86-120g.html"
headers = {
    'user-agent': 'Mozilla/5.0'
}
proxies = {
    'https': 'https://127.0.0.1:1080',
    'http': 'http://127.0.0.1:1080'
}
response = requests.get(url, proxies=proxies)
text = response.text
pattern = re.compile(r'ed2k\:\/\/\|file\|.*\|\/')
cinfo = pattern.findall(text)

f = open("out.txt", "w")
for i in cinfo:
	f.write(str(i) + "\n")
