from django.shortcuts import render
from django.http import HttpResponse

from .models import Tutorial,AccountPage,CoursePage

# Create your views here.

def programming(request):

    return render(request=request,
    template_name='Tutorials/index.html',
    context={'course':CoursePage.objects.all})



    
def accountpage(request):

    return render(request=request,
    template_name='Tutorials/newFolder/index_tempo.html',
    context={'account':AccountPage.objects.all})


    



