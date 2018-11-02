from django.shortcuts import render
import time
import requests
from bs4 import BeautifulSoup
from .forms import UrlForm

class Spider:
    def __init__(self,request):
        self.form = UrlForm(request.POST)
        self.table = self.get_table_data()
        self.context = {'form':self.form,'table':self.table}

    def get_table_data(self):
        #This will the dictionary contatining all the data scraped from the html document
        dictionary={'title':'This is a title','description':'This is a description'}
        return dictionary

def index(request):
    spider = Spider(request)
    return render(request,'main.html',spider.context)
