from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.IndexView.as_view()),
    path('employee/',views.EmployeeListView.as_view()),
    path('areaemployee/',views.EmployeeAreaListView.as_view()),
]


