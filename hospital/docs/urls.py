from django.urls import path
from .import views


urlpatterns = [
    path('', views.index, name='index'),
    path('memorial.html', views.memorial, name='memorial'),
    path('olc.html', views.olc, name='olc'),
    path('desert.html', views.desert, name='desert'),
]
