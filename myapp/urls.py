from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.index, name='submit_form'),
    path('submissions/', views.display_submissions, name='display_submissions'),
]
