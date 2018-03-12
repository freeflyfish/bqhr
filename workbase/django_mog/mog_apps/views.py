from django.shortcuts import render
import time

# Create your views here.


def index(req):
    current_data = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    return render(req, 'index.html', locals())


def chenk(req):
    current_data = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    return render(req, 'chenk_all.html', locals())