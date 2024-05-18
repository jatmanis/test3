from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render , HttpResponse, HttpResponseRedirect
from django.template import loader


def page(request):
    now = datetime.now()
    html = f'''
    <html>
        <body>
            <h1>Hello from page</h1>
            <p>The current time is { now }.</p>
        </body>
    </html>
    '''
    return HttpResponse(html)
def pages(request):
    return render(request, "index.html")
def even_odd(request):
    fn=""
    n=""
    try:
        if request.method=="POST":
            n=(request.POST.get("n"))
            #print(n)
            #print(type(n))
            n=int(n)
            if (n%2)==0:
               fn= "EVEN number"
            elif (n%2==1):
                fn="ODD number"
            else:
                fn ="not intiger"
    except:
        fn ="INVALIDs  "
    data={
        "fn":fn,
        "n":n
    }
    #print(fn)
    return render(request , "index.html", data)
 
def test(request):
    return render(request,"test.html")
