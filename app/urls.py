from django.urls import path
from .views import (
    register,
    user_login,
    user_logout,
    EnergyConsumptionListView,
    create_bar_chart,
    create_bar_chart_water,
    create_bar_chart_heating,
    create_bar_chart_attic,
    create_bar_chart_groundfloor,
    create_bar_chart_basement,
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
    path('bar-chart-heating/', create_bar_chart_heating, name='bar-chart-heating'), 
    path('bar-chart-groundfloor/', create_bar_chart_groundfloor, name='bar-chart-groundfloor'), 
    path('bar-chart-attic/', create_bar_chart_attic, name='bar-chart-attic'), 
    path('bar-chart-basement/', create_bar_chart_basement, name='bar-chart-basement'), 
    path("api/", EnergyAPIView.as_view(), name="energy-api"),
    path('api/<int:pk>/', DetailEnergyAPIView.as_view(), name='energy-api-detail'),

]
