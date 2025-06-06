from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def register(request):
    if request.method == "POST":
        data = json.loads(request.body.decode('utf-8'))
        first_name = data.get('firstName')
        last_name = data.get('lastName')
        email = data.get('email')
        password = data.get('password')
        phone = data.get('phone')  # You may want to store this in a custom user profile

        if not (first_name and last_name and email and password and phone):
            return JsonResponse({'success': False, 'message': 'All fields are required.'})

        if User.objects.filter(email=email).exists():
            return JsonResponse({'success': False, 'message': 'Email is already registered.'})

        username = email  # can use email as username for simplicity
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
        )
        user.save()
        return JsonResponse({'success': True, 'message': 'Registration successful!'})
    else:
        return JsonResponse({'success': False, 'message': 'Invalid request method.'})