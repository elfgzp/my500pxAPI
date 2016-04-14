#encoding:utf-8
from lxml import etree
import requests
from django.http import HttpResponse
from django.shortcuts import render
import requests
import sys

reload(sys)
sys.setdefaultencoding('utf-8')



# Create your views here.

def index(request,photo,id):
    url = "http://500px.com/"+photo+"/"+id
    html = requests.get(url)
    selector = etree.HTML(html.text)
    imageUrl = selector.xpath('/html/head/meta[@property="og:image"]/@content')  # imageUrl类型为list
    if len(imageUrl):
        return HttpResponse(imageUrl[0])
    else:
        return HttpResponse("")