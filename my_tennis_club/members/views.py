                         #ARTICLE 1

# from django.shortcuts import render
# from django.http import HttpResponse

# # def Grettings(request):
# #     return HttpResponse("Hello world!")
def welcome( request):
   x= "Welcome in new django!"
   return HttpResponse(x)
   
                        #ARTICLE 2
from django.http import HttpResponse
from django.template import loader

def members(request):
  template = loader.get_template('myfirst.html')
  return HttpResponse(template.render())