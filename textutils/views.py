# This file was created by Amey Naik
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request,'index.html',)
    # return HttpResponse("<h1>hello World</h1>")

def about(request):
    return HttpResponse("hello World About")

def analyze(request):
    # Getting the text
    djtext=request.POST.get('text','default')
    removepunc=request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    # Default value off ho jayegi
    # print(removepunc)
    # return HttpResponse("remove punc")
    if removepunc == "on":
        analyzed=""
        punctuations = ''',.!?;:'"()[]{}<>-_/\|@#$%^&*+=~'''
        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed+char
        params={'purpose':'Removed Punctuations','analyzed_text':analyzed}
        return render(request,'analyze.html',params)
    elif (fullcaps == "on"):
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper()
        params = {'purpose': 'Capitalize', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    else:
        return HttpResponse("Error")
def capfirst(request):
    return HttpResponse("capfirst")

def newlineremove(request):
    return HttpResponse("newlineremove")

def spaceremover(request):
    return HttpResponse("spaceremover")