from django.shortcuts import render
from bs4 import BeautifulSoup
from .forms import UrlForm
from . import page
from . import user
from . import domain
import time
import pprint
import random

def index(request):
    form = UrlForm()
    context={}
    url = False
    if request.method == 'POST':
        form = UrlForm(request.POST)
        url = request.POST['address']
        user.prompt(feed="______ "+str(url))
        #if len(str(request.POST['address'])) > 6 and 'htt' in str(request.POST['address']):
        if form.is_valid():
            context.update({'url_address':url})
            context.update({'score':random.randint(50,100)})
            
            form.save()
        else:
            user.prompt(feed="wrong format")
    if url:
        d = domain.Domain(request,url)
        context.update({'table':d.table})
    context.update({'form':form})
    return render(request,'main.html',context)
