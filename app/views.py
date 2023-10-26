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

# def create_pie_chart(request):
#     # Retrieve data from the "EnergyConsumption" model
#     data = BuildingConsumption.objects.all().order_by('month')
#     print(data)
#     # Process the data and create a list of categories and values
#     categories = [entry.month for entry in data]
#     values = [entry.total_consumption for entry in data]

#     # Create a DataFrame for the pie chart
#     pie_chart_data = {'Category': categories, 'Values': values}

#     # Create a pie chart using Plotly
#     fig = px.pie(pie_chart_data, names='Category', values='Values', title='Pie Chart Example')

#     # Convert the chart to JSON using plotly.io.to_json
#     chart_data = pio.to_json(fig)
    
#     return render(request, 'pie_chart.html', {'chart_data': chart_data})

def create_pie_chart(request):
    # Retrieve data from the "BuildingConsumption" model and sort by month
    data = BuildingConsumption.objects.all().order_by('month')

    # Process the data and create lists for categories and values
    categories = [f'Month {entry.month}' for entry in data]
    values = [entry.total_consumption for entry in data]

    # Create a bar chart using Plotly
    fig = go.Figure(data=[go.Bar(x=categories, y=values)])

    # Set the layout for the bar chart
    fig.update_layout(title='Bar Chart Example', xaxis_title='Months', yaxis_title='Total Consumption')

    # Convert the chart to JSON using plotly.io.to_json
    chart_data = pio.to_json(fig)

    return render(request, 'pie_chart.html', {'chart_data': chart_data})

class DataProcessor:
    def __init__(self, year):
        self.year = year
    def process_data(self):
        BuildingConsumption.objects.filter(year=self.year).delete()
        sorted_energy_data = EnergyConsumption.objects.filter(year=self.year).order_by('month')  # Order by 'month'
        print(sorted_energy_data)
        for data in sorted_energy_data:
            month = data.month
            try:
                data_current_month = EnergyConsumption.objects.get(year=self.year, month=month)
                data_previous_month = EnergyConsumption.objects.get(year=self.year, month=month - 1)
                result = data_current_month.total_kwh - data_previous_month.total_kwh
            except EnergyConsumption.DoesNotExist:
                print(f'Data not found for year {self.year}, month {month}. Using default value.')
                result = 0
            BuildingConsumption.objects.create(
                total_consumption=round(result),
                month=month,
                year=self.year
            )
processor = DataProcessor(year=2023)
processor.process_data()
