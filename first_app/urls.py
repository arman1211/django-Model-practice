from django.urls import path
from . import views
urlpatterns = [
    
    path('', views.home,name="home"),
    path('form/', views.form, name='form'),
    path('delete/<int:id>', views.delete_user, name="delete_user"),
]