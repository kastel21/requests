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

app = Flask(__name__)

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
    
# *************************************************************************************************************************
# purchase request
def purchase_request(request):
    form = PuchaseRequest.objects.all()
    context = {'form':form}
    return render(request, 'pages/purchase_requests/purchase_requests.html', context)

def purchase_request_all(request):
    records = PuchaseRequest.objects.all()
    context = {'records':records}
    return render(request, 'pages/purchase_requests/list.html', context)

def purchase_request_super(request):
    form = PuchaseRequest.objects.all()
    context = {'form':form}
    return render(request, 'pages/purchase_requests/list.html', context)

def purchase_request_pending(request):
    form = PuchaseRequest.objects.all()
    context = {'form':form}
    return render(request, 'pages/purchase_request.html', context)

def purchase_request_approved(request):
    form = PuchaseRequest.objects.all()
    context = {'form':form}
    return render(request, 'pages/purchase_request.html', context)

def purchase_request_add(request):
    form = PuchaseRequest.objects.all()
    context = {'form':form}
    return render(request, 'pages/purchase_requests/add.html', context)

@csrf_exempt
@app.route("/send_record")
def purchase_request_send_record(request):

    with app.app_context():
        try:
        
          request_id= request.POST.get('request_id',default=None)
          requester= request.POST.get('requester',default=None)
          date_of_request= request.POST.get('date_of_request',default=None)
          requesting_dpt= request.POST.get('requesting_dpt',default=None)

          request_justification= request.POST.get('request_justification',default=None) 
          name_address_of_supplier = request.POST.get('name_address_of_supplier',default=None)
          budget_line_item= request.POST.get('budget_line_item',default=None)

          qnty= request.POST.get('qnty',default=None)
          item_number= request.POST.get('item_number',default=None)

          description= request.POST.get('description',default=None)
          unit_price=  request.POST.get('unit_price',default=None)

          supervisor_approved= request.POST.get('supervisor_approved',default=None)
          supervisor_approved_date= request.POST.get('supervisor_approved_date',default=None)

          accounts_clerk_approved= request.POST.get('accounts_clerk_approved',default=None)
          accounts_clerk_approved_date= request.POST.get('accounts_clerk_approved_date',default=None)

          record = PuchaseRequest()

        #   record.compiled_by = request.user.username
          record.request_id= request_id
          record.requester= requester
          record.date_of_request= date_of_request
          record.requesting_dpt= requesting_dpt

          record.request_justification= request_justification 
          record.name_address_of_supplier = name_address_of_supplier
          record.budget_line_item= budget_line_item

          record.qnty= qnty
          record.item_number= item_number

          record.description= description
          record.unit_price= unit_price

          record.supervisor_approved= supervisor_approved
          record.supervisor_approved_date= supervisor_approved_date

          record.accounts_clerk_approved= accounts_clerk_approved
        #   d = datetime.datetime.now()
        #   record.date_of_request = "{:%B %d, %Y}".format(d)
          record.accounts_clerk_approved_date= accounts_clerk_approved_date

          record.save()

          return JsonResponse( {'message':"success"})

        except Exception as e  :
            f= open("service1.txt","w")
            f.write(str(e))
            f.close()
            print(str(e))
            return JsonResponse({'message':(str(e))})

def purchase_request_get_record(request):
    context={}
    if request.method == "POST":
        _id = request.POST.get('id',default=None)

        record = PuchaseRequest.objects.get(id=_id)
        dic = {
           
        "date_of_request": record.date_of_request,
          "payee": record.payee,
          "payment_type": record.payment_type,
          "amount": record.amount,
          "project_number": record.project_number,

          "account_code": record.account_code, 
          "details ": record.details,
          # // "amount ": record.pat_name,
          # "unit_price ": record.unit_price,
          "total": record.total,

          "certified_by": record.certified_by,
          "certified_by_date": record.certified_by_date,

          "cleared_by_fin_man": record.cleared_by_fin_man,
          "cleared_by_fin_man_date": record.cleared_by_fin_man_date,

          "approved_by_project_man": record.approved_by_project_man,
          "approved_by_project_man_date": record.approved_by_project_man_date,

          "approved_by": record.approved_by,
          "approved_by_date": record.approved_by_date,
          "message":"success",
        }
        context = {'addTabActive': True, "record":""}
        return JsonResponse(dic)
    else:
        return redirect('/payment_requests')
# ***********************************************************************************************************************


# comparative schedule
def comp_schedule(request):
    form = ComparativeSchedule.objects.all()
    context = {'form':form}
    return render(request, 'pages/comparative_schedules/comparative_schedules.html', context)

# payment request
def payment_request_all(request):
    username = request.user.username
    user_id = request.user.id
    records = PaymentRequest.objects.filter( Q(compiled_by=username) | Q(certified_by= username) | Q(approved_by=username))
    context = {'records':records}
    return render(request, 'pages/payment_requests/list.html', context)


def payment_request(request):
    form = PaymentRequest.objects.all()
    context = {'form':form}
    return render(request, 'pages/payment_requests/payment_requests.html', context)

def payment_request_view(request):
    if request.method == "POST":
      
      _id = request.POST.get('id',default=None)

        # objs = Record.objects.get(id=_id)
      record = PaymentRequest.objects.get(id=_id)
      context = {'record':record}
      return render(request, 'pages/payment_requests/view2.html', context)
    else:
      return render(request, 'pages/payment_requests/list.html', {})

def payment_request_print(request):
    if request.method == "POST":
      _id = ""
      record = PaymentRequest.objects.filter(id=_id)
      context = {'record':record}
      return render(request, 'pages/payment_requests/print.html', context)

def payment_request_super(request):
    records = PaymentRequest.objects.all()
    context = {'records':records}
    return render(request, 'pages/payment_requests/list.html', context)



def payment_request_edit(request):
    form = PaymentRequest.objects.all()
    context = {'form':form}
    return render(request, 'pages/payment_requests/add.html', context)

def payment_request_pending_certification(request):
    records = PaymentRequest.objects.filter(certified_by="None")
    context = {'records':records}
    return render(request, 'pages/payment_requests/list.html', context)


def payment_request_certification(request):
    if request.method == "POST":
      
      _id = request.POST.get('id',default=None)

        # objs = Record.objects.get(id=_id)
      record = PaymentRequest.objects.get(id=_id)
      context = {'record':record}
      return render(request, 'pages/payment_requests/view.html', context)
    else:
      return render(request, 'pages/payment_requests/list.html', {})

def payment_request_certify(request):
    if request.method == "POST":
      
      _id = request.POST.get('id',default=None)

        # objs = Record.objects.get(id=_id)
      record = PaymentRequest.objects.get(id=_id)
      record.certified_by = request.user.username
      # record.certified_by_date = request.user.username
      d = datetime.datetime.now()
          # record.date_of_request = "{:%B %d, %Y}".format(d)
      record.certified_by_date= "{:%B %d, %Y}".format(d)

      record.save()




      return JsonResponse( {'message':"success"})

    else:
      return render(request, 'pages/payment_requests/list.html', {})




def payment_request_pending_clearance(request):
    records = PaymentRequest.objects.filter(cleared_by_fin_man="None")
    context = {'records':records}
    return render(request, 'pages/payment_requests/list.html', context)




def payment_request_clearance(request):
    if request.method == "POST":
      
      _id = request.POST.get('id',default=None)

        # objs = Record.objects.get(id=_id)
      record = PaymentRequest.objects.get(id=_id)
      context = {'record':record}
      return render(request, 'pages/payment_requests/view.html', context)
    else:
      return render(request, 'pages/payment_requests/list.html', {})

def payment_request_clear(request):
    if request.method == "POST":
      
      _id = request.POST.get('id',default=None)

        # objs = Record.objects.get(id=_id)
      record = PaymentRequest.objects.get(id=_id)
      record.cleared_by_fin_man = request.user.username
      # record.certified_by_date = request.user.username
      d = datetime.datetime.now()
          # record.date_of_request = "{:%B %d, %Y}".format(d)
      record.cleared_by_fin_man_date= "{:%B %d, %Y}".format(d)

      record.save()




      return JsonResponse( {'message':"success"})

    else:
      return render(request, 'pages/payment_requests/list.html', {})




def payment_request_pending_approval(request):
    records = PaymentRequest.objects.filter(approved_by="None")
    context = {'records':records}
    return render(request, 'pages/payment_requests/list.html', context)



def payment_request_approval(request):
    if request.method == "POST":
      
      _id = request.POST.get('id',default=None)

        # objs = Record.objects.get(id=_id)
      record = PaymentRequest.objects.get(id=_id)
      context = {'record':record}
      return render(request, 'pages/payment_requests/view.html', context)
    else:
      return render(request, 'pages/payment_requests/list.html', {})

def payment_request_approve(request):
    if request.method == "POST":
      
      _id = request.POST.get('id',default=None)

        # objs = Record.objects.get(id=_id)
      record = PaymentRequest.objects.get(id=_id)
      record.approved_by = request.user.username
      # record.certified_by_date = request.user.username
      d = datetime.datetime.now()
          # record.date_of_request = "{:%B %d, %Y}".format(d)
      record.approved_by_date= "{:%B %d, %Y}".format(d)

      record.save()




      return JsonResponse( {'message':"success"})

    else:
      return render(request, 'pages/payment_requests/list.html', {})



def payment_request_pending(request):
    form = PaymentRequest.objects.all()
    context = {'form':form}
    return render(request, 'pages/payment_requests/list.html', context)



def payment_request_approved(request):
    form = PaymentRequest.objects.all()
    context = {'form':form}
    return render(request, 'pages/payment_request.html', context)

def payment_request_add(request):
    
    form = PaymentRequest.objects.all()
    context = {'form':form}
    return render(request, 'pages/payment_requests/add.html', context)



@csrf_exempt
def get_users(request):
   try:
      dic = {}
      User = get_user_model()
      users = User.objects.all()

      for user in users: 
          dic[user.username]= user.username
      return JsonResponse(dic)
   except Exception as e:
          return JsonResponse(str(e))

    


@csrf_exempt
def payment_request_get_record(request):
    context={}
    if request.method == "POST":
        _id = request.POST.get('id',default=None)

        record = PaymentRequest.objects.get(id=_id)
        dic = {
           
           "date_of_request": record.date_of_request,
          "payee": record.payee,
          "payment_type": record.payment_type,
          "amount": record.amount,
          "project_number": record.project_number,

          "account_code": record.account_code, 
          "details ": record.details,
          # // "amount ": record.pat_name,
          # "unit_price ": record.unit_price,
          "total": record.total,

          "certified_by": record.certified_by,
          "certified_by_date": record.certified_by_date,

          "cleared_by_fin_man": record.cleared_by_fin_man,
          "cleared_by_fin_man_date": record.cleared_by_fin_man_date,

          "approved_by_project_man": record.approved_by_project_man,
          "approved_by_project_man_date": record.approved_by_project_man_date,

          "approved_by": record.approved_by,
          "approved_by_date": record.approved_by_date,
          "message":"success",
        }
        context = {'addTabActive': True, "record":""}
        return JsonResponse(dic)
    else:
        return redirect('/payment_requests')



@csrf_exempt
@app.route("/send_record")
def payment_request_send_record(request):

    with app.app_context():
        try:
           

          payee= request.POST.get('payee',default=None)
          payment_type= request.POST.get('payment_type',default=None)
          amount= request.POST.get('amount',default=None)
          project_number= request.POST.get('project_number',default=None)

          account_code= request.POST.get('account_code',default=None) 
          details = request.POST.get('details',default=None)
          # // amount = request.POST.get('pat_name',default=None)
          # unit_price = request.POST.get('unit_price',default=None)
          total= request.POST.get('total',default=None)

          certified_by= request.POST.get('certified_by',default=None)
          # certified_by_date= request.POST.get('certified_by_date',default=None)

          # cleared_by_fin_man= request.POST.get('cleared_by_fin_man',default=None)
          # cleared_by_fin_man_date= request.POST.get('cleared_by_fin_man_date',default=None)

          # approved_by_project_man= request.POST.get('approved_by_project_man',default=None)
          # approved_by_project_man_date= request.POST.get('approved_by_project_man_date',default=None)

          # approved_by= request.POST.get('approved_by',default=None)
          # approved_by_date= request.POST.get('approved_by_date',default=None)












          record = PaymentRequest()

          record.compiled_by = request.user.username
          record.payee= payee
          record.payment_type= payment_type
          record.amount= amount
          record.project_number= project_number

          record.account_code= account_code 
          record.details = details
          # // record.amount = pat_name
          # record.unit_price = unit_price
          record.total= total

          record.certified_by= certified_by
          # record.certified_by_date= certified_by_date

          # record.cleared_by_fin_man= cleared_by_fin_man
          # record.cleared_by_fin_man_date= cleared_by_fin_man_date

          # record.approved_by_project_man= approved_by_project_man
          # record.approved_by_project_man_date= approved_by_project_man_date

          # record.approved_by= approved_by
          d = datetime.datetime.now()
          record.date_of_request = "{:%B %d, %Y}".format(d)
          # record.approved_by_date= approved_by_date

          record.save()




          return JsonResponse( {'message':"success"})

        except Exception as e  :
            f= open("service1.txt","w")
            f.write(str(e))
            f.close()
            return JsonResponse({'message':"failed"})






@csrf_exempt
def payment_request_edit_record(request):

        try:
           

          _id= request.POST.get('case_id',default=None)

          payee= request.POST.get('payee',default=None)
          payment_type= request.POST.get('payment_type',default=None)
          amount= request.POST.get('amount',default=None)
          project_number= request.POST.get('project_number',default=None)

          account_code= request.POST.get('account_code',default=None) 
          details = request.POST.get('details',default=None)
          # // amount = request.POST.get('pat_name',default=None)
          # unit_price = request.POST.get('unit_price',default=None)
          total= request.POST.get('total',default=None)

          certified_by= request.POST.get('certified_by',default=None)
          # certified_by_date= request.POST.get('certified_by_date',default=None)

          # cleared_by_fin_man= request.POST.get('cleared_by_fin_man',default=None)
          # cleared_by_fin_man_date= request.POST.get('cleared_by_fin_man_date',default=None)

          # approved_by_project_man= request.POST.get('approved_by_project_man',default=None)
          # approved_by_project_man_date= request.POST.get('approved_by_project_man_date',default=None)

          # approved_by= request.POST.get('approved_by',default=None)
          # approved_by_date= request.POST.get('approved_by_date',default=None)












          record = PaymentRequest.objects.get(id=_id)

          record.compiled_by = request.user.username
          record.payee= payee
          d = datetime.datetime.now()
          record.date_of_request = "{:%B %d, %Y}".format(d)



          record.payment_type= payment_type
          record.amount= amount
          record.project_number= project_number

          record.account_code= account_code 
          record.details = details
          # // record.amount = pat_name
          # record.unit_price = unit_price
          record.total= total

          record.certified_by= certified_by
          # record.certified_by_date= certified_by_date

          # record.cleared_by_fin_man= cleared_by_fin_man
          # record.cleared_by_fin_man_date= cleared_by_fin_man_date

          # record.approved_by_project_man= approved_by_project_man
          # record.approved_by_project_man_date= approved_by_project_man_date

          # record.approved_by= approved_by
          # record.approved_by_date= approved_by_date

          record.save()



          return JsonResponse( {'message':"success"})

        except Exception as e  :
            f= open("service1.txt","w")
            f.write(str(e))
            f.close()
            return JsonResponse({'message':"failed"})




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