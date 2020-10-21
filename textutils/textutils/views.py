# self created file

from django.http import HttpResponse  # added by me
from django.shortcuts import render
# from .models import *
# from datetime import date
# from .resources import *
# import django
# django.setup()




def index(request):  # http://127.0.0.1:8000/
    return render(request, 'index.html')


def analyse(request):  # http://127.0.0.1:8000/
    djtext=request.POST.get('text', 'default')
    print(djtext)
    spaceremove = request.POST.get('spaceremove', 'off')
    newlineremove = request.POST.get('newlineremove', 'off')
    capfirst = request.POST.get('capfirst', 'off')
    charcount = request.POST.get('charcount', 'off')
    removepunc = request.POST.get('removepunc', 'off')
    print(spaceremove)


    if (capfirst == "on"):
        analysed = ""
        for char in djtext:
            analysed = analysed + char.upper()

        params = {'purpose': 'Changed to Uppercase', 'analysed_text': analysed}
        djtext=analysed
        # Analyze the text
        #return render(request, 'analyse.html', params)

    if (spaceremove == "on"):
        analysed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analysed = analysed + char

        params = {'purpose': 'Removed NewLines', 'analysed_text': analysed}
        djtext = analysed
        # Analyze the text
       #return render(request, 'analyse.html', params)

    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analysed = ""
        for char in djtext:
            if char not in punctuations:
                analysed = analysed + char

        params = {'purpose':'Removed Punctuations', 'analysed_text': analysed}
        djtext = analysed
        # return render(request, 'analyse.html', params)
    if (newlineremove == "on"):
        analysed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analysed = analysed + char

        params = {'purpose': 'Removed NewLines', 'analysed_text': analysed}
        djtext = analysed
        # Analyze the text
        #return render(request, 'analyse.html', params)
    if (charcount == "on"):
        analysed=len(djtext)
        params={'purpose':'Character count','analysed_text':analysed}
    if (charcount != "on" and spaceremove!= "on" and newlineremove != "on" and removepunc != "on" and capfirst != "on"):
        return HttpResponse("Error")
    return render(request, 'analyse.html', params)



def capfirst(request):  # http://127.0.0.1:8000/about
    return HttpResponse('''<h1>capfirst</h1> 
     <a href="http://127.0.0.1:8000"> 
    home
    </a>
    <br>
    <a href="http://127.0.0.1:8000/spaceremove"> 
    spaceremove
    </a>
       <br> 
    <a href="http://127.0.0.1:8000/charcount"> 
    charcount
    </a>
       <br> 
       <a href="http://127.0.0.1:8000/newlineremove"> 
    newlineremover
    </a>
       <br> 
   
        ''')


def spaceremove(request):  # http://127.0.0.1:8000/about
    print(request.POST.POST('text', 'default'))
    return HttpResponse('''<h1>spaceremove</h1>
     <br> 
     <a href="http://127.0.0.1:8000"> 
    home
    </a>
       <br> 
    <a href="http://127.0.0.1:8000/charcount"> 
    charcount
    </a>
       <br> 
       <a href="http://127.0.0.1:8000/newlineremove"> 
    newlineremover
    </a>
       <br> 
    <a href="http://127.0.0.1:8000/capfirst"> 
    capfirst
    </a>
      ''')


def newlineremove(request):  # http://127.0.0.1:8000/about
    return HttpResponse('''<h1>spaceremove</h1>
    <a href="http://127.0.0.1:8000"> 
    home
    </a>
       <br> 
    <br> 
     <a href="http://127.0.0.1:8000/spaceremove"> 
    spaceremove
    </a>
       <br> 
    <a href="http://127.0.0.1:8000/charcount"> 
    charcount
    </a>
       <br> 
       
    <a href="http://127.0.0.1:8000/capfirst"> 
    capfirst
    </a>
       ''')


def charcount(request):  # http://127.0.0.1:8000/about
    return HttpResponse(
        '''<h1>charcount</h1>
        <a href="http://127.0.0.1:8000"> 
    home
    </a>
    <br>
            <a href="http://127.0.0.1:8000/spaceremove"> 
    spaceremove
    </a>
       <br> 
       <a href="http://127.0.0.1:8000/newlineremove"> 
    newlineremover
    </a>
       <br> 
    <a href="http://127.0.0.1:8000/capfirst"> 
    capfirst
    </a>
               '''
    )
