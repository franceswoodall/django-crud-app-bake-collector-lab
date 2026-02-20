from django.urls import path 
from .import views 

urlpatterns = [
    path('', views.home, name='home'), 
    path('about/', views.about, name='about'), 
    path('bakes/', views.bakes_index, name='bakes-index'), 
    path('bakes/<int:bake_id>/', views.bake_detail, name='bake-detail'), 
]