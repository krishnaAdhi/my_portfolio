from django.urls import path, include
from myy_app import views
 
urlpatterns = [
    path('', views.myy_app, name="myy_app"),
    path('pdf/', views.gen_pdf, name='pdf'),
    
]