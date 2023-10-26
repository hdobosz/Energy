from django.urls import path
from .views import (
    register,
    user_login,
    user_logout,
    EnergyConsumptionListView,
    create_pie_chart,
    EnergyConsumptionUpdateView,
    EnergyConsumptionCreateView,
    EnergyConsumptionDetailView,  
)

urlpatterns = [
 
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('', EnergyConsumptionListView.as_view(), name='energy-list'),
    path('<int:pk>/', EnergyConsumptionDetailView.as_view(), name='energy-detail'),
    path('create/', EnergyConsumptionCreateView.as_view(), name='energy-create'),
    path('<int:pk>/edit/', EnergyConsumptionUpdateView.as_view(), name='energy-update'),
       
    path('pie-chart/', create_pie_chart, name='pie-chart'), 
]
