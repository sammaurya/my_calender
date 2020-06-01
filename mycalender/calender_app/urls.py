
from django.urls import path
from .views import get_calender

urlpatterns = [
    path('calender/<int:year>/<int:month>/',get_calender, name='calender'),
]