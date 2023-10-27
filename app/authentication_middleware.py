from django.http import HttpResponseRedirect
from django.urls import reverse
from .views import register, user_login


class AuthenticationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        
        if not request.user.is_authenticated and request.path != reverse('login') and request.path != reverse('register'):
            return HttpResponseRedirect(reverse('login'))  
                
        response = self.get_response(request)
        return response