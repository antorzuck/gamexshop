from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from base.models import Profile
from django.db import transaction
from django.contrib.auth.models import User



def signup_view(request):
    if request.method == 'POST':
        print("bai bai im running bai.........")
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirmPassword')
        currency = request.POST.get('currency')

        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect('/auth/signup') 

        if not currency:
            messages.error(request, "Please select a preferred currency.")
            return redirect('auth/signup')

        try:
            with transaction.atomic():
                user = User.objects.create_user(username=username, email=email, password=password)
                Profile.objects.create(user=user, currency_choice=currency)
                messages.success(request, "Account created successfully. Please log in.")
                return redirect('/auth/signup') 
        except Exception as e:
            messages.error(request, f"An error occurred: {e}")
            return redirect('/auth/signup')

    return render(request, 'signup.html')
