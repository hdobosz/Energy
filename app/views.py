from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import RegistrationForm, LoginForm
from django.contrib import messages
from django.views.generic.base import TemplateView 
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .models import EnergyConsumption, BuildingConsumption
import plotly.express as px
import plotly.io as pio
from django.shortcuts import render
import json
from .models import EnergyConsumption
from django.views.generic.edit import UpdateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .forms import EnergyConsumptionForm
import plotly.graph_objs as go 
from rest_framework.generics import *  #ListAPIView, RetrieveAPIView
from .serializers import EnergySerializer
from django.http import HttpResponseRedirect

def register(request):
    if request.method == 'POST':               
        form = RegistrationForm(request.POST)  
        if form.is_valid():                   
            user = form.save(commit=False)     
            password = form.cleaned_data['password']  
            user.set_password(password)             
            user.save()                              
            messages.success(request, 'Account created successfully') 
            # login(request, user)                      
            return redirect('energy-list')                   
    else:                                             
        form = RegistrationForm() # create form
    return render(request, 'users/register.html', {'form': form}) 


def user_login(request):
    if request.method == 'POST':      
        form = LoginForm(request.POST)  
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password) 
            if user is not None:          
                login(request, user)
                return redirect('energy-list')  
            else:
                form.add_error(None, f'Failed to authenticate user: {username}')
    else:                                
        form = LoginForm()               
    return render(request, 'users/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('energy-list') 


class EnergyConsumptionListView(ListView):
    model = EnergyConsumption
    template_name = 'energy_list.html'
    context_object_name = 'energy_records'
    queryset = EnergyConsumption.objects.all().order_by('month')


class EnergyConsumptionDetailView(DetailView):
    model = EnergyConsumption
    template_name = 'energy_detail.html'
    context_object_name = 'energy'
    

class EnergyConsumptionCreateView(CreateView):
    model = EnergyConsumption
    form_class = EnergyConsumptionForm
    template_name = 'energy_form.html' 
    success_url = reverse_lazy('energy-list') 

class EnergyConsumptionUpdateView(UpdateView):
    model = EnergyConsumption
    form_class = EnergyConsumptionForm
    template_name = 'energy_form.html' 
    context_object_name = 'energy'
    success_url = reverse_lazy('energy-list')

class EnergyAPIView(ListCreateAPIView):
    queryset = EnergyConsumption.objects.all()
    serializer_class = EnergySerializer

class DetailEnergyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = EnergyConsumption.objects.all()
    serializer_class = EnergySerializer


def create_bar_chart(request):
    data = BuildingConsumption.objects.all().order_by('year', 'month')
    chart_data = [['Year-Month', 'Total Consumption']]

    for entry in data:
        total_consumption = float(entry.total_consumption)  # Convert to float
        chart_data.append([f'{entry.year} - Month {entry.month}', total_consumption])

    return render(request, 'bar_chart.html', {'chart_data': chart_data})


def create_bar_chart_house(request):
    data = BuildingConsumption.objects.all().order_by('year', 'month')
    chart_data = [['Year-Month', 'Total House Consumption']]

    for entry in data:
        total_consumption = float(entry.house_consumption)  # Convert to float
        chart_data.append([f'{entry.year} - Month {entry.month}', total_consumption])

    return render(request, 'bar_chart_house.html', {'chart_data': chart_data})

def create_bar_chart_water(request):
    data = BuildingConsumption.objects.all().order_by('year', 'month')
    chart_data = [['Year-Month', 'Total Water Consumption']]

    for entry in data:
        total_consumption = float(entry.water_consumption)  # Convert to float
        chart_data.append([f'{entry.year} - Month {entry.month}', total_consumption])

    return render(request, 'bar_chart_water.html', {'chart_data': chart_data})

# class DataProcessor:
#     def __init__(self, year):
#         self.year = year
#     def process_data(self):
#         BuildingConsumption.objects.filter(year=self.year).delete()
#         sorted_energy_data = EnergyConsumption.objects.filter(year=self.year).order_by('month')[1:]
#         for data in sorted_energy_data:
#             month = data.month
#             try:
#                 data_current_month = EnergyConsumption.objects.get(year=self.year, month=month)
#                 data_previous_month = EnergyConsumption.objects.get(year=self.year, month=month - 1)
#                 result = data_current_month.total_kwh - data_previous_month.total_kwh

#             except EnergyConsumption.DoesNotExist:
#                 print(f'Data not found for year {self.year}, month {month}. Using default value.')
#                 result = 0
#             BuildingConsumption.objects.create(
#                 total_consumption=round(result),
#                 month=month,
#                 year=self.year
#             )
# processor = DataProcessor(year=2023)
# processor.process_data()

class DataProcessor:
    def __init__(self, year):
        self.year = year

    def process_data(self):
        BuildingConsumption.objects.filter(year=self.year).delete()
        sorted_energy_data = EnergyConsumption.objects.filter(year=self.year).order_by('month')[1:]
        for data in sorted_energy_data:
            month = data.month
            try:
                data_current_month = EnergyConsumption.objects.get(year=self.year, month=month)
                data_previous_month = EnergyConsumption.objects.get(year=self.year, month=month - 1)
                result = data_current_month.total_kwh - data_previous_month.total_kwh
                water_consumption = data_current_month.water_m3 - data_previous_month.water_m3
                house_consumption = data_current_month.total_kwh - data_current_month.heating_kwh - data_current_month.water_m3
                ground_floor_consumption = data_current_month.total_kwh - data_current_month.attic_kwh - data_current_month.basement_kwh
                attic_consumption = data_current_month.attic_kwh
                basement_consumption = data_current_month.basement_kwh
                heating_consumption = data_current_month.heating_kwh
            except EnergyConsumption.DoesNotExist:
                print(f'Data not found for year {self.year}, month {month}. Using default values.')
                result = 0
                # Set default values for additional consumption attributes
                water_consumption = 0
                house_consumption = 0
                ground_floor_consumption = 0
                attic_consumption = 0
                basement_consumption = 0
                heating_consumption = 0

            BuildingConsumption.objects.create(
                total_consumption=round(result),
                month=month,
                year=self.year,
                water_consumption=round(water_consumption),
                house_consumption=round(house_consumption),
                ground_floor_consumption=round(ground_floor_consumption),
                attic_consumption=round(attic_consumption),
                basement_consumption=round(basement_consumption),
                heating_consumption=round(heating_consumption)
            )

processor = DataProcessor(year=2023)
processor.process_data()
