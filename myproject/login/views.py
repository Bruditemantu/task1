from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
weakday=["Monday","Tuesday","Wednesday","Friday"]

# links={"google":"https://www.google.com/","facebook":"https://www.facebook.com/","instagram":"https://www.instagram.com/"}
data = {'item':{'key1':'value' ,'key2':'value2' ,'key3':'value3'}}
def hello_world(request):
    # return ({"message":"hello world"})
    return HttpResponse("<h1>Hello World</h>")


def nav_bar(request):
    # return render(request, "login/index.html",{"days":weakday},{"link":links})
    return render(request,"login/index.html",{"p":data})

def form_bar(request):
    return render(request,"login/form.html")


