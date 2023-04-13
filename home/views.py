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
from .utils import *
from django.contrib.auth.decorators import login_required


app = Flask(__name__)

from django.contrib.auth import views as auth_views

# Create your views here.
@login_required(login_url='login')
def index(request):
  username = request.user.username
  notices = Notifications.objects.filter(to=username)
  

  context = {
     "notices":notices,
     "nots_num": notices.count()

  }

  return render(request, 'pages/index.html', context=context)

@login_required(login_url='login')
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
@login_required(login_url='login')
def purchase_request(request):
    form = PuchaseRequest.objects.all()
    context = {'form':form}
    return render(request, 'pages/purchase_requests/purchase_requests.html', context)

@login_required(login_url='login')
def purchase_request_all(request):
    records = PuchaseRequest.objects.all()
    context = {'records':records}
    return render(request, 'pages/purchase_requests/list.html', context)

@login_required(login_url='login')
def purchase_request_super(request):
    form = PuchaseRequest.objects.all()
    context = {'form':form}
    return render(request, 'pages/purchase_requests/list.html', context)

@login_required(login_url='login')
def purchase_request_pending(request):
    form = PuchaseRequest.objects.all()
    context = {'form':form}
    return render(request, 'pages/purchase_request.html', context)

@login_required(login_url='login')
def purchase_request_approved(request):
    form = PuchaseRequest.objects.all()
    context = {'form':form}
    return render(request, 'pages/purchase_request.html', context)

@login_required(login_url='login')
def purchase_request_add(request):
    form = PuchaseRequest.objects.all()
    context = {'form':form}
    return render(request, 'pages/purchase_requests/add.html', context)

@login_required(login_url='login')
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
        #   record.date_of_request = "{:%B %d, %Y  %H:%M:%S}".format(d)
          record.accounts_clerk_approved_date= accounts_clerk_approved_date

          record.save()

          return JsonResponse( {'message':"success"})

        except Exception as e  :
            f= open("service1.txt","w")
            f.write(str(e))
            f.close()
            print(str(e))
            return JsonResponse({'message':(str(e))})

@login_required(login_url='login')
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

# ***********************************************************************************************************************
# comparative schedule
@login_required(login_url='login')
def comp_schedule(request):
    records = ComparativeSchedule.objects.all()
    context = {'records':records}
    return render(request, 'pages/comparative_schedules/comparative_schedules.html', context)

@login_required(login_url='login')
def comp_schedule_all(request):
    records = ComparativeSchedule.objects.all()
    context = {'records':records}
    return render(request, 'pages/comparative_schedules/list.html', context)

@login_required(login_url='login')
def comp_schedule_super(request):
    form = ComparativeSchedule.objects.all()
    context = {'form':form}
    return render(request, 'pages/payment_request.html', context)

@login_required(login_url='login')
def comp_schedule_pending(request):
    form = ComparativeSchedule.objects.all()
    context = {'form':form}
    return render(request, 'pages/payment_request.html', context)

@login_required(login_url='login')
def comp_schedule_approved(request):
    form = ComparativeSchedule.objects.all()
    context = {'form':form}
    return render(request, 'pages/payment_request.html', context)

@login_required(login_url='login')
def comp_schedule_add(request):
    form = ComparativeSchedule.objects.all()
    context = {'form':form}
    return render(request, 'pages/comparative_schedules/add.html', context)

@login_required(login_url='login')
@csrf_exempt
@app.route("/send_record")
def comp_schedule_send_record(request):

    with app.app_context():
        try:
          # request_id= request.POST.get('request_id',default=None)
          payee= request.POST.get('payee',default=None)

          company_name_supplier1= request.POST.get('company_name_supplier1',default=None)
          item_number_supplier1= request.POST.get('item_number_supplier1',default=None)
          desc_supplier1= request.POST.get('desc_supplier1',default=None)
          qnty_supplier1= request.POST.get('qnty_supplier1',default=None) 
          unit_price_supplier1 = request.POST.get('unit_price_supplier1',default=None)
          total_price_supplier1 = request.POST.get('total_price_supplier1',default=None)

          company_name_supplier2= request.POST.get('company_name_supplier2',default=None)
          item_number_supplier2= request.POST.get('item_number_supplier2',default=None)
          desc_supplier2= request.POST.get('desc_supplier2',default=None)
          qnty_supplier2= request.POST.get('qnty_supplier2',default=None) 
          unit_price_supplier2 = request.POST.get('unit_price_supplier2',default=None)
          total_price_supplier2 = request.POST.get('total_price_supplier2',default=None)

          company_name_supplier3= request.POST.get('company_name_supplier3',default=None)
          item_number_supplier3= request.POST.get('item_number_supplier3',default=None)
          desc_supplier3= request.POST.get('desc_supplier3',default=None)
          qnty_supplier3= request.POST.get('qnty_supplier3',default=None) 
          unit_price_supplier3 = request.POST.get('unit_price_supplier3',default=None)
          total_price_supplier3 = request.POST.get('total_price_supplier3',default=None)

          recommended_supplier= request.POST.get('recommended_supplier',default=None)
          recommended_supplier_reason= request.POST.get('recommended_supplier_reason',default=None)
          dpt_project_requesting= request.POST.get('dpt_project_requesting',default=None)

          # requested_by= request.POST.get('requested_by',default=None)
          # requested_by_sig= request.POST.get('requested_by_sig',default=None)
          # requested_by_date= request.POST.get('requested_by_date',default=None)

          tech_person_by= request.POST.get('tech_person_by',default=None)
          # tech_person_by_sig= request.POST.get('tech_person_by_sig',default=None)
          # tech_person_date= request.POST.get('tech_person_date',default=None)

          # dpt_head_by= request.POST.get('dpt_head_by',default=None)
          # dpt_head_by_sig= request.POST.get('dpt_head_by_sig',default=None)
          # dpt_head_date= request.POST.get('dpt_head_date',default=None)

          # team_lead_by= request.POST.get('team_lead_by',default=None)
          # team_lead_by_sig= request.POST.get('team_lead_by_sig',default=None)
          # team_lead_date= request.POST.get('team_lead_date',default=None)

          # approved_by= request.POST.get('approved_by',default=None)
          # approved_by_sig= request.POST.get('approved_by_sig',default=None)
          # approved_date= request.POST.get('approved_date',default=None)

          record = ComparativeSchedule()
          notice = Notifications()

        #   record.compiled_by = request.user.username
          # record.request_id= request_id
          record.payee= payee

          record.company_name_supplier1= company_name_supplier1
          record.item_number_supplier1= item_number_supplier1
          record.desc_supplier1= desc_supplier1
          record.qnty_supplier1= qnty_supplier1 
          record.unit_price_supplier1 = unit_price_supplier1
          record.total_price_supplier1= total_price_supplier1

          record.company_name_supplier2= company_name_supplier2
          record.item_number_supplier2= item_number_supplier2
          record.desc_supplier2= desc_supplier2
          record.qnty_supplier2= qnty_supplier2 
          record.unit_price_supplier2 = unit_price_supplier2
          record.total_price_supplier2= total_price_supplier2
        
          record.company_name_supplier3= company_name_supplier3
          record.item_number_supplier3= item_number_supplier3
          record.desc_supplier3= desc_supplier3
          record.qnty_supplier3= qnty_supplier3 
          record.unit_price_supplier3 = unit_price_supplier3
          record.total_price_supplier3= total_price_supplier3

          record.recommended_supplier= recommended_supplier
          record.recommended_supplier_reason= recommended_supplier_reason
          record.dpt_project_requesting= dpt_project_requesting
          username = request.user.username 
          record.requested_by= username

          notice.trigger = username

          # record.requested_by_sig = requested_by_sig

          d = datetime.datetime.now()
          record.requested_by_date = "{:%B %d, %Y  %H:%M:%S}".format(d)
          # record.requested_by_date= requested_by_date
        
          record.tech_person_by= tech_person_by
          notice.message = " "+ username +" created a Comparative schedule\n and assigned you as the Technical Person to approve."
          # record.tech_person_by_sig= tech_person_by_sig
          notice.status = "New"
          notice.to  = tech_person_by
          notice.date_time = "{:%B %d, %Y  %H:%M:%S}".format(d)
          # record.tech_person_date= tech_person_date

          # record.dpt_head_by= dpt_head_by 
          # record.dpt_head_by_sig = dpt_head_by_sig
          # record.dpt_head_date= dpt_head_date

          # record.team_lead_by= team_lead_by 
          # record.team_lead_by_sig = team_lead_by_sig
          # record.team_lead_date= team_lead_date

          # record.approved_by= approved_by
          # record.approved_by_sig= approved_by_sig
          # record.approved_date= approved_date

          # d = datetime.datetime.now()
        #   record.date_of_request = "{:%B %d, %Y  %H:%M:%S}".format(d)
        #   record.approved_by_date= approved_by_date

          record.save()
          notice.save()

          return JsonResponse( {'message':"success"})

        except Exception as e  :
            f= open("service2.txt","w")
            f.write(str(e))
            f.close()
            return JsonResponse({'message':"failed"})

@login_required(login_url='login')
@csrf_exempt
def comp_schedule_get_record(request):
    context={}
    if request.method == "POST":
      try:
        _id = request.POST.get('id',default=None)

        record = ComparativeSchedule.objects.get(id=_id)
        dic = {
      "payee":record.payee,
      "message":"success",
      "company_name_supplier1":record.company_name_supplier1,
      "item_number_supplier1":record.item_number_supplier1,
      "desc_supplier1":record.desc_supplier1,
      "qnty_supplier1":record.qnty_supplier1,
      "unit_price_supplier1":record.unit_price_supplier1,
      "total_price_supplier1":record.total_price_supplier1,

      "company_name_supplier2":record.company_name_supplier2,
      "item_number_supplier2":record.item_number_supplier2,
      "desc_supplier2":record.desc_supplier2,
      "qnty_supplier2":record.qnty_supplier2,
      "unit_price_supplier2":record.unit_price_supplier2,
      "total_price_supplier2":record.total_price_supplier2,

      "company_name_supplier3":record.company_name_supplier3,
      "item_number_supplier3":record.item_number_supplier3,
      "desc_supplier3":record.desc_supplier3,
      "qnty_supplier3":record.qnty_supplier3,
      "unit_price_supplier3":record.unit_price_supplier3,
      "total_price_supplier3":record.total_price_supplier3,

      "recommended_supplier":record.recommended_supplier,
      "recommended_supplier_reason":record.recommended_supplier_reason,
      "dpt_project_requesting":record.dpt_project_requesting,

      "requested_by":record.requested_by,
      "requested_by_sig":record.requested_by_sig,
      "requested_by_date":record.requested_by_date,

      "tech_person_by":record.tech_person_by,
      "tech_person_by_sig":record.tech_person_by_sig,
      "tech_person_date":record.tech_person_date,

      "dpt_head_by":record.dpt_head_by,
      "dpt_head_by_sig":record.dpt_head_by_sig,
      "dpt_head_date":record.dpt_head_date,

      "team_lead_by":record.team_lead_by,
      "team_lead_by_sig":record.team_lead_by_sig,
      "team_lead_date":record.team_lead_date,

      "approved_by":record.approved_by,
      "approved_by_sig":record.approved_by_sig,
      "approved_date":record.approved_date,
    }
        return JsonResponse(dic)

      except Exception as e:
        return JsonResponse(str(e))

    else:
        return redirect('/comp_schedule')





login_required(login_url='login')
@csrf_exempt
def comp_schedule_approve(request):
    if request.method == "POST":
      
      _id = request.POST.get('id',default=None)
      head = request.POST.get('head',default=None)
      username = request.user.username
        # objs = Record.objects.get(id=_id)
      record = ComparativeSchedule.objects.get(id=_id)
      record.tech_person_by = username
      record.dpt_head_by = head
      d = datetime.datetime.now()
          # record.date_of_request = "{:%B %d, %Y  %H:%M:%S}".format(d)
      record.tech_person_date= "{:%B %d, %Y  %H:%M:%S}".format(d)

      record.save()

      notice = Notifications()
      notice.to = head
      notice.message = " "+ username +" updated a Comparative schedule\n and assigned you as the Department Head for you to approve."
      notice.date_time = "{:%B %d, %Y  %H:%M:%S}".format(d)
      notice.trigger = username
      notice.save()




      return JsonResponse( {'message':"success"})
    else:
      return render(request, 'pages/payment_requests/list.html', {})



login_required(login_url='login')
@csrf_exempt
def comp_schedule_approve_head(request):
    if request.method == "POST":
      
      _id = request.POST.get('id',default=None)
      pi = request.POST.get('pi',default=None)
      lead = request.POST.get('lead',default=None)

        # objs = Record.objects.get(id=_id)
      record = ComparativeSchedule.objects.get(id=_id)
      username = request.user.username
      record.dpt_head_by = username
      record.team_lead_by = lead
      record.approved_by = pi

      d = datetime.datetime.now()
          # record.date_of_request = "{:%B %d, %Y  %H:%M:%S}".format(d)
      record.dpt_head_date= "{:%B %d, %Y  %H:%M:%S}".format(d)

      record.save()

      if pi == "None":
         pass
      else:
        notice = Notifications()
        notice.to = pi
        notice.message = " "+ username +" updated a Comparative schedule\n and assigned you as the PI for you to approve."
        notice.date_time = "{:%B %d, %Y  %H:%M:%S}".format(d)
        notice.trigger = username
        notice.save()

      if lead == "None":
         pass
      else:
        notice = Notifications()
        notice.to = lead
        notice.message = " "+ username +" updated a Comparative schedule\n and assigned you as the Coordinator for you to approve."
        notice.date_time = "{:%B %d, %Y  %H:%M:%S}".format(d)
        notice.trigger = username
        notice.save()


      return JsonResponse( {'message':"success"})

    else:
      return render(request, 'pages/payment_requests/list.html', {})




login_required(login_url='login')
@csrf_exempt
def comp_schedule_approve_lead(request):
    if request.method == "POST":
      
      _id = request.POST.get('id',default=None)
      pi = request.POST.get('pi',default=None)
      # lead = request.POST.get('lead',default=None)

        # objs = Record.objects.get(id=_id)
      record = ComparativeSchedule.objects.get(id=_id)
      record.approved_by = pi
      # record.team_lead_by = request.user.username
      # record.team_lead_by = lead

      d = datetime.datetime.now()
          # record.date_of_request = "{:%B %d, %Y  %H:%M:%S}".format(d)
      record.team_lead_date= "{:%B %d, %Y  %H:%M:%S}".format(d)

      if pi == "None":
         pass
      else:
        notice = Notifications()
        notice.to = pi
        notice.message = " "+ request.user.username +" updated a Comparative schedule\n and assigned you as the PI for you to approve."
        notice.date_time = "{:%B %d, %Y  %H:%M:%S}".format(d)
        notice.trigger = request.user.username
        notice.save()



      record.save()




      return JsonResponse( {'message':"success"})

    else:
      return render(request, 'pages/payment_requests/list.html', {})


login_required(login_url='login')
@csrf_exempt
def comp_schedule_approve_pi(request):
    if request.method == "POST":
      
      _id = request.POST.get('id',default=None)
      # pi = request.POST.get('pi',default=None)
      # lead = request.POST.get('lead',default=None)

        # objs = Record.objects.get(id=_id)
      record = ComparativeSchedule.objects.get(id=_id)
      # record.approved_by = pi
      record.approved_by = request.user.username
      # record.team_lead_by = lead

      d = datetime.datetime.now()
          # record.date_of_request = "{:%B %d, %Y  %H:%M:%S}".format(d)
      record.approved_date= "{:%B %d, %Y  %H:%M:%S}".format(d)

      record.save()
      notice = Notifications()
      notice.to = record.requested_by
      notice.message = " "+ request.user.username +" approved your Comparative schedule."
      notice.date_time = "{:%B %d, %Y  %H:%M:%S}".format(d)
      notice.trigger = request.user.username
      notice.save()



      return JsonResponse( {'message':"success"})

    else:
      return render(request, 'pages/payment_requests/list.html', {})

login_required(login_url='login')
def comp_schedule_open_record(request):
    if request.method == "POST":
      
      _id = request.POST.get('id',default=None)

        # objs = Record.objects.get(id=_id)
      record = ComparativeSchedule.objects.get(id=_id)
      context = {'record':record}
      print("IN POST")
      return render(request, 'pages/comparative_schedules/view_record.html', context)
    else:
       redirect("payment_request_all")


@login_required(login_url='login')
def comp_schedule_pending_view(request):
    if request.method == "POST":
      
      _id = request.POST.get('id',default=None)

        # objs = Record.objects.get(id=_id)
      record = ComparativeSchedule.objects.get(id=_id)
      context = {'record':record}

      print("IN POST")

      if record.tech_person_date == "None" and record.tech_person_by == request.user.username:
         print("certified")
         return render(request, 'pages/comparative_schedules/tech_approve.html', context)
      
      elif record.dpt_head_date == "None" and record.dpt_head_by == request.user.username:
         print("cleared")

         return render(request, 'pages/comparative_schedules/head_approve.html', context)
      

      elif record.team_lead_date == "None" and record.team_lead_by is not "None" and record.team_lead_by == request.user.username:
         print("approved")

         return render(request, 'pages/comparative_schedules/lead_approve.html', context)
      

      elif record.team_lead_by == "None" and record.team_lead_date == "None" and record.approved_by == "None" and record.dpt_head_by == request.user.username:
         print("approved")

         return render(request, 'pages/comparative_schedules/head_approve.html', context)
      
      elif record.approved_date == "None" and record.approved_by is not "None" and record.approved_by == request.user.username: 
         print("approved")

         return render(request, 'pages/comparative_schedules/pi_approve.html', context)
      else:
        return render(request, 'pages/comparative_schedules/not_auth.html', {})


@login_required(login_url='login')
def comp_schedule_pending(request):
    username = request.user.username
    records = ComparativeSchedule.objects.filter((Q(approved_by=username) & Q (approved_date="None")) | (Q(dpt_head_by=username) & Q (dpt_head_date="None")) | (Q(team_lead_by=username) & Q (team_lead_date="None")) | (Q(tech_person_by=username) & Q (tech_person_date="None")) )
    context = {'records':records}
    return render(request, 'pages/comparative_schedules/list_pending.html', context)


# ***********************************************************************************************************************

# ***********************************************************************************************************************
# payment request
@login_required(login_url='login')
def payment_request_all(request):
    username = request.user.username
    user_id = request.user.id
    records = PaymentRequest.objects.filter( Q(compiled_by=username) | Q(certified_by= username) | Q(approved_by=username) | Q(cleared_by_fin_man=username))
    context = {'records':records}
    return render(request, 'pages/payment_requests/list2.html', context)

@login_required(login_url='login')
def payment_request(request):
    form = PaymentRequest.objects.all()
    context = {'form':form}
    return render(request, 'pages/payment_requests/payment_requests.html', context)

@login_required(login_url='login')
def payment_request_view(request):
    if request.method == "POST":
      
      _id = request.POST.get('id',default=None)

        # objs = Record.objects.get(id=_id)
      record = PaymentRequest.objects.get(id=_id)
      context = {'record':record}
      print("IN POST")
      if record.certified_by_date == "None" and record.certified_by == request.user.username:
         print("certified")
         return render(request, 'pages/payment_requests/certify.html', context)
      
      elif record.cleared_by_fin_man_date == "None" and record.cleared_by_fin_man == request.user.username:
         print("cleared")

         return render(request, 'pages/payment_requests/clear.html', context)
      
      elif record.approved_by_date == "None" and record.approved_by == request.user.username:
         print("approved")

         return render(request, 'pages/payment_requests/approve.html', context)
      else:
         return redirect("payment_request_pending")


@login_required(login_url="login")
def payment_request_open_record(request):
    if request.method == "POST":
      
      _id = request.POST.get('id',default=None)

        # objs = Record.objects.get(id=_id)
      record = PaymentRequest.objects.get(id=_id)
      context = {'record':record}
      print("IN POST")
      return render(request, 'pages/payment_requests/view_record.html', context)
    else:
       redirect("payment_request_all")


# def payment_request_view2(request):
#     if request.method == "POST":
      
#       _id = request.POST.get('id',default=None)

#         # objs = Record.objects.get(id=_id)
#       record = PaymentRequest.objects.get(id=_id)
#       context = {'record':record}
#       print("IN POST")
#       return render(request, 'pages/payment_requests/view2.html', context)
#     else:
#        redirect("payment_request_all")

@login_required(login_url='login')
def payment_request_pending_view(request):
    if request.method == "POST":
      
      _id = request.POST.get('id',default=None)

        # objs = Record.objects.get(id=_id)
      record = PaymentRequest.objects.get(id=_id)
      context = {'record':record}

      print("IN POST")
      if record.certified_by_date == "None" and record.certified_by == request.user.username:
         print("certified")
         return render(request, 'pages/payment_requests/certify.html', context)
      elif record.cleared_by_fin_man_date == "None" and record.cleared_by_fin_man == request.user.username:
         print("cleared")

         return render(request, 'pages/payment_requests/clear.html', context)
      
      elif record.approved_by_date == "None" and record.approved_by == request.user.username:
         print("approved")

         return render(request, 'pages/payment_requests/approve.html', context)


    else:
      return render(request, 'pages/payment_requests/list2.html', {})


@login_required(login_url='login')
@csrf_exempt
def payment_request_print(request):
    # if request.method == "POST":
        current_url = request.path
        x= current_url.split("/")[-1]
        print(x)

        # _id = request.POST.get(x)
        # print(_id)

        record = PaymentRequest.objects.get(id=x)
        
        data = {"payee": record.payee,
        "compiled_by": record.compiled_by,
        "date_of_request": record.date_of_request,
        "payment_type": record.payment_type,
        "project_number": record.project_number,
        "account_code": record.account_code,
        "details": record.details,
        "amount": record.amount,
        "total": record.total,
        "certified_by": record.certified_by,
        "certified_by_date": record.certified_by_date,
        "cleared_by_fin_man": record.cleared_by_fin_man,
        "cleared_by_fin_man_date": record.cleared_by_fin_man_date,
        "approved_by_project_man": record.approved_by_project_man,
        "approved_by_project_man_date": record.approved_by_project_man_date,
        "approved_by": record.approved_by,
        "approved_by_date": record.approved_by_date,
        
        "message":"success"}   


        pdf = render_to_pdf('pages/payment_requests/print.html', data)
        return HttpResponse(pdf, content_type='application/pdf')

    # if request.method == "POST":
    #   _id = request.POST.get('id',default=None)

      
    #   print(current_url)

    #   l = current_url.split('/')
    #   print(l)

      

    #   record = PaymentRequest.objects.filter(id=x)
    #   context = {'record':record}
    #   return render(request, 'pages/payment_requests/print.html', context)
@login_required(login_url='login')
def payment_request_super(request):
    records = PaymentRequest.objects.all()
    context = {'records':records}
    return render(request, 'pages/payment_requests/list2.html', context)

@login_required(login_url='login')
def payment_request_edit(request):
    form = PaymentRequest.objects.all()
    context = {'form':form}
    return render(request, 'pages/payment_requests/add.html', context)

# @login_required(login_url='login')
# def payment_request_pending_certification(request):
#     records = PaymentRequest.objects.filter(Q (certified_by="None") & Q(certified_by_date="None"))
#     context = {'records':records}
#     return render(request, 'pages/payment_requests/list.html', context)

@login_required(login_url='login')
def payment_request_certification(request):
    if request.method == "POST":
      
      _id = request.POST.get('id',default=None)

        # objs = Record.objects.get(id=_id)
      record = PaymentRequest.objects.get(id=_id)
      context = {'record':record}
      return render(request, 'pages/payment_requests/view.html', context)
    else:
      return render(request, 'pages/payment_requests/list.html', {})


# @login_required(login_url='login')
# def payment_request_pending_clearance(request):
#     username = request.user.username
#     records = PaymentRequest.objects.filter(Q (cleared_by_fin_man=username)  & Q(cleared_by_fin_man_date="None") )
#     context = {'records':records}
#     return render(request, 'pages/payment_requests/list.html', context)



@login_required(login_url='login')
def payment_request_clearance(request):
    if request.method == "POST":
      
      _id = request.POST.get('id',default=None)

        # objs = Record.objects.get(id=_id)
      record = PaymentRequest.objects.get(id=_id)
      context = {'record':record}
      return render(request, 'pages/payment_requests/view.html', context)
    else:
      return render(request, 'pages/payment_requests/list.html', {})

# @login_required(login_url='login')
# def payment_request_clear(request):
#     if request.method == "POST":
      
#       _id = request.POST.get('id',default=None)

#         # objs = Record.objects.get(id=_id)
#       record = PaymentRequest.objects.get(id=_id)
#       record.cleared_by_fin_man = request.user.username
#       # record.certified_by_date = request.user.username
#       d = datetime.datetime.now()
#           # record.date_of_request = "{:%B %d, %Y  %H:%M:%S}".format(d)
#       record.cleared_by_fin_man_date= "{:%B %d, %Y  %H:%M:%S}".format(d)

#       record.save()




#       return JsonResponse( {'message':"success"})

#     else:
#       return render(request, 'pages/payment_requests/list.html', {})



@login_required(login_url='login')
def payment_request_pending_approval(request):
    records = PaymentRequest.objects.filter(approved_by="None")
    context = {'records':records}
    return render(request, 'pages/payment_requests/list.html', context)


# @login_required(login_url='login')
# def payment_request_approval(request):
#     if request.method == "POST":
      
#       _id = request.POST.get('id',default=None)

#         # objs = Record.objects.get(id=_id)
#       record = PaymentRequest.objects.get(id=_id)




#       context = {'record':record}
#       return render(request, 'pages/payment_requests/view.html', context)
#     else:
#       return render(request, 'pages/payment_requests/list.html', {})

# @login_required(login_url='login')
# def payment_request_approve(request):
#     if request.method == "POST":
      
#       _id = request.POST.get('id',default=None)

#         # objs = Record.objects.get(id=_id)
#       record = PaymentRequest.objects.get(id=_id)
#       record.approved_by = request.user.username
#       # record.certified_by_date = request.user.username
#       d = datetime.datetime.now()
#           # record.date_of_request = "{:%B %d, %Y  %H:%M:%S}".format(d)
#       record.approved_by_date= "{:%B %d, %Y  %H:%M:%S}".format(d)





#       return JsonResponse( {'message':"success"})

#     else:
#       return render(request, 'pages/payment_requests/list.html', {})

@login_required(login_url='login')
@csrf_exempt
def payment_request_certify(request):
    
    try:
      if request.method == "POST":
        
        _id = request.POST.get('id',default=None)
        clear = request.POST.get('clear',default=None)

          # objs = Record.objects.get(id=_id)
        record = PaymentRequest.objects.get(id=_id)
        record.certified_by = request.user.username
        record.cleared_by_fin_man = clear
        d = datetime.datetime.now()
            # record.date_of_request = "{:%B %d, %Y  %H:%M:%S}".format(d)
        record.certified_by_date= "{:%B %d, %Y  %H:%M:%S}".format(d)
        record.save()

        notice = Notifications()
        notice.to = clear
        notice.message = " "+ request.user.username +" updated a Payement Request\n and assigned you as the Finance Officer for you to clear."
        notice.date_time = "{:%B %d, %Y  %H:%M:%S}".format(d)
        notice.trigger = request.user.username
        notice.save()

        return JsonResponse( {'message':"success"})
      else:
        return render(request, 'pages/payment_requests/list.html', {})

    except:
       return JsonResponse( {'message':"failed"})

@login_required(login_url='login')
@csrf_exempt
def payment_request_clear(request):
    
    try:
      if request.method == "POST":
        
        _id = request.POST.get('id',default=None)
        approver = request.POST.get('approver',default=None)

          # objs = Record.objects.get(id=_id)
        record = PaymentRequest.objects.get(id=_id)
        record.cleared_by_fin_man = request.user.username
        record.approved_by = approver
        d = datetime.datetime.now()
            # record.date_of_request = "{:%B %d, %Y  %H:%M:%S}".format(d)
        record.cleared_by_fin_man_date= "{:%B %d, %Y  %H:%M:%S}".format(d)

        record.save()

        notice = Notifications()
        notice.to = approver
        notice.message = " "+ request.user.username +" updated a Payement Request\n and assigned you as the Approver."
        notice.date_time = "{:%B %d, %Y  %H:%M:%S}".format(d)
        notice.trigger = request.user.username
        notice.save()

        return JsonResponse( {'message':"success"})
      else:
        return render(request, 'pages/payment_requests/list.html', {})


    except:
       return JsonResponse( {'message':"failed"})


@login_required(login_url='login')
@csrf_exempt
def payment_request_approve(request):
    
    try:
      if request.method == "POST":
        
        _id = request.POST.get('id',default=None)

          # objs = Record.objects.get(id=_id)
        record = PaymentRequest.objects.get(id=_id)
        record.approved_by = request.user.username
        # record.certified_by_date = request.user.username
        d = datetime.datetime.now()
            # record.date_of_request = "{:%B %d, %Y  %H:%M:%S}".format(d)
        record.approved_by_date= "{:%B %d, %Y  %H:%M:%S}".format(d)



        notice = Notifications()
        notice.to = record.compiled_by
        record.save()

        notice.message = " "+ request.user.username +" Approved your Payement Request."
        notice.date_time = "{:%B %d, %Y  %H:%M:%S}".format(d)
        notice.trigger = request.user.username
        notice.save()

        return JsonResponse( {'message':"success"})
      else:
        return render(request, 'pages/payment_requests/list.html', {})


    except:
       return JsonResponse( {'message':"failed"})

@login_required(login_url='login')
def payment_request_pending(request):
    username = request.user.username
    records = PaymentRequest.objects.filter((Q(approved_by=username) & Q (approved_by_date="None")) | (Q(certified_by=username) & Q (certified_by_date="None")) | (Q(cleared_by_fin_man=username) & Q (cleared_by_fin_man_date="None")))
    context = {'records':records}
    return render(request, 'pages/payment_requests/list_pending.html', context)


@login_required(login_url='login')
def payment_request_approved(request):
    username = request.user.username

    records = PaymentRequest.objects.filter( (Q(approved_by=username) & ~Q(approved_by_date="None") ) | (Q(compiled_by=username) & ~Q(approved_by_date="None") ) |  (Q(certified_by=username) & ~Q(approved_by_date="None") ) | (Q(cleared_by_fin_man=username) & ~Q(approved_by_date="None") )  )
    context = {'records':records}
    return render(request, 'pages/payment_requests/list2.html', context)

@login_required(login_url='login')
def payment_request_add(request):
    
    form = PaymentRequest.objects.all()
    context = {'form':form}
    return render(request, 'pages/payment_requests/add.html', context)


@login_required(login_url='login')
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

    

@login_required(login_url='login')
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
          "compiled_by": record.compiled_by,
          "compiled_by_date": record.date_of_request,

          "account_code": record.account_code, 
          "details": record.details,
          "qnty": record.qnty,
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

@login_required(login_url='login')
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
          qnty = request.POST.get('qnty',default=None)
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
          record.qnty = qnty
          record.total= total

          record.certified_by= certified_by
          # record.certified_by_date= certified_by_date

          # record.cleared_by_fin_man= cleared_by_fin_man
          # record.cleared_by_fin_man_date= cleared_by_fin_man_date

          # record.approved_by_project_man= approved_by_project_man
          # record.approved_by_project_man_date= approved_by_project_man_date

          # record.approved_by= approved_by

          notice = Notifications()
          notice.to= record.certified_by
          notice.trigger = request.user.username
          notice.message = request.user.username +" has created a Payment Request and assigned you to Certify"

          d = datetime.datetime.now()
          record.date_of_request = "{:%B %d, %Y  %H:%M:%S}".format(d)
          notice.date_time = "{:%B %d, %Y  %H:%M:%S}".format(d)
          notice.status = "New"
          notice.save()
          # record.approved_by_date= approved_by_date


          record.save()

          return JsonResponse( {'message':"success"})

        except Exception as e  :
            f= open("service1.txt","w")
            f.write(str(e))
            f.close()
            return JsonResponse({'message':"failed"})

@login_required(login_url='login')
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
          qnty = request.POST.get('qnty',default=None)
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
          record.date_of_request = "{:%B %d, %Y  %H:%M:%S}".format(d)

          record.payment_type= payment_type
          record.amount= amount
          record.project_number= project_number

          record.account_code= account_code 
          record.details = details
          # // record.amount = pat_name
          record.qnty = qnty
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
# ***********************************************************************************************************************


