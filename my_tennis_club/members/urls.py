from django.urls import path
from . import views
urlpatterns = [
#path('members/', views.Grettings),
path('members/', views.welcome),
path('members/', views.members),
 ]