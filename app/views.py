from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import RegistrationForm, LoginForm
from django.contrib import messages
from django.views.generic.base import TemplateView # new
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .models import EnergyConsumption
from .forms import EnergyConsumptionForm
import plotly.express as px
import plotly.io as pio
from django.shortcuts import render
import json
from .models import EnergyConsumption
from django.views.generic.edit import UpdateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView



def register(request):
    if request.method == 'POST':               # if form is submitted
        form = RegistrationForm(request.POST)  # create form
        if form.is_valid():                   
            user = form.save(commit=False)     
            password = form.cleaned_data['password']  
            user.set_password(password)             
            user.save()                              
            messages.success(request, 'Account created successfully') 
            # login(request, user)                      
            return redirect('login')                   
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
                return redirect('home')  
            else:
                form.add_error(None, f'Failed to authenticate user: {username}')
    else:                                
        form = LoginForm()               
    return render(request, 'users/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('home') 

class EnergyConsumptionListView(ListView):
    model = EnergyConsumption
    template_name = 'energy_list.html'
    context_object_name = 'energy_records'


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

def create_pie_chart(request):
    # Retrieve data from the "EnergyConsumption" model
    data = EnergyConsumption.objects.all()

    # Process the data and create a list of categories and values
    categories = [entry.month for entry in data]
    values = [entry.total_kwh for entry in data]

    # Create a DataFrame for the pie chart
    pie_chart_data = {'Category': categories, 'Values': values}

    # Create a pie chart using Plotly
    fig = px.pie(pie_chart_data, names='Category', values='Values', title='Pie Chart Example')

    # Convert the chart to JSON using plotly.io.to_json
    chart_data = pio.to_json(fig)

    return render(request, 'pie_chart.html', {'chart_data': chart_data})

