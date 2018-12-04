from django.shortcuts import render
from bs4 import BeautifulSoup
from .forms import UrlForm
from . import page
from . import user
from . import domain
import time
import pprint
import random
import validators

def index(request):
    form = UrlForm()
    context={}
    url = False
    if request.method == 'POST':
        form = UrlForm(request.POST)
        url = request.POST['address']
        user.prompt(feed="url enetered: "+str(url))
        is_valid = is_valid_url(url)
        if is_valid:
            if form.is_valid():
                print("url: "+str(url))
                context.update({'url_address':url})
                context.update({'score':random.randint(50,100)})
                form.save()
            else:
                user.prompt(feed="wrong format")
            if url:
                d = domain.Domain(request,url)
                context.update({'table':d.post_table})
        else:
            context.update({'error_message':"invalid format"})
    context.update({'form':form})
    return render(request,'main.html',context)

def is_valid_url(url):
    print(validators.url(url))
    if not validators.url(url):
        return False
    return True
