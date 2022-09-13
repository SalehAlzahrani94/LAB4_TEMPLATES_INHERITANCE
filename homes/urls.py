from django.urls import path
from . import views
app_name = "my_first_app" # app name 
urlpatterns = [# list to use all views 
path("today/", views.today, name="path"),
path("random/password/", views.pas, name="path"),
path("favs/books/", views.books, name="path"),
path("botstrap", views.Bootstrap, name="path"),
path("index/",views.start, name="path")

]