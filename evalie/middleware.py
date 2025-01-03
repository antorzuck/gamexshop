from django.shortcuts import redirect
from django.utils.deprecation import MiddlewareMixin
from base.models import Profile
def currency_middleware(get_response):

    def middleware(request):
        currency = request.GET.get('currency')

        if currency:
            if not request.user.is_authenticated:
                return redirect('/signup') 
            else:
                profile = Profile.objects.get(user=request.user)
                if profile:
                    profile.currency_choice = currency
                    profile.save()

        response = get_response(request)
        return response

    return middleware
