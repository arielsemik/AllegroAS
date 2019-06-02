from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('singup/', views.sing_up, name='sing_up'),
    path('singup/submit/', views.submit, name='submit'),
    path('singin/', views.sing_in, name='sing_in'),
    path('singin/sing/', views.sing_in_function, name='sing_in_function'),

]
