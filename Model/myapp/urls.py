from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Định nghĩa view tại đây
]
