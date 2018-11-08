from django.shortcuts import render
from bs4 import BeautifulSoup
from .forms import UrlForm
from . import webbing
import time

class Spider:
    def __init__(self,request):
        self.form = UrlForm(request.POST)
        self.table = self.get_table_data()
        self.html = self.get_request(self.form['address'])
        self.context = {'form':self.form,'table':self.table}

    def get_table_data(self):
        #This will the dictionary contatining all the data scraped from the html document
        dictionary={'title':'This is a title','description':'This is a description'}
        return dictionary

    def get_request(self,url):
        num7=0

def index(request):
    spider = Spider(request)
    return render(request,'main.html',spider.context)
