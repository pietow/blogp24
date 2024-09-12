
from django.http import HttpResponseRedirect
from django.urls import resolve, reverse

class SpecialUserMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        
        username = request.user.username
        # if username: 
        #     return HttpResponse(username)

        response = self.get_response(request)
        response.write('Hello from my Middleware')
        return response
        
class ProtectSpecificRoutesMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        protected_url_name = [
            'post_new',
            'post_edit',
            'post_delete',
        ]

        current_url_name = resolve(request.path_info).url_name

        if current_url_name in protected_url_name  \
            and not request.user.is_authenticated:
            return HttpResponseRedirect(reverse('login'))


        return self.get_response(request)


