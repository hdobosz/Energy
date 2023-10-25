from django.urls import path
from .views import register, user_login, user_logout, HomePageView, EnergyConsumptionCreateView, create_pie_chart

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('energy/', EnergyConsumptionCreateView.as_view(), name='energy'),
    path('pie-chart/', create_pie_chart, name='pie_chart'),
]

