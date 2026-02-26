from django.urls import path, include
from django.contrib import admin 
from .import views 

urlpatterns = [
    path('', views.Home.as_view(), name='home'), 
    path('about/', views.about, name='about'), 
    path('bakes/', views.BakeList.as_view(), name='bake-index'), 
    path('bakes/create/', views.BakeCreate.as_view(), name='bake-create'), 
    path('bakes/<int:pk>/', views.BakeDetail.as_view(), name='bake-detail'), 
    path('bakes/<int:pk>/update/', views.BakeUpdate.as_view(), name='bake-update'), 
    path('bakes/<int:pk>/delete/', views.BakeDelete.as_view(), name='bake-delete'), 
    path('bakes/<int:pk>/add-review/', views.add_review, name='add-review'), 
    path('admin/', admin.site.urls), 
    path('accounts/', include('django.contrib.auth.urls')), 
    path('accounts/signup/', views.signup, name='signup')
]