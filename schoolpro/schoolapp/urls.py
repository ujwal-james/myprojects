from . import views
from django.urls import path

urlpatterns = [
    path('',views.home,name='home'),
    # path('math/',views.result,name='result')
]