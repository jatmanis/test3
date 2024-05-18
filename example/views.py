# example/views.py
from datetime import datetime
from django.shortcuts import render , HttpResponse, HttpResponseRedirect
from django.template import loader
from django.http import HttpResponse

def index(request):
    now = datetime.now()
    html = f'''
    <html>
        <body>
            <h1>Hello from Mjcreations!</h1>
            <p>The current time is india { now }.</p>
        </body>
    </html>
    '''
    return HttpResponse(html)
def index1(request):
    now = datetime.now()
    html = f'''
    <html>
        <body>
            <h1>Hello from jatmanis1!</h1>
            <p>The current time is { now }.</p>
        </body>
    </html>
    '''
    return HttpResponse(html)

def homeg(request):
    return render(request, "index.html")
