from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.IndexView.as_view()),
    path('lista/', views.PruebaListView.as_view()),
#    path('prueba/',views.ModeloPruebaListView.as_view()),
]
