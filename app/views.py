from django.shortcuts import render
from .models import *
import datetime
# Create your views here.
def index(request):

    expertis=expertise.objects.all()
    pers=personal.objects.last()
    year=datetime.date.today().year
    webinfoss=webinfo.objects.last()
    
    context={
        'expertis':expertis,
        'services':Services.objects.all(),
        'projects':Projects.objects.all(),
        'pers':pers,
        'year':str(year),
        'webinfoss':webinfoss
        
    }


    return render(request, 'app/index.html',context=context)