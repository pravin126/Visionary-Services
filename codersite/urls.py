from django.urls import path
from . import views 


urlpatterns =[
    path('',views.index,name="index"),
    path('index',views.index,name="index"),
    path('product',views.product,name="product"),

    path('about',views.about,name="about"),
    path('contact',views.contact_info,name="contact"),
    path('services',views.services,name="services"),
    
    
   
]