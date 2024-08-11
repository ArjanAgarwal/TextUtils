#i have created it

from django.http import HttpResponse
from django.shortcuts import render

# code for video 6
# def index(request):
#     return  HttpResponse('''<h1> Bhartiya Vastralaya </h1> <a href="https://www.instagram.com/bhartiyavastralayaetah/"> Clothes</a>''')
# def about (request):
#     return  HttpResponse("About BVS")

# code for video 7 & 8


# def analyze(request):
#     # get the text
#     djtext = request.GET.get('text','default') # return text written in text area in html
#     print(djtext)
#     # analyze the text
#     return HttpResponse("remove punc ")

# def capfirst(request):
#    return HttpResponse("capitalized first ")
# def newlineremove(request):
#    return HttpResponse("new line")
#
# def spaceremove(request):
#    return HttpResponse("spaceremove <a href='/'>back</a>")
#
# def charcount(request):
#    return HttpResponse("char count")


# code for video 9
# def index (request):
#    # params={'name':'harry','place':'Mars'}
#    return render(request,'index.html')


# code for video 10

def index (request):
    return render(request, 'index.html')
def analyze(request):
    # get the text
    djtext = request.POST.get('text','default') # return text written in text area in html

    # check checkbox values
    removepunc=request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    newlineremove=request.POST.get('newlineremove','off')
    extraspaceremover=request.POST.get('extraspaceremover','off')

    # check which checkbox is on
    if removepunc =="on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed=""
        for char in djtext:
           if char not in punctuations:
               analyzed = analyzed+char
        params={'purpose':'Remove punc','analyzed_text':analyzed}
        djtext=analyzed


    if fullcaps== "on":
        analyzed =""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        djtext = analyzed


    if newlineremove =="on":
        analyzed=""
        for char in djtext:
            if char !="\n" and char !="\r":
             analyzed = analyzed + char
        params = {'purpose': 'Remove new lines', 'analyzed_text': analyzed}
        djtext = analyzed


    if extraspaceremover == "on":
        analyzed = ""
        for index, char in enumerate( djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char
        params = {'purpose': 'Remove space', 'analyzed_text': analyzed}
        djtext = analyzed


    if( removepunc !="on" and fullcaps!= "on" and newlineremove !="on" and extraspaceremover != "on" ):
        return HttpResponse("Error")

    return render(request, 'analyze.html', params)
