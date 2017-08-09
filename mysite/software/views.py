from django.shortcuts import render


def index(request):
    return render(request,'software/home.html')

def contact(request):
    return render(request ,'software/basic.html',{'content':['email : ankitk.singh@stniituniversity.in']})


