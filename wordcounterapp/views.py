from django.shortcuts import render

def index(request):
    return render(request, 'index.html', {})

def counter(request):
    text = request.POST['text']
    words = len(text.split())
    char = len(text)
    return render(request, 'counter.html', {'word': words, 'char': char, 'text': text})