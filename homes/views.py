
from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
import datetime
from random import choice
import string
import random


def today(request):
    day=datetime.datetime.now()
    return render(request,"homes/today.html",{"day" : day})
def pas(request):
    random_password = "".join(random.choices(string.ascii_letters + string.digits, k=9))
    return render(request,"homes/pas.html",{"pas" : random_password})
def books(request):
    books=". The Outsiders , 5 AM clup"
    return render(request,"homes/book.html",{"book" : books})
def Bootstrap(request):
    books=". The Outsiders , 5 AM clup"
    return render(request,"homes/base.html",{"book" : books})
def start(request):
    n=". welcome to our web"
    return render(request,"homes/index.html",{"st" : n})