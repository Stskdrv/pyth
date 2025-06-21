from django.shortcuts import render

def index(request):
    #main page
    return render(request, 'learning_logs/index.html')