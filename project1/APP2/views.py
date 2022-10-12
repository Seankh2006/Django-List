from audioop import reverse
from cProfile import label
import datetime
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django import forms
from django.urls import reverse


# Create your views here.
def file2(request):
    return HttpResponse("Hello")

def file4(request):
    return HttpResponse("<h1 style=\"color:blue; background-color:black\">Welcome to the page<h1/>")

def file5(request):
    return render(request, "page1.html")

def greet(request, name):
    return render(request, "halo/greet.html", {
        "name1": name.capitalize()
    })

def date(request):
    date1 = datetime.datetime.now()
    return render(request, "page2.html", {
        "mybirthday": date1.month == 10 and date1.day == 5
    })

food = ["egg", "rice", "vegetables"]

def list(request):
    return render(request, "page3.html", {"list1": food})

class newform(forms.Form): 
    input1 = forms.CharField(label = "enter the item")
    # input2 = forms.IntegerField(label = "enter the number")


def form(request):
    if request.method == "POST":
        form1 = newform(request.POST)
        if form1.is_valid():
            mylist = form1.cleaned_data["input1"]
            food.append(mylist)
            return HttpResponseRedirect(reverse("forms1"))
        else:
            return render(request, "page4.html", {"list1":food})

    return render(request, "page4.html", {
        "myform": newform(),
        "list1": food
        })