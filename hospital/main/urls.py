from django.urls import path
from .views import detail, index


urlpatterns = [
    path('', index, name='index'),
    path('detail/<int:pk>', detail, name='detail')
    
]