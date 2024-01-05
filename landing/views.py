from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.shortcuts import render, redirect
from admin_berry.forms import LoginForm, RegistrationForm, UserPasswordResetForm, UserSetPasswordForm, UserPasswordChangeForm
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from flask import Flask
import datetime
from django.db.models import Q
from django.contrib.auth import get_user_model
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
import qrcode






# Create your views here.

@login_required(login_url='login')
def app_root(request):
  username = request.user.username
#   notices = Notifications.objects.filter(to=username)

#   payments = PaymentRequest.objects.all().order_by('-id')[:5][:-1]
#   total_payments= 123455

#   context = {
#      "notices":notices,
#      "nots_num": notices.count(),
#      "payments": payments,
#      "total_payments":total_payments,

#   }

  return render(request, 'index.html', context={})
