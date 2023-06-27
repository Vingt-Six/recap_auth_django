from django.shortcuts import redirect
from django.utils.deprecation import MiddlewareMixin

class Jtebloque(MiddlewareMixin):
    def __init__(self, get_response):
        self.get_response = get_response
    
    def process_view(self, request, view_func, view_args, view_kwargs):
        if request.path in ['/home/admin/', 'home/admin3/']:
            user = request.user
            if user.is_authenticated:
                if user.role.id == 1:
                    return None
                else: 
                    return redirect('home')
            else:
                return redirect('home')
