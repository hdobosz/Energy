from django.urls import path
from .views import register, user_login, user_logout, HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
]

