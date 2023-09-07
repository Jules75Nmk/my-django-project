# from django.shortcuts import render

# # Create your views here.

# from django.shortcuts import render
# from django.http import HttpResponse

# def Hello_word_fun(request):
#     return HttpResponse("Hello guys, welcome in django frame work!")
from django.http import HttpResponse
from django.template import loader

def Hello_word_fun(request):
  template = loader.get_template('home.html')
  context = {
    'greeting': 2,
  }
  return HttpResponse(template.render(context, request)) 