from django.urls import path
from .views import (
    HomePageView,
    register,
    user_login,
    user_logout,
    EnergyConsumptionListView,
    create_pie_chart,
    EnergyConsumptionUpdateView,
    EnergyConsumptionCreateView,
    EnergyConsumptionDetailView,  # Add this import
)

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('energy-list/', EnergyConsumptionListView.as_view(), name='energy-list'),
    path('pie-chart/', create_pie_chart, name='pie-chart'),
    path('update/<int:pk>/', EnergyConsumptionUpdateView.as_view(), name='energy-update'),
    path('create/', EnergyConsumptionCreateView.as_view(), name='energy-create'),
    path('detail/<int:pk>/', EnergyConsumptionDetailView.as_view(), name='energy-detail'),  # Add this URL pattern
]
