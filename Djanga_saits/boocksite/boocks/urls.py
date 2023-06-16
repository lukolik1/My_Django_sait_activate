from django.urls import path
from .views import *

urlpatterns = [
    
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('addpage/', addpage, name='add_page'),
    path('contact/', contact, name='contact'),
    path('login/', login, name='login'),
    path('Boocks/<int:boocks_id>/', Show_Boocks, name='Boocks'),
    path('category/<int:cat_id>/', Show_category, name='category'),
    
    
]