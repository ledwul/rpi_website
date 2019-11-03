from django.urls import path

from . import views

app_name = "wakeuptime"
urlpatterns = [
    path('', views.index, name='index'),
    path('set/', views.set, name='set'),
]
