
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def login(request):
    # template = loader.get_template('/templates/login/index.html')
    # return HttpResponse(template.render())
    return render_to_response("login/index.html")