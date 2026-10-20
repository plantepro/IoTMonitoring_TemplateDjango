from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.sensor_create, name='sensor_create'),
    path('<int:sensor_id>/', views.sensor_detail, name='sensor_detail'), #<int:sensor_id> 表示从 URL 中获取一个整数，并把它传递给 sensor_detail()。
]