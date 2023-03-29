from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.shortcuts import render, redirect
from admin_berry.forms import LoginForm, RegistrationForm, UserPasswordResetForm, UserSetPasswordForm, UserPasswordChangeForm
from django.contrib.auth import logout

from django.contrib.auth import views as auth_views

# Create your views here.

def index(request):
  return render(request, 'pages/index.html')


def payment_request(request):
    return render(request, 'pages/payment_requests/payment_requests.html')


def typography(request):
  return render(request, 'pages/typography.html')

def color(request):
  return render(request, 'pages/color.html')

def icon_tabler(request):
  return render(request, 'pages/icon-tabler.html')

def sample_page(request):
  return render(request, 'pages/sample-page.html')


# Authentication
def registration(request):
  if request.method == 'POST':
    form = RegistrationForm(request.POST)
    if form.is_valid():
      form.save()
      print('Account created successfully!')
      return redirect('/accounts/login/')
    else:
      print("Registration failed!")
  else:
    form = RegistrationForm()
  
  context = {'form': form}
  return render(request, 'accounts/register.html', context)

class UserLoginView(auth_views.LoginView):
  template_name = 'accounts/login.html'
  form_class = LoginForm
  success_url = '/'

class UserPasswordResetView(auth_views.PasswordResetView):
  template_name = 'accounts/password_reset.html'
  form_class = UserPasswordResetForm

class UserPasswordResetConfirmView(auth_views.PasswordResetConfirmView):
  template_name = 'accounts/password_reset_confirm.html'
  form_class = UserSetPasswordForm

class UserPasswordChangeView(auth_views.PasswordChangeView):
  template_name = 'accounts/password_change.html'
  form_class = UserPasswordChangeForm

def user_logout_view(request):
  logout(request)
  return redirect('/accounts/login/')
    

# purchase request
def purchase_request(request):
    form = PuchaseRequest.objects.all()
    context = {'form':form}
    return render(request, 'pages/purchase_requests/purchase_requests.html', context)

# comparative schedule
def comp_schedule(request):
    form = ComparativeSchedule.objects.all()
    context = {'form':form}
    return render(request, 'pages/comparative_schedules/comparative_schedules.html', context)

# payment request
def payment_request_all(request):
    form = PaymentRequest.objects.all()
    context = {'form':form}
    return render(request, 'pages/payment_request.html', context)


def payment_request(request):
    form = PaymentRequest.objects.all()
    context = {'form':form}
    return render(request, 'pages/payment_requests/payment_requests.html', context)

def payment_request_view(request):
    if request.method == "POST":
      _id = ""
      record = PaymentRequest.objects.filter(id==_id)
      context = {'record':record}
      return render(request, 'pages/payment_requests/view.html', context)



def payment_request_print(request):
    if request.method == "POST":
      _id = ""
      record = PaymentRequest.objects.filter(id==_id)
      context = {'record':record}
      return render(request, 'pages/payment_requests/view.html', context)

def payment_request_super(request):
    records = PaymentRequest.objects.all()
    context = {'records':records}
    return render(request, 'pages/payment_requests/list.html', context)


def payment_request_pending(request):
    form = PaymentRequest.objects.all()
    context = {'form':form}
    return render(request, 'pages/payment_request.html', context)

def payment_request_approved(request):
    form = PaymentRequest.objects.all()
    context = {'form':form}
    return render(request, 'pages/payment_request.html', context)

def payment_request_add(request):
    form = PaymentRequest.objects.all()
    context = {'form':form}
    return render(request, 'pages/payment_request.html', context)


#purchase request
def purchase_request_all(request):
    form = PaymentRequest.objects.all()
    context = {'form':form}
    return render(request, 'pages/payment_request.html', context)

def purchase_request_super(request):
    form = PaymentRequest.objects.all()
    context = {'form':form}
    return render(request, 'pages/payment_request.html', context)

def purchase_request_pending(request):
    form = PaymentRequest.objects.all()
    context = {'form':form}
    return render(request, 'pages/payment_request.html', context)

def purchase_request_approved(request):
    form = PaymentRequest.objects.all()
    context = {'form':form}
    return render(request, 'pages/payment_request.html', context)

def purchase_request_add(request):
    form = PaymentRequest.objects.all()
    context = {'form':form}
    return render(request, 'pages/payment_requests/add.html', context)


#comp schedule

def comp_schedule_all(request):
    form = PaymentRequest.objects.all()
    context = {'form':form}
    return render(request, 'pages/payment_request.html', context)

def comp_schedule_super(request):
    form = PaymentRequest.objects.all()
    context = {'form':form}
    return render(request, 'pages/payment_request.html', context)

def comp_schedule_pending(request):
    form = PaymentRequest.objects.all()
    context = {'form':form}
    return render(request, 'pages/payment_request.html', context)

def comp_schedule_approved(request):
    form = PaymentRequest.objects.all()
    context = {'form':form}
    return render(request, 'pages/payment_request.html', context)



def comp_schedule_add(request):
    form = PaymentRequest.objects.all()
    context = {'form':form}
    return render(request, 'pages/comparative_schedules/add.html', context)