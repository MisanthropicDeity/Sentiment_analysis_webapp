
from django.urls import path
from . import views

urlpatterns = [
	path('fform/', views.fform),
    path('', views.feed,name = 'index'),
    path('thank/', views.thank),
]
