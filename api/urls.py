from django.urls import path
from drf_app.views import EmployeeAPI, RegisterAPI, LoginAPI


urlpatterns = [
    
    path('employee/', EmployeeAPI.as_view()),
    path('register/', RegisterAPI.as_view()),
    path('login/', LoginAPI.as_view())
]
