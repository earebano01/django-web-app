# ~/projects/django-web-app/merchex/listings/views.py

from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band

def hello(request):
    bands = Band.objects.all()
    # return render(request, 'listings/hello.html')
    return render(request, 
                  'listings/hello.html',
                  {'bands': bands})
    # albums = Band.objects.all()
#     return HttpResponse(f"""
#         <h1>Hello Django!</h1>
#         <p>Mes groupes préférés sont :<p>
#         <ul>
#             <li>{bands[0].name}</li>
#             <li>{bands[1].name}</li>
#             <li>{bands[2].name}</li>
#             <li>{bands[3].name}</li>
#             <li>{bands[4].name}</li>
#         </ul>
#         <p>Mes albums préférés sont :<p>
#         <ul>
#             <li>{bands[4].albums}</li>
#         </ul>
# """)

def about(request):
    return HttpResponse('<h1>À propos</h1> <p>Nous adorons merch !</p>')
