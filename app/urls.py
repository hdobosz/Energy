from django.urls import path
from .views import (
    register,
    user_login,
    user_logout,
    EnergyConsumptionListView,
    create_bar_chart,
    create_bar_chart_water,
    create_bar_chart_house,
    EnergyConsumptionUpdateView,
    EnergyConsumptionCreateView,
    EnergyConsumptionDetailView,  
    TemplateView,
    EnergyAPIView,
    DetailEnergyAPIView,
)

urlpatterns = [
 
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('', EnergyConsumptionListView.as_view(), name='energy-list'),
    path('<int:pk>/', EnergyConsumptionDetailView.as_view(), name='energy-detail'),
    path('create/', EnergyConsumptionCreateView.as_view(), name='energy-create'),
    path('<int:pk>/edit/', EnergyConsumptionUpdateView.as_view(), name='energy-update'),    
    path('bar-chart/', create_bar_chart, name='bar-chart'), 
    path('bar-chart-water/', create_bar_chart_water, name='bar-chart-water'), 
    path('bar-chart-house/', create_bar_chart_house, name='bar-chart-house'), 
    path("api/", EnergyAPIView.as_view(), name="energy-api"),
    path('api/<int:pk>/', DetailEnergyAPIView.as_view(), name='energy-api-detail'),

]
