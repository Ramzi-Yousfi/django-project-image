from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name='books'),
    path('two',views.two,name='two'),
]
