from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def analyze(request):
    djtxt = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('linerem', 'off')
    charCounter = request.POST.get('count', 'off')
    params = {}

    if djtxt is None :
        return HttpResponse('Please enter some text.')

    else :
        if removepunc == "on" :
            punc = '''!@#$%^&*()_+-=[]\;',./{}|:"<>?'''
            analyzed = ""
            removed_Punctuations = ""
            for char in djtxt:
                if char not in punc:
                    analyzed = analyzed + char
                else:
                    removed_Punctuations = removed_Punctuations + char 
            
            params = {'purpose': removed_Punctuations, 'analyzed_text': analyzed}
            djtxt = analyzed
        
        if fullcaps=="on":
            analyzed = ""
            for char in djtxt:
                analyzed = analyzed + char.upper()
            params = {'purpose': 'Changes to uppercase', 'analyzed_text': analyzed}
            djtxt = analyzed
        
        if newlineremover=="on":
            analyzed = ""
            for char in djtxt:
                if char !="\n" and char!="\r" :
                    analyzed = analyzed + char
            params = {'purpose': 'Removed New Lines', 'analyzed_text': analyzed}
            djtxt = analyzed
        
        if charCounter=="on":
            analyzed = len(djtxt)
            params = {'purpose': 'Counting total characters...', 'analyzed_text': analyzed}
            djtxt = analyzed
            

        return render(request, 'analyze.html', params)    

    if (removepunc!="on" and fullcaps!="on" and newlineremover!="on" and charCounter!="on") :
        return HttpResponse('Please select any operations.')