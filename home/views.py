from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *
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
import qrcode

# Data to be encoded
data = 'QR Code using make() function'
 
# Encoding data using make() function
img = qrcode.make(data)
 
# Saving as an image file
img.save('MyQRCode1.png')

app = Flask(__name__)

from django.contrib.auth import views as auth_views


from django.http import FileResponse
import os
 
def show_pdf(request):
    #printrequest.path)
    filepath="C:\\fakepath\\2022 PRICE LIST (1).pdf"
    return FileResponse(open(filepath, 'rb'), content_type='application/pdf')


# Create your views here.
@login_required(login_url='login')
def index(request):
  username = request.user.username
  notices = Notifications.objects.filter(to=username)

  payments = PaymentRequest.objects.all().order_by('-id')[::5][:-1]
  total_payments= 123455

  context = {
     "notices":notices,
     "nots_num": notices.count(),
     "payments": payments,
     "total_payments":total_payments,

  }

  return render(request, 'pages/index.html', context=context)


@login_required(login_url='login')
def app_root(request):
  username = request.user.username
  notices = Notifications.objects.filter(to=username)

  payments = PaymentRequest.objects.all().order_by('-id')[::5][:-1]
  total_payments= 123455

  context = {
     "notices":notices,
     "nots_num": notices.count(),
     "payments": payments,
     "total_payments":total_payments,

  }

  return render(request, 'pages/index.html', context=context)


@login_required(login_url='login')
def payment_request(request):
    return render(request, 'pages/payment_requests/payment_requests.html')



def cm(request):
      return JsonResponse( {'message':"ALVSeuuWa5aXqWtjDLfBgU3FdxTMb4Z2YL8pLmSyu2Q.RuEKtPWKHBIYysMx6MgzRDdsJa4D9GKCpw-7cQNjy_k","tab":"1"})


def typography(request):
  return render(request, 'pages/typography.html')

def color(request):
  return render(request, 'pages/color.html')

def icon_tabler(request):
  return render(request, 'pages/icon-tabler.html')

def sample_page(request):
  return render(request, 'pages/sample-page.html')


# # Authentication
# def registration(request):
#   if request.method == 'POST':
#     form = RegistrationForm(request.POST)
#     if form.is_valid():
#       form.save()
#       #print'Account created successfully!')
#       return redirect('/procurement//accounts/login/')
#     else:
#       #print"Registration failed!")
#   else:
#     form = RegistrationForm()
  
#   context = {'form': form}
#   return render(request, 'accounts/register.html', context)

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


from django.conf import settings
from django.core.files.storage import FileSystemStorage

def purchase_request_quote_upload(request):
    if request.method == 'POST' and request.FILES['quote']:
        myfile = request.FILES['quote']
        request_id = request.POST.get('request_id')
        
        # fs = FileSystemStorage()

        # filename = fs.save("uploads/"+myfile.name, myfile)
        # uploaded_file_url = fs.url(filename)



        import os
        path = "uploads/purchase_requests/"+str(request_id)
        # Check whether the specified path exists or not
        # #print"path ",path)
        isExist = os.path.exists(path)
        if not isExist:

          # Create a new directory because it does not exist
          os.makedirs(path)



        fs = FileSystemStorage()
        filename1 = fs.save(path+"/"+myfile.name, myfile)
        uploaded_file_url1 = fs.url(filename1)

        record = PuchaseRequestQuotation()
        record.request_id = request_id
        record.quote_path = uploaded_file_url1
        record.save()

    #     return render(request, 'core/simple_upload.html', {'uploaded_file_url': uploaded_file_url})
    # return render(request, 'core/simple_upload.html')
        return redirect('/procurement/purchase_request')
    else:
          return render(request, 'pages/purchase_requests/upload_quote.html')



    # if request.method == 'POST':
    #     form = PuchaseRequestQuoteForm(request.POST, request.FILES)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('purchase_request_all')
    # else:
    #     form = PuchaseRequestQuoteForm()
    # return render(request, 'purchase_requests/upload_quote.html', {'form': form})




@login_required(login_url='login')
def purchase_request(request):
    # form = PuchaseRequest.objects.all()
    context = {'form':"form"}
    return render(request, 'pages/purchase_requests/purchase_requests.html', context)

@login_required(login_url='login')
def purchase_request_all(request):
    records = PuchaseRequest.objects.all()
    context = {'records':records , "tab":"1"}
    return render(request, 'pages/purchase_requests/list2.html', context)

@login_required(login_url='login')
def purchase_request_super(request):
    form = PuchaseRequest.objects.all()
    context = {'form':form, "tab":"1"}
    return render(request, 'pages/purchase_requests/list2.html', context)

@login_required(login_url='login')
def purchase_request_pending(request):
      username = request.user.username

      records = PuchaseRequest.objects.filter( Q(rejector="None")  &( (Q(supervisor_approved=username) & Q (supervisor_approved_date="None")) | (Q(finance_officer=username) & Q (finance_officer_approved_date="None")) ))
      context = {'records':records, "tab":"1"}

      return render(request, 'pages/purchase_requests/list_pending.html', context)

@login_required(login_url='login')
def purchase_request_approved(request):
    username = request.user.username
    records = PuchaseRequest.objects.filter( (Q(requester =username)& ~Q(finance_officer_approved_date="None"))  |  (Q(supervisor_approved =username)& ~Q(finance_officer_approved_date="None")) | (Q(finance_officer =username)& ~Q(finance_officer_approved_date="None")) )
    context = {'records':records, "tab":"1"}
    return render(request, 'pages/purchase_requests/list_approved.html', context)

@login_required(login_url='login')
def purchase_request_add(request):
    form = PuchaseRequest.objects.all()
    context = {'form':form, "tab":"1"}
    return render(request, 'pages/purchase_requests/add.html', context)

@login_required(login_url='login')
@csrf_exempt
@app.route("/send_record")
def purchase_request_send_record(request):

    with app.app_context():
        try:
        
          requester= request.user.username
          requesting_dpt= request.POST.get('requesting_dpt',default=None)


          request_justification= request.POST.get('request_justification',default=None) 
          budget_line_item= request.POST.get('budget_line_item',default=None)

          qnty= request.POST.get('qnty',default=None)
          item_name= request.POST.get('item_name',default=None)

          description= request.POST.get('description',default=None)

          supervisor_approved= request.POST.get('supervisor_approved',default=None)

          # accounts_clerk_approved= request.POST.get('accounts_clerk_approved',default=None)
          # accounts_clerk_approved_date= request.POST.get('accounts_clerk_approved_date',default=None)

          record = PuchaseRequest()

          record.requester= requester
          record.requesting_dpt= requesting_dpt
          # record.q1 = q1

          record.request_justification= request_justification 
          record.budget_line_item= budget_line_item

          record.qnty= qnty
          record.item_name= item_name

          record.description= description

          record.supervisor_approved = supervisor_approved
          # record.supervisor_approved_date= supervisor_approved_date

          # record.accounts_clerk_approved= accounts_clerk_approved
          d = datetime.datetime.now()
          record.date_of_request = "{:%B %d, %Y  %H:%M:%S}".format(d)
          # record.accounts_clerk_approved_date= accounts_clerk_approved_date
          
          record.save()
       
          _id = record.pk
          return JsonResponse( {'message':"success",'id':_id})

        except Exception as e  :
            f= open("service1.txt","w")
            f.write(str(e))
            f.close()
            #printstr(e))
            return JsonResponse({'message':(str(e))})


@login_required(login_url='login')
@csrf_exempt
def purchase_request_get_record(request):
    context={}
    if request.method == "POST":

        _id = request.POST.get('id',default=None)

        # pdf = PuchaseRequestQuotation.objects.get(id=1)

        # try:
        #   pdf = PuchaseRequestQuotation.objects.get(request_id=_id)
        # except:
        #   pass
        record = PuchaseRequest.objects.get(id=_id)

        dic = {
                                            "requesting_dpt":record.requesting_dpt,
                                            "date_of_request":record.date_of_request,
                                            "budget_line_item":record.budget_line_item,
                                            "item_name":record.item_name,
                                            "description":record.description,
                                            "requester":record.requester,
                                            "rejector":record.rejector,
                                            "rejector_date":record.rejector_date,
                                            "rejector_message":record.rejector_message,

                
                                            "request_justification":record.request_justification,

                                            "qnty":record.qnty,

                
                                            "supervisor_approved":record.supervisor_approved,
                                            "supervisor_approved_date": record.supervisor_approved_date,
                
                                            "finance_officer": record.finance_officer,
                                            "finance_officer_approved_date": record.finance_officer_approved_date,
          "message":"success",
        }

        #printrecord.supervisor_approved)
        context = {'addTabActive': True, "record":"","tab":"1","tab":"1"}
        return JsonResponse(dic)
    else:
        return redirect('/procurement/payment_requests')
    




@login_required(login_url='login')
@csrf_exempt
def purchase_request_pi_approve(request):
    if request.method == "POST":
      
      _id = request.POST.get('id',default=None)
      clerk = request.POST.get('finance_officer',default=None)
      username = request.user.username
        # objs = Record.objects.get(id=_id)
      record = PuchaseRequest.objects.get(id=_id)
      record.finance_officer = clerk
      d = datetime.datetime.now()
          # record.date_of_request = "{:%B %d, %Y  %H:%M:%S}".format(d)
      record.supervisor_approved_date= "{:%B %d, %Y  %H:%M:%S}".format(d)

      record.save()

      notice = Notifications()
      notice.to = clerk
      notice.message = " "+ username +" updated a Purchse Request \n and assigned you as the Accounts Clerk for you to approve."
      notice.date_time = "{:%B %d, %Y  %H:%M:%S}".format(d)
      notice.trigger = username
      notice.save()




      return JsonResponse( {'message':"success","tab":"1"})
    else:
      return render(request, 'pages/purchase_requests/list.html', {})



@login_required(login_url='login')
@csrf_exempt
def purchase_request_clerk_approve(request):
    if request.method == "POST":
      
      _id = request.POST.get('id',default=None)
      # clerk = request.POST.get('clerk',default=None)
      username = request.user.username
        # objs = Record.objects.get(id=_id)
      record = PuchaseRequest.objects.get(id=_id)
      # record.accounts_clerk_approved = clerk
      d = datetime.datetime.now()
          # record.date_of_request = "{:%B %d, %Y  %H:%M:%S}".format(d)
      record.finance_officer_approved_date= "{:%B %d, %Y  %H:%M:%S}".format(d)
      notice = Notifications()
      notice.to = record.requester
      record.save()

  
      notice.message = " "+ username +" has Approved your Purchse Request."
      notice.date_time = "{:%B %d, %Y  %H:%M:%S}".format(d)
      notice.trigger = username
      notice.save()
      return JsonResponse( {'message':"success","tab":"1"})
    else:
      return render(request, 'pages/purchase_requests/list.html', {})
    

@login_required(login_url='login')
@csrf_exempt
def purchase_request_reject(request):
    if request.method == "POST":
      
      _id = request.POST.get('id',default=None)
      message = request.POST.get('message',default=None)
      username = request.user.username
        # objs = Record.objects.get(id=_id)
      record = PuchaseRequest.objects.get(id=_id)
      record.rejector = username
      record.rejector_message = message

      d = datetime.datetime.now()
          # record.date_of_request = "{:%B %d, %Y  %H:%M:%S}".format(d)
      record.rejector_date= "{:%B %d, %Y  %H:%M:%S}".format(d)
      notice = Notifications()
      notice.to = record.requester
      record.save()

  
      notice.message = " "+ username +" has rejected your Purchse Request."
      notice.date_time = "{:%B %d, %Y  %H:%M:%S}".format(d)
      notice.trigger = username
      notice.save()
      return JsonResponse( {'message':"success","tab":"1"})
    else:
      return render(request, 'pages/purchase_requests/list.html', {})
    




@login_required(login_url='login')
def purchase_request_view(request):
      username = request.user.username
      records = PuchaseRequest.objects.filter(Q(requester = username) | Q(supervisor_approved =username) | Q(finance_officer = username))
      context = {'records':records, "tab":"1"}


      return render(request, 'pages/purchase_requests/list2.html', context)



@login_required(login_url="login")
def purchase_request_open_record(request):
    if request.method == "POST":

      _id = request.POST.get('id',default=None)

      record = PuchaseRequest.objects.get(id=_id)
      context = {'record':record, "tab":"1"}
      #print"IN POST")
      return render(request, 'pages/purchase_requests/view_record.html', context)
    else:
       redirect("/procurement/purchase_request_all")


# make some error so this name is unique to purchase only

@login_required(login_url='login')
def purchase_request_edit_options(request):
    if request.method == "POST":
      
      _id = request.POST.get('id',default=None)

        # objs = Record.objects.get(id=_id)
      record = PuchaseRequest.objects.get(id=_id)
      context = {'record':record, "tab":"1"}
      # #print"IN POST")
      if record.supervisor_approved_date == "None" and record.supervisor_approved == request.user.username:
        #  #print"certified")
         return render(request, 'pages/purchase_requests/pi.html', context)
      
      elif record.finance_officer_approved_date == "None" and record.finance_officer == request.user.username:
        #  #print"cleared")

         return render(request, 'pages/purchase_requests/clerk.html', context)
      else:
         return render(request, 'pages/comparative_schedules/not_auth.html', {})
      

    else:
         return redirect("/procurement/purchase_request_pending")


# (request):


@login_required(login_url='login')
@csrf_exempt
def get_purchase_requests(request):
   try:
      dic = {}
      # User = get_user_model()
      schedules = PuchaseRequest.objects.filter(~Q(finance_officer_approved_date="None"))

      for schedule in schedules: 
          dic[schedule.id]= schedule.item_name +" : raised by "+ schedule.requester+" : raised on "+schedule.date_of_request
      return JsonResponse(dic)
   except Exception as e:
          return JsonResponse(str(e)) 






# ***********************************************************************************************************************

# comparative schedule

# ***********************************************************************************************************************
@login_required(login_url='login')
def comp_schedule(request):
    records = ComparativeSchedule.objects.all()
    context = {'records':records}
    return render(request, 'pages/comparative_schedules/comparative_schedules.html', context)

@login_required(login_url='login')
def comp_schedule_all(request):
    records = ComparativeSchedule.objects.all()
    context = {'records':records, "tab":"2"}
    return render(request, 'pages/comparative_schedules/list.html', context)

@login_required(login_url='login')
def comp_schedule_super(request):
    form = ComparativeSchedule.objects.all()
    context = {'form':form ,"tab":"2"}
    return render(request, 'pages/payment_request.html', context)


@login_required(login_url='login')
@csrf_exempt
def comp_schedule_print(request):
    # if request.method == "POST":
        current_url = request.path
        x= current_url.split("/")[-1]
        # #printx)

        record = ComparativeSchedule.objects.get(id=x)

        # qr_code(record.id)
        
        data = {"service_request": record.service_request,
        "request_id": record.request_id,
        "payee": record.payee,

        "company_name_supplier1": record.company_name_supplier1,
        "company_name_supplier2": record.company_name_supplier2,
        "company_name_supplier3": record.company_name_supplier3,

        "item_number_supplier1": record.item_number_supplier1,
        "item_number_supplier2": record.item_number_supplier2,
        "item_number_supplier3": record.item_number_supplier3,

        "desc_supplier1": record.desc_supplier1,
        "desc_supplier2": record.desc_supplier2,
        "desc_supplier3": record.desc_supplier3,

        "qnty_supplier1": record.qnty_supplier1,
        "qnty_supplier2": record.qnty_supplier2,
        "qnty_supplier3": record.qnty_supplier3,

        "unit_price_supplier1": record.unit_price_supplier1,
        "unit_price_supplier2": record.unit_price_supplier2,
        "unit_price_supplier3": record.unit_price_supplier3,

        "total_price_supplier1": record.total_price_supplier1,
        "total_price_supplier2": record.total_price_supplier2,
        "total_price_supplier3": record.total_price_supplier3,

        "requested_by": record.requested_by,
        "requested_by_sig": record.requested_by_sig,
        "requested_by_date": record.requested_by_date,

        "tech_person_by": record.tech_person_by,
        "tech_person_by_sig": record.tech_person_by_sig,
        "tech_person_date": record.tech_person_date,

        "dpt_head_by": record.dpt_head_by,
        "dpt_head_by_sig": record.dpt_head_by_sig,
        "dpt_head_date": record.dpt_head_date,

        "team_lead_by": record.team_lead_by,
        "team_lead_by_sig": record.team_lead_by_sig,
        "team_lead_date": record.team_lead_date,

        "approved_by": record.approved_by,
        "approved_by_sig": record.approved_by_sig,
        "approved_date": record.approved_date,

        "recommended_supplier": record.recommended_supplier,
        "recommended_supplier_reason": record.recommended_supplier_reason,

        "upload_name": record.upload_name,

        "dpt_project_requesting": record.dpt_project_requesting,

        "project_number": record.project_number,
        
        "message":"success","tab":"2"}   

        pdf = render_to_pdf('pages/comparative_schedules/print.html', data)
        return HttpResponse(pdf, content_type='application/pdf')

@login_required(login_url='login')
def comp_schedule_approved(request):
    username = request.user.username
    records = ComparativeSchedule.objects.filter( ~Q(rejector="None")& (  Q(requested_by =username )& ~Q(approved_date="None"))  |  (Q(tech_person_by =username )& ~Q(approved_date="None")) | (Q(dpt_head_by =username )& ~Q(approved_date="None")) | (Q(team_lead_by =username )& ~Q(approved_date="None")) | (Q(approved_by =username )& ~Q(approved_date="None")))
    context = {'records':records ,"tab":"2"}
    return render(request, 'pages/comparative_schedules/list_approved.html', context)

@login_required(login_url='login')
def comp_schedule_add(request):
    # form = ComparativeSchedule.objects.all()
    context = {'form':"form" ,"tab":"2"}
    return render(request, 'pages/comparative_schedules/add.html', context)

@login_required(login_url='login')
@csrf_exempt
@app.route("/send_record")
def comp_schedule_send_record(request):

    with app.app_context():
        try:
          import os
          app.config['UPLOAD_FOLDER'] = "/uploads"
          purchase_request= request.POST.get('purchase_request',default=None)
          #initialize quotations
          pdf1,pdf = CompScheduleQuotation.objects.get_or_create(

          
          request_id = "0",
          quote1_path= "#",
          quote2_path= "#",
          quote3_path= "#",


        )


     

          # for filename in  request.FILES.items():
          #   name = request.FILES[filename].name
          #   #printname)

          # upload= request.FILES['upload']
          # #printupload)
          # filename = upload.filename
          # upload.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

          company_name_supplier1= request.POST.get('company_name_supplier1',default=None)
          item_name_supplier1= request.POST.get('item_name_supplier1',default=None)
          desc_supplier1= request.POST.get('desc_supplier1',default=None)
          qnty_supplier1= request.POST.get('qnty_supplier1',default=None) 
          unit_price_supplier1 = request.POST.get('unit_price_supplier1',default=None)
          total_price_supplier1 = request.POST.get('total_price_supplier1',default=None)

          company_name_supplier2= request.POST.get('company_name_supplier2',default=None)
          item_name_supplier2= request.POST.get('item_name_supplier2',default=None)
          desc_supplier2= request.POST.get('desc_supplier2',default=None)
          qnty_supplier2= request.POST.get('qnty_supplier2',default=None) 
          unit_price_supplier2 = request.POST.get('unit_price_supplier2',default=None)
          total_price_supplier2 = request.POST.get('total_price_supplier2',default=None)

          company_name_supplier3= request.POST.get('company_name_supplier3',default=None)
          item_name_supplier3= request.POST.get('item_name_supplier3',default=None)
          desc_supplier3= request.POST.get('desc_supplier3',default=None)
          qnty_supplier3= request.POST.get('qnty_supplier3',default=None) 
          unit_price_supplier3 = request.POST.get('unit_price_supplier3',default=None)
          total_price_supplier3 = request.POST.get('total_price_supplier3',default=None)

          recommended_supplier= request.POST.get('recommended_supplier',default=None)
          recommended_supplier_reason= request.POST.get('recommended_supplier_reason',default=None)

          # service_request= request.POST.get('requested_by',default=None)
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
          record.purchase_request= purchase_request
          record.company_name_supplier1= company_name_supplier1
          record.item_name_supplier1= item_name_supplier1
          record.desc_supplier1= desc_supplier1
          record.qnty_supplier1= qnty_supplier1 
          record.unit_price_supplier1 = unit_price_supplier1
          record.total_price_supplier1= total_price_supplier1

          record.company_name_supplier2= company_name_supplier2
          record.item_name_supplier2= item_name_supplier2
          record.desc_supplier2= desc_supplier2
          record.qnty_supplier2= qnty_supplier2 
          record.unit_price_supplier2 = unit_price_supplier2
          record.total_price_supplier2= total_price_supplier2
        
          record.company_name_supplier3= company_name_supplier3
          record.item_name_supplier3= item_name_supplier3
          record.desc_supplier3= desc_supplier3
          record.qnty_supplier3= qnty_supplier3 
          record.unit_price_supplier3 = unit_price_supplier3
          record.total_price_supplier3= total_price_supplier3

          record.recommended_supplier= recommended_supplier
          record.recommended_supplier_reason= recommended_supplier_reason
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

          return JsonResponse( {'message':"success",'id':record.pk})

        except Exception as e  :
            f= open("service2.txt","w")
            f.write(str(e))
            f.close()
            return JsonResponse({'message':"failed","tab":"1"})

@login_required(login_url='login')
@csrf_exempt
def comp_schedule_get_record(request):
    context={}
    if request.method == "POST":

      try:
        _id = request.POST.get('id',default=None)
        pdf = CompScheduleQuotation.objects.get(id=1)

        try:
          pdf = CompScheduleQuotation.objects.get(request_id=_id)
        except Exception as e:
          # #printstr(e))
          pass
        # record = PaymentRequest.objects.get(id=_id)

        record = ComparativeSchedule.objects.get(id=_id)
        # #printrecord.upload_name)
        dic = {
      "pdf1":"/procurement"+pdf.quote1_path,
      "pdf2":"/procurement"+pdf.quote2_path,
      "pdf3":"/procurement"+pdf.quote3_path,

      "message":"success",
      "request_id":record.id,
      "rejector":record.rejector,
      "rejector_date":record.rejector_date,
      "rejector_message":record.rejector_message,

      "purchase_request":record.purchase_request,

      "company_name_supplier1":record.company_name_supplier1,
      "item_name_supplier1":record.item_name_supplier1,
      "desc_supplier1":record.desc_supplier1,
      "qnty_supplier1":record.qnty_supplier1,
      "unit_price_supplier1":record.unit_price_supplier1,
      "total_price_supplier1":record.total_price_supplier1,

      "company_name_supplier2":record.company_name_supplier2,
      "item_name_supplier2":record.item_name_supplier2,
      "desc_supplier2":record.desc_supplier2,
      "qnty_supplier2":record.qnty_supplier2,
      "unit_price_supplier2":record.unit_price_supplier2,
      "total_price_supplier2":record.total_price_supplier2,

      "company_name_supplier3":record.company_name_supplier3,
      "item_name_supplier3":record.item_name_supplier3,
      "desc_supplier3":record.desc_supplier3,
      "qnty_supplier3":record.qnty_supplier3,
      "unit_price_supplier3":record.unit_price_supplier3,
      "total_price_supplier3":record.total_price_supplier3,

      "recommended_supplier":record.recommended_supplier,
      "recommended_supplier_reason":record.recommended_supplier_reason,

      "requested_by":record.requested_by,
      "requested_by_sig":record.requested_by_sig,
      "requested_by_date":record.requested_by_date,

      "tech_person_by":record.tech_person_by,
      "tech_person_by_sig":record.tech_person_by_sig,
      "tech_person_date":record.tech_person_date,

      "dpt_head_by":record.dpt_head_by,
      "dpt_head_by_sig":record.dpt_head_by_sig,
      "dpt_head_date":record.dpt_head_date,
      "purchase_request":record.purchase_request,



      "approved_by":record.approved_by,
      "approved_by_sig":record.approved_by_sig,
      "approved_date":record.approved_date,
    }
        return JsonResponse(dic)

      except Exception as e:
        return JsonResponse(str(e),safe=False)

    else:
        return redirect('/procurement/comp_schedule')





login_required(login_url='login')
@csrf_exempt
def comp_schedule_approve(request):
    if request.method == "POST":
      
      _id = request.POST.get('id',default=None)
      head = request.POST.get('head',default=None)
      username = request.user.username
        # objs = Record.objects.get(id=_id)
      record = ComparativeSchedule.objects.get(id=_id)

      if record.rejector != "None":
        return JsonResponse( {'message':"cannot approve a rejected record","tab":"1"})

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




      return JsonResponse( {'message':"success","tab":"1"})
    else:
      return render(request, 'pages/payment_requests/list.html', {})



login_required(login_url='login')
@csrf_exempt
def comp_schedule_approve_head(request):
    if request.method == "POST":
      
      _id = request.POST.get('id',default=None)
      chair = request.POST.get('chair',default=None)

        # objs = Record.objects.get(id=_id)
      record = ComparativeSchedule.objects.get(id=_id)

      if record.rejector != "None":
        return JsonResponse( {'message':"cannot approve a rejected record","tab":"1"})

      username = request.user.username
      record.dpt_head_by = username
      record.approved_by = chair

      d = datetime.datetime.now()
          # record.date_of_request = "{:%B %d, %Y  %H:%M:%S}".format(d)
      record.dpt_head_date= "{:%B %d, %Y  %H:%M:%S}".format(d)


      if chair == "None":
         pass
      else:
        notice = Notifications()
        notice.to = chair
        notice.message = " "+ username +" updated a Comparative schedule\n and assigned you as the PI for you to approve."
        notice.date_time = "{:%B %d, %Y  %H:%M:%S}".format(d)
        notice.trigger = username
        notice.save()

      # if lead == "None":
      #    pass
      # else:
      #   notice = Notifications()
      #   notice.to = lead
      #   notice.message = " "+ username +" updated a Comparative schedule\n and assigned you as the Coordinator for you to approve."
      #   notice.date_time = "{:%B %d, %Y  %H:%M:%S}".format(d)
      #   notice.trigger = username
      #   notice.save()

      record.save()

      return JsonResponse( {'message':"success","tab":"1"})

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

      if record.rejector != "None":
        return JsonResponse( {'message':"cannot approve a rejected record","tab":"1"})
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




      return JsonResponse( {'message':"success","tab":"1"})

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

      if record.rejector != "None":
        return JsonResponse( {'message':"cannot approve a rejected record","tab":"1"})
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



      return JsonResponse( {'message':"success","tab":"1"})

    else:
      return render(request, 'pages/payment_requests/list.html', {})

login_required(login_url='login')
def comp_schedule_open_record(request):
    if request.method == "POST":
      
      _id = request.POST.get('id',default=None)

        # objs = Record.objects.get(id=_id)
      record = ComparativeSchedule.objects.get(id=_id)
      context = {'record':record ,"tab":"2"}
      # #print"IN POST")
      return render(request, 'pages/comparative_schedules/view_record.html', context)
    else:
       redirect("/procurement/comp_schedule_all")


@login_required(login_url='login')
def comp_schedule_pending_view(request):
    if request.method == "POST":
      
      _id = request.POST.get('id',default=None)

        # objs = Record.objects.get(id=_id)
      record = ComparativeSchedule.objects.get(id=_id)
      context = {'record':record ,"tab":"2"}

      # #print"IN POST")

      if record.tech_person_date == "None" and record.tech_person_by == request.user.username and record.rejector == "None":
        #  #print"certified")
         return render(request, 'pages/comparative_schedules/tech_approve.html', context)
      
      elif record.dpt_head_date == "None" and record.dpt_head_by == request.user.username and record.rejector == "None":
        #  #print"cleared")

         return render(request, 'pages/comparative_schedules/head_approve.html', context)
      

      elif record.team_lead_date == "None" and record.team_lead_by != "None" and record.team_lead_by == request.user.username and record.rejector == "None":
        #  #print"approved")

         return render(request, 'pages/comparative_schedules/lead_approve.html', context)
      
      
      elif record.approved_date == "None" and record.approved_by != "None" and record.approved_by == request.user.username and record.rejector == "None": 
        #  #print"approved")

         return render(request, 'pages/comparative_schedules/pi_approve.html', context)
      else:
        return render(request, 'pages/comparative_schedules/not_auth.html', {})


@login_required(login_url='login')
def comp_schedule_pending(request):
    username = request.user.username
    records = ComparativeSchedule.objects.filter(Q(rejector="None") &( ( Q(approved_by=username) & Q (approved_date="None")) | (Q(dpt_head_by=username) & Q (dpt_head_date="None")) | (Q(team_lead_by=username) & Q (team_lead_date="None")) | (Q(tech_person_by=username) & Q (tech_person_date="None")) ))
    context = {'records':records ,"tab":"2"}
    return render(request, 'pages/comparative_schedules/list_pending.html', context)

@login_required(login_url='login')
def comp_schedule_quotes_upload(request):
    if request.method == 'POST' and request.FILES['quote1'] and request.FILES['quote2'] and request.FILES['quote3']:
        myfile1 = request.FILES['quote1']
        myfile2 = request.FILES['quote2']
        myfile3 = request.FILES['quote3']

        request_id = request.POST.get('request_id')
        
        import os
        path = "uploads/comp_schedules/"+str(request_id)
        # Check whether the specified path exists or not
        #print"path ",path)
        isExist = os.path.exists(path)
        if not isExist:

          # Create a new directory because it does not exist
          os.makedirs(path)



        fs = FileSystemStorage()
        filename1 = fs.save(path+"/"+myfile1.name, myfile1)
        uploaded_file_url1 = fs.url(filename1)

        filename2 = fs.save(path+"/"+myfile2.name, myfile2)
        uploaded_file_url2 = fs.url(filename2)

        filename3 = fs.save(path+"/"+myfile3.name, myfile3)
        uploaded_file_url3 = fs.url(filename3)

        record = CompScheduleQuotation()
        record.request_id = request_id
        record.quote1_path = uploaded_file_url1
        record.quote2_path = uploaded_file_url2
        record.quote3_path = uploaded_file_url3

        record.save()
        return redirect('/procurement/comp_schedule')
    else:
          return render(request, 'pages/comparative_schedules/upload_quote.html')



@login_required(login_url='login')
@csrf_exempt
def comp_schedule_reject(request):
    if request.method == "POST":
      
      _id = request.POST.get('id',default=None)
      message = request.POST.get('message',default=None)
      username = request.user.username
        # objs = Record.objects.get(id=_id)
      record = ComparativeSchedule.objects.get(id=_id)
      record.rejector = username
      record.rejector_message = message

      d = datetime.datetime.now()
          # record.date_of_request = "{:%B %d, %Y  %H:%M:%S}".format(d)
      record.rejector_date= "{:%B %d, %Y  %H:%M:%S}".format(d)
      notice = Notifications()
      notice.to = record.requested_by
      record.save()

  
      notice.message = " "+ username +" has rejected your Purchse Request."
      notice.date_time = "{:%B %d, %Y  %H:%M:%S}".format(d)
      notice.trigger = username
      notice.save()
      return JsonResponse( {'message':"success","tab":"1"})
    else:
      return render(request, 'pages/purchase_requests/list.html', {})
   

# ***********************************************************************************************************************

# ***********************************************************************************************************************
# payment request



@login_required(login_url='login')
@csrf_exempt
def payment_request_reject(request):
    if request.method == "POST":
      
      _id = request.POST.get('id',default=None)
      message = request.POST.get('message',default=None)
      username = request.user.username
        # objs = Record.objects.get(id=_id)
      record = PaymentRequest.objects.get(id=_id)
      record.rejector = username
      record.rejector_message = message

      d = datetime.datetime.now()
          # record.date_of_request = "{:%B %d, %Y  %H:%M:%S}".format(d)
      record.rejector_date= "{:%B %d, %Y  %H:%M:%S}".format(d)
      notice = Notifications()
      notice.to = record.compiled_by
      record.save()

  
      notice.message = " "+ username +" has rejected your Purchse Request."
      notice.date_time = "{:%B %d, %Y  %H:%M:%S}".format(d)
      notice.trigger = username
      notice.save()
      return JsonResponse( {'message':"success","tab":"1"})
    else:
      return render(request, 'pages/purchase_requests/list.html', {})
   



@login_required(login_url='login')
@csrf_exempt
def get_payment_requests(request):

   try:
      dic = {}
      # User = get_user_model()
      schedules = PaymentRequest.objects.filter(  ~Q(cleared_by_fin_man_date="None")   )


      for schedule in schedules: 
          dic[schedule.id]= "ID : "+str(schedule.id) +", raised by :"+ schedule.compiled_by+", raised on "+schedule.date_of_request +", amount : "+ schedule.amount
      return JsonResponse(dic)
   except Exception as e:
          #printstr(e))
          return JsonResponse(str(e))


@login_required(login_url='login')
def payment_request_all(request):
    username = request.user.username
    user_id = request.user.id
    records = PaymentRequest.objects.filter( Q(compiled_by=username) | Q(certified_by= username)  | Q(cleared_by_fin_man=username))
    context = {'records':records ,"tab":"4"}
    return render(request, 'pages/payment_requests/list2.html', context)


@login_required(login_url='login')
def payment_request_completed(request):
    username = request.user.username
    user_id = request.user.id
    records = PaymentRequest.objects.filter( Q( Q(completed="1") & Q(accepted_by_date="None")) )  



    context = {'records':records ,"tab":"4"}
    return render(request, 'pages/payment_requests/list_completed.html', context)

@login_required(login_url='login')
def payment_request_pop_upload(request):
    if request.method == 'POST' and request.FILES['quote1']:
        myfile1 = request.FILES['quote1']
        request_id = request.POST.get('request_id')

        
        import os
        path = "uploads/payment_requests/pops/"+str(request_id)
        # Check whether the specified path exists or not
        # #print"path ",path)
        isExist = os.path.exists(path)
        if not isExist:

          # Create a new directory because it does not exist
          os.makedirs(path)



        fs = FileSystemStorage()
        filename1 = fs.save(path+"/"+myfile1.name, myfile1)
        uploaded_file_url1 = fs.url(filename1)




        record = PaymentRequestPOP()
        record.request_id = request_id
        record.quote_path1 = uploaded_file_url1
        record.save()

        rec = PaymentRequest.objects.get(id=request_id)
        rec.completed = "1"
        rec.save()

        return redirect('/procurement/payment_request')
    else:
          return render(request, 'pages/payment_requests/upload_pop.html')




@login_required(login_url='login')
def payment_request_voucher_upload(request):
    if request.method == 'POST' and request.FILES['quote']:
        myfile1 = request.FILES['quote']
        request_id = request.POST.get('request_id')
        
        import os
        path = "uploads/payment_requests/vouchers/"+str(request_id)
        # Check whether the specified path exists or not
        # #print"path ",path)
        isExist = os.path.exists(path)
        if not isExist:

          # Create a new directory because it does not exist
          os.makedirs(path)



        fs = FileSystemStorage()
        filename1 = fs.save(path+"/"+myfile1.name, myfile1)
        uploaded_file_url1 = fs.url(filename1)




        record = PaymentRequestQuotation()
        record.request_id = request_id
        record.quote_path = uploaded_file_url1
        record.save()
        return redirect('/procurement/payment_request')
    else:
          return render(request, 'pages/payment_requests/upload_quote.html')



@login_required(login_url='login')
def payment_request_delivery_note_upload(request):
    if request.method == 'POST' and request.FILES['quote']:
        myfile1 = request.FILES['quote']
        request_id = request.POST.get('request_id')
        
        import os
        path = "uploads/payment_requests/delivery_note/"+str(request_id)
        # Check whether the specified path exists or not
        # #print"path ",path)
        isExist = os.path.exists(path)
        if not isExist:

          # Create a new directory because it does not exist
          os.makedirs(path)



        fs = FileSystemStorage()
        filename1 = fs.save(path+"/"+myfile1.name, myfile1)
        uploaded_file_url1 = fs.url(filename1)




        record = PaymentRequestQuotation()
        record.request_id = request_id
        record.quote_path = uploaded_file_url1
        record.save()
        return redirect('/procurement/payment_request')
    else:
          return render(request, 'pages/payment_requests/upload_quote.html')




@login_required(login_url='login')
def payment_request_quote_and_dnote_upload(request):
    if request.method == 'POST' and request.FILES['quote1'] and request.FILES['quote2']:
        myfile1 = request.FILES['quote1']
        myfile2 = request.FILES['quote2']

        request_id = request.POST.get('request_id')
        
        import os
        path1 = "uploads/payment_requests/quotations/"+str(request_id)
        path2 = "uploads/payment_requests/delivery_notes/"+str(request_id)

        # Check whether the specified path exists or not
        #print"path ",path1)
        isExist1 = os.path.exists(path1)
        if not isExist1:

          # Create a new directory because it does not exist
          os.makedirs(path1)

        isExist2 = os.path.exists(path2)
        if not isExist2:

          # Create a new directory because it does not exist
          os.makedirs(path2)


        fs = FileSystemStorage()
        filename1 = fs.save(path1+"/"+myfile1.name, myfile1)
        uploaded_file_url1 = fs.url(filename1)

        fs2 = FileSystemStorage()
        filename2 = fs.save(path2+"/"+myfile2.name, myfile2)
        uploaded_file_url2 = fs.url(filename2)


        record = PaymentRequestQuotation1()
        record.request_id = request_id
        record.quote_path1 = uploaded_file_url1
        record.quote_path2 = uploaded_file_url2

        record.save()
        return redirect('/procurement/payment_request')
    else:
          return render(request, 'pages/payment_requests/upload_delivery_note.html')


@login_required(login_url='login')
def payment_request_quote_upload(request):
    if request.method == 'POST' and request.FILES['quote']:
        myfile1 = request.FILES['quote']
        request_id = request.POST.get('request_id')
        
        import os
        path = "uploads/payment_requests/quotations/"+str(request_id)
        # Check whether the specified path exists or not
        #print"path ",path)
        isExist = os.path.exists(path)
        if not isExist:

          # Create a new directory because it does not exist
          os.makedirs(path)



        fs = FileSystemStorage()
        filename1 = fs.save(path+"/"+myfile1.name, myfile1)
        uploaded_file_url1 = fs.url(filename1)




        record = PaymentRequestQuotation()
        record.request_id = request_id
        record.quote_path1 = uploaded_file_url1
        record.save()
        return redirect('/procurement/payment_request')
    else:
          return render(request, 'pages/payment_requests/upload_quote.html')

@login_required(login_url='login')
def payment_request(request):
    form = PaymentRequest.objects.all()
    context = {'form':form }
    return render(request, 'pages/payment_requests/payment_requests.html', context)


@login_required(login_url='login')
def payment_request_open_approved(request):
      if request.method == "POST":

          _id = request.POST.get('id',default=None)
          record = PaymentRequest.objects.get(id=_id)
          #print" posted")

          return render(request, 'pages/payment_requests/view_approved.html', context={"record":record,"tab":"4"})
      else:
         #print"not post")
         return redirect("/procurement/payment_request_approved")



@login_required(login_url='login')
def payment_request_kas_completed(request):
      if request.method == "POST":

          _id = request.POST.get('id',default=None)
          record = PaymentRequest.objects.get(id=_id)
          #print" posted")

          return render(request, 'pages/payment_requests/view_completed.html', context={"record":record,"tab":"4"})
      else:
         #print"not post")
         return redirect("/procurement/payment_request_completed")


@login_required(login_url='login')
def payment_request_view(request):
    if request.method == "POST":
      
      _id = request.POST.get('id',default=None)

        # objs = Record.objects.get(id=_id)
      record = PaymentRequest.objects.get(id=_id)
      context = {'record':record,"tab":"4"}
      #print"IN POST")
      if record.certified_by_date == "None" and record.certified_by == request.user.username and record.rejector == "None":
         #print"certified")
         return render(request, 'pages/payment_requests/certify.html', context)
      
      elif record.cleared_by_fin_man_date == "None" and record.cleared_by_fin_man == request.user.username and record.rejector =="None":
         #print"cleared")

         return render(request, 'pages/payment_requests/clear.html', context)
      
      elif record.approved_by_date == "None" and record.approved_by == request.user.username and record.rejector == "None":
         #print"approved")

         return render(request, 'pages/payment_requests/approve.html', context)
      else:
         return redirect("/procurement/payment_request_pending")
      
@login_required(login_url='login')
def payment_request_edit_options(request):
    if request.method == "POST":
      
      _id = request.POST.get('id',default=None)

        # objs = Record.objects.get(id=_id)
      record = PaymentRequest.objects.get(id=_id)
      context = {'record':record,"tab":"4"}
      #print"IN POST")
      if record.cleared_by_fin_man_date == "None" and record.cleared_by_fin_man_date == request.user.username and record.rejector == "None":
         #print"certified")
         return render(request, 'pages/payment_requests/pi.html', context)
      
      elif record.approved_by_project_man_date == "None" and record.approved_by_project_man_date == request.user.username and record.rejector == "None":
         #print"cleared")

         return render(request, 'pages/payment_requests/clerk.html', context)
      else:
         return render(request, 'pages/comparative_schedules/not_auth.html', {})
      

    else:
         return redirect("/procurement/purchase_request_pending")


@login_required(login_url="login")
def payment_request_open_record(request):
    if request.method == "POST":
      finance = False

      # user = request.user
    
    # Get the groups the user belongs to
      # groups = user.groups.all()


      _id = request.POST.get('id',default=None)
      # if request.user.groups.all()[0].name == "finance":
      #     finance = True
        # objs = Record.objects.get(id=_id)
      record = PaymentRequest.objects.get(id=_id)
      context = {'record':record, "finance":finance ,"tab":"4"}
      #print"finance",finance)
      return render(request, 'pages/payment_requests/view_record.html', context)
    else:
       redirect("/procurement/payment_request_all")


# def payment_request_view2(request):
#     if request.method == "POST":
      
#       _id = request.POST.get('id',default=None)

#         # objs = Record.objects.get(id=_id)
#       record = PaymentRequest.objects.get(id=_id)
#       context = {'record':record}
#       #print"IN POST")
#       return render(request, 'pages/payment_requests/view2.html', context)
#     else:
#        redirect("/procurement/payment_request_all")

@login_required(login_url='login')
def payment_request_pending_view(request):
    if request.method == "POST":
      
      _id = request.POST.get('id',default=None)

        # objs = Record.objects.get(id=_id)
      record = PaymentRequest.objects.get(id=_id)
      context = {'record':record,"tab":"4"}

      #print"IN POST")
      if record.certified_by_date == "None" and record.certified_by == request.user.username and record.rejector == "None":
         #print"certified")
         return render(request, 'pages/payment_requests/certify.html', context)
      elif record.cleared_by_fin_man_date == "None" and record.cleared_by_fin_man == request.user.username and record.rejector == "None":
         #print"cleared")

         return render(request, 'pages/payment_requests/clear.html', context)
      
      elif record.approved_by_date == "None" and record.approved_by == request.user.username and record.rejector == "None":
         #print"approved")

         return render(request, 'pages/payment_requests/approve.html', context)


    else:
      return render(request, 'pages/payment_requests/list2.html', {})


@login_required(login_url='login')
@csrf_exempt
def payment_request_print(request):
    # if request.method == "POST":
        current_url = request.path
        x= current_url.split("/")[-1]
        #printx)

        # _id = request.POST.get(x)
        # #print_id)

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
        
        "message":"success","tab":"1"}   


        pdf = render_to_pdf('pages/payment_requests/print.html', data)
        return HttpResponse(pdf, content_type='application/pdf')

    # if request.method == "POST":
    #   _id = request.POST.get('id',default=None)

      
    #   #printcurrent_url)

    #   l = current_url.split('/')
    #   #printl)

      

    #   record = PaymentRequest.objects.filter(id=x)
    #   context = {'record':record}
    #   return render(request, 'pages/payment_requests/print.html', context)
@login_required(login_url='login')
def payment_request_super(request):
    records = PaymentRequest.objects.all()
    context = {'records':records,"tab":"4"}
    return render(request, 'pages/payment_requests/list2.html', context)

@login_required(login_url='login')
def payment_request_edit(request):
    form = PaymentRequest.objects.all()
    context = {'form':form,"tab":"4"}
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
      context = {'record':record,"tab":"4"}
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
      context = {'record':record,"tab":"4"}
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




#       return JsonResponse( {'message':"success","tab":"1"})

#     else:
#       return render(request, 'pages/payment_requests/list.html', {})



@login_required(login_url='login')
def payment_request_pending_approval(request):
    records = PaymentRequest.objects.filter(Q(rejector="None")&Q(approved_by="None"))
    context = {'records':records,"tab":"4"}
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





#       return JsonResponse( {'message':"success","tab":"1"})

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

        if record.rejector != "None":
          return JsonResponse( {'message':"cannot approve a rejected record","tab":"1"})

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

        return JsonResponse( {'message':"success","tab":"1"})
      else:
        return render(request, 'pages/payment_requests/list.html', {})

    except:
       return JsonResponse( {'message':"failed","tab":"1"})

@login_required(login_url='login')
@csrf_exempt
def payment_request_clear(request):
    
    try:
      if request.method == "POST":
        
        _id = request.POST.get('id',default=None)

          # objs = Record.objects.get(id=_id)
        record = PaymentRequest.objects.get(id=_id)

        if record.rejector != "None":
          return JsonResponse( {'message':"cannot approve a rejected record","tab":"1"})
        record.cleared_by_fin_man = request.user.username
        d = datetime.datetime.now()
            # record.date_of_request = "{:%B %d, %Y  %H:%M:%S}".format(d)
        record.cleared_by_fin_man_date= "{:%B %d, %Y  %H:%M:%S}".format(d)

        record.save()

        notice = Notifications()
        notice.to = record.compiled_by
        notice.message = " "+ request.user.username +" updated a Payement Request\n and assigned you as the Approver."
        notice.date_time = "{:%B %d, %Y  %H:%M:%S}".format(d)
        notice.trigger = request.user.username
        notice.save()

        return JsonResponse( {'message':"success","tab":"1"})
      else:
        return render(request, 'pages/payment_requests/list.html', {})


    except Exception as e:
       return JsonResponse( {'message':str(e),"tab":"1"})


@login_required(login_url='login')
@csrf_exempt
def payment_request_approve(request):
    
    try:
      if request.method == "POST":
        
        _id = request.POST.get('id',default=None)

          # objs = Record.objects.get(id=_id)
        record = PaymentRequest.objects.get(id=_id)

        if record.rejector != "None":
          return JsonResponse( {'message':"cannot approve a rejected record","tab":"1"})
        record.approved_by = request.user.username
        # record.certified_by_date = request.user.username
        d = datetime.datetime.now()
            # record.date_of_request = "{:%B %d, %Y  %H:%M:%S}".format(d)
        record.approved_by_date= "{:%B %d, %Y  %H:%M:%S}".format(d)
        record.completed="1"



        notice = Notifications()
        notice.to = record.compiled_by
        record.save()

        notice.message = " "+ request.user.username +" Approved your Payment Request."
        notice.date_time = "{:%B %d, %Y  %H:%M:%S}".format(d)
        notice.trigger = request.user.username
        notice.save()

        return JsonResponse( {'message':"success","tab":"1"})
      else:
        return render(request, 'pages/payment_requests/list.html', {})


    except:
       return JsonResponse( {'message':"failed","tab":"1"})

@login_required(login_url='login')
def payment_request_pending(request):
    username = request.user.username
    records = PaymentRequest.objects.filter( Q(rejector="None") & (Q(certified_by=username) & Q (certified_by_date="None")) | (Q(cleared_by_fin_man=username) & Q (cleared_by_fin_man_date="None")))
    context = {'records':records,"tab":"4"}
    return render(request, 'pages/payment_requests/list_pending.html', context)


@login_required(login_url='login')
def payment_request_approved(request):
    username = request.user.username

    records = PaymentRequest.objects.filter( (Q(certified_by=username) & ~Q(cleared_by_fin_man_date="None") ) | (Q(compiled_by=username) & ~Q(cleared_by_fin_man_date="None") )  | (Q(cleared_by_fin_man=username) & ~Q(cleared_by_fin_man_date="None") )  )
    context = {'records':records,"tab":"4"}
    return render(request, 'pages/payment_requests/list_approved.html', context)

# @login_required(login_url='login')
# def payment_request_completed(request):
#     username = request.user.username

#     records = PaymentRequest.objects.filter( (Q(approved_by=username) & ~Q(approved_by_date="None") ) | (Q(compiled_by=username) & ~Q(approved_by_date="None") ) |  (Q(certified_by=username) & ~Q(approved_by_date="None") ) | (Q(cleared_by_fin_man=username) & ~Q(approved_by_date="None") )  )
#     context = {'records':records}
#     return render(request, 'pages/payment_requests/list_completed.html', context)


@login_required(login_url='login')
def payment_request_add(request):
    
    form = PaymentRequest.objects.all()
    context = {'form':form,"tab":"4"}
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
def get_comp_schedules(request):
   try:
      dic = {}
      # User = get_user_model()
      schedules = ComparativeSchedule.objects.filter(~Q(approved_date = "None"))

      for schedule in schedules: 
          dic[schedule.id]= " : raised by "+ schedule.requested_by+" : raised on "+schedule.requested_by_date
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

        pdf = PaymentRequestQuotation.objects.get(id=1)
        pop = PaymentRequestPOP.objects.get(id=1)
        try:
          if record.type_of_payment == "post" or record.type_of_payment == "cod":
              pdf = PaymentRequestQuotation1.objects.get(request_id=_id)
          else:
              pdf = PaymentRequestQuotation.objects.get(request_id=_id)

        except:
          pass

        try:
              pop = PaymentRequestPOP.objects.get(request_id=_id)


        except:
          pass

        dic = {
           
          "pdf1":"/procurement"+pdf.quote_path1,
          "pdf2":"/procurement"+pdf.quote_path2,
          "pop":"/procurement"+pop.quote_path1,

          "purchase_id": record.purchase_id,
          "request_id": record.id,
      "rejector":record.rejector,
      "rejector_date":record.rejector_date,
      "rejector_message":record.rejector_message,
          "date_of_request": record.date_of_request,
          "payee": record.payee,
          "payment_type": record.payment_type,
          "amount": record.amount,
          "compiled_by": record.compiled_by,
          "compiled_by_date": record.date_of_request,

          "details": record.details,
          "qnty": record.qnty,
          "type_of_payment ": record.type_of_payment,
          "total": record.total,

          "certified_by": record.certified_by,
          "certified_by_date": record.certified_by_date,

          "cleared_by_fin_man": record.cleared_by_fin_man,
          "cleared_by_fin_man_date": record.cleared_by_fin_man_date,


          "accepted_by": record.accepted_by,
          "accepted_by_date": record.accepted_by_date,

          "message":"success",
        }
        context = {'addTabActive': True, "record":"","tab":"1"}
        return JsonResponse(dic)
    else:
        return redirect('/procurement/payment_requests')

@login_required(login_url='login')
@csrf_exempt
@app.route("/send_record")
def payment_request_send_record(request):

    with app.app_context():
        try:
           

          payee= request.POST.get('payee',default=None)
          payment_type= request.POST.get('payment_type',default=None)
          amount= request.POST.get('amount',default=None)

          details = request.POST.get('details',default=None)
          qnty = request.POST.get('qnty',default=None)
          purchase_order = request.POST.get('purchase_order',default=None)
          total= request.POST.get('total',default=None)

          certified_by= request.POST.get('certified_by',default=None)
          type_of_payment= request.POST.get('type_of_payment',default=None)


          p,p1 = PaymentRequestQuotation.objects.get_or_create(

            request_id = "0",
            quote_path1 ="#",
            quote_path2 = "#",
          )

          p2,p3 = PaymentRequestPOP.objects.get_or_create(

            request_id = "0",
            quote_path1 ="#",
          )
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

          record.details = details
          record.purchase_id = purchase_order
          record.qnty = qnty
          record.total= total

          record.certified_by= certified_by
          record.type_of_payment= type_of_payment

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

          _id = record.pk
          return JsonResponse( {'message':"success",'id':_id})

        except Exception as e  :
            f= open("service1.txt","w")
            f.write(str(e))
            f.close()
            return JsonResponse({'message':"failed","tab":"1"})

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

          if record.rejector != "None":
            return JsonResponse( {'message':"cannot approve a rejected record","tab":"1"})

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



          return JsonResponse( {'message':"success","tab":"1"})

        except Exception as e  :
            f= open("service1.txt","w")
            f.write(str(e))
            f.close()
            return JsonResponse({'message':"failed","tab":"1"})


# ***********************************************************************************************************************

#PAYMENT TICKET

# ************************************************************************************************************************




@login_required(login_url='login')
@csrf_exempt
def payment_request_adopt(request):
    
    try:
      if request.method == "POST":
        
        _id = request.POST.get('id',default=None)

          # objs = Record.objects.get(id=_id)
        record = PaymentRequest.objects.get(id=_id)
        record.accepted_by = request.user.username
        # record.certified_by_date = request.user.username
        d = datetime.datetime.now()
            # record.date_of_request = "{:%B %d, %Y  %H:%M:%S}".format(d)
        record.accepted_by_date= "{:%B %d, %Y  %H:%M:%S}".format(d)

        notice = Notifications()
        notice.to = record.compiled_by
        record.save()

        notice.message = " "+ request.user.username +" adopted your Payment Request."
        notice.date_time = "{:%B %d, %Y  %H:%M:%S}".format(d)
        notice.trigger = request.user.username
        notice.save()

        return JsonResponse( {'message':"success","tab":"1"})
      else:
        return render(request, 'pages/payment_requests/list.html', {})


    except:
       return JsonResponse( {'message':"failed","tab":"1"})


@login_required(login_url='login')
def payment_tickets(request):
    return render(request, 'pages/payment_ticket/payment_tickets.html')

@login_required(login_url='login')
def payment_tickets_all(request):
      username = request.user.username
      records = PaymentTicket.objects.filter(Q(creator = username) )
      context = {"records":records,"tab":"5"}


      return render(request, 'pages/payment_ticket/list.html', context)



@login_required(login_url='login')
def payment_ticket_add(request):
      # username = request.user.username
      # records = PaymentTicket.objects.filter(Q(creator = username) )
      context = {"tab":"5"}


      return render(request, 'pages/payment_ticket/add.html', context)

@login_required(login_url='login')
def payment_ticket_view(request):
      username = request.user.username
      records = PaymentTicket.objects.filter(Q(creator = username) )
      context = {'records':records,"tab":"5"}


      return render(request, 'pages/payment_ticket/list.html', context)

@login_required(login_url='login')
def payment_tickets_completed(request):
      username = request.user.username
      records = PaymentTicket.objects.filter(Q(creator = username) & Q( status="completed"))
      context = {'records':records,"tab":"5"}


      return render(request, 'pages/payment_ticket/list_completed.html', context)

@login_required(login_url='login')
def payment_tickets_pending(request):
      username = request.user.username
      records = PaymentTicket.objects.filter(Q(creator = username) & ~Q(status="completed"))
      context = {'records':records,"tab":"5"}


      return render(request, 'pages/payment_ticket/list_pending.html', context)

@login_required(login_url="login")
def payment_ticket_open_record(request):
    if request.method == "POST":
      finance = False

      # user = request.user
    
    # Get the groups the user belongs to
      # groups = user.groups.all()


      _id = request.POST.get('id',default=None)
      # if request.user.groups.all()[0].name == "finance":
      #     finance = True
        # objs = Record.objects.get(id=_id)
      record = PaymentTicket.objects.get(id=_id)
      context = {'record':record, "finance":finance,"tab":"5"}
      # #print"finance",finance)
      return render(request, 'pages/payment_ticket/view_record.html', context)
    else:
       redirect("/procurement/payment_tickets_all")


@login_required(login_url="login")
def payment_ticket_open_record_for_edit(request):
    if request.method == "POST":
      finance = False

      # user = request.user
    
    # Get the groups the user belongs to
      # groups = user.groups.all()


      _id = request.POST.get('id',default=None)
      # if request.user.groups.all()[0].name == "finance":
      #     finance = True
        # objs = Record.objects.get(id=_id)
      record = PaymentTicket.objects.get(id=_id)
      context = {'record':record, "finance":finance,"tab":"5"}
      # #print"finance",finance)

      return render(request, 'pages/payment_ticket/edit_record.html', context)

    else:
      redirect("/procurement/payment_tickets_all")



@login_required(login_url="login")
@csrf_exempt
def payment_ticket_edit_record(request):
      finance = False

      # user = request.user
    
    # Get the groups the user belongs to
      # groups = user.groups.all()


      _id = request.POST.get('id',default=None)
      status = request.POST.get('status',default=None)

      # if request.user.groups.all()[0].name == "finance":
      #     finance = True
        # objs = Record.objects.get(id=_id)
      record = PaymentTicket.objects.get(id=_id)
      record.status = status
      record.save()
      return JsonResponse({"message":"success","id":record.pk})


@login_required(login_url='login')
@csrf_exempt
def payment_ticket_get_record(request):
    context={}
    if request.method == "POST":
        _id = request.POST.get('id',default=None)

        record = PaymentTicket.objects.get(id=_id)

        pdf = PaymentTicketPOP.objects.get(id=1)

        try:
          pdf = PaymentTicketPOP.objects.get(payment_ticket_id=_id)
        except:
          pass
        dic = {
           

          "pop":"/procurement"+pdf.pop_path,

          "payment_request_id": record.payment_request_id,

          "date_of_ticket": record.date_of_ticket,
          "amount": record.amount,
          "to_name": record.to_name,
          "to_bank_name": record.to_bank_name,
          "to_bank_account": record.to_bank_account,
          "narration": record.narration,


          "creator": record.creator, 
          "status": record.status,

          "message":"success",
        }
        context = {'addTabActive': True, "record":"","tab":"1"}
        return JsonResponse(dic)
    else:
        return redirect('/procurement/payment_tickets')

@login_required(login_url='login')
@csrf_exempt
@app.route("/send_record")
def payment_ticket_send_record(request):

    with app.app_context():
        try:
           

          status= request.POST.get('status',default=None)
          payment_request_id= request.POST.get('request_id',default=None)


          PaymentTicketPOP.objects.get_or_create(
            payment_ticket_id = "0",
            pop_path = "#",

          )

          d = datetime.datetime.now()

          narration= request.POST.get('narration',default=None)
          to_bank_account= request.POST.get('to_bank_account',default=None)

          to_name= request.POST.get('to_name',default=None)
          to_bank_name= request.POST.get('to_bank_name',default=None)

          amount= request.POST.get('amount',default=None)
          # approved_by_date= request.POST.get('approved_by_date',default=None)

          record = PaymentTicket()

          record.creator = request.user.username
          record.status= status


          record.date_of_ticket=  "{:%B %d, %Y  %H:%M:%S}".format(d)
          record.payment_request_id= payment_request_id

          record.amount= amount
          record.to_name= to_name

          record.narration= narration
          record.to_bank_name= to_bank_name

          record.to_bank_account= to_bank_account

          notice = Notifications()
          notice.to= record.creator
          notice.trigger = request.user.username
          notice.message = request.user.username +" has created a Payment ticket for your request"

          d = datetime.datetime.now()
          record.date_of_request = "{:%B %d, %Y  %H:%M:%S}".format(d)
          notice.date_time = "{:%B %d, %Y  %H:%M:%S}".format(d)
          notice.status = "New"
          notice.save()
          # record.approved_by_date= approved_by_date


          record.save()

          _id = record.pk
          return JsonResponse( {'message':"success",'id':_id})

        except Exception as e  :
            f= open("service1.txt","w")
            f.write(str(e))
            f.close()
            return JsonResponse({'message':"failed","tab":"1"})

@login_required(login_url='login')
@csrf_exempt
def payment_ticket_upload_pop(request):
    if request.method == 'POST' and request.FILES['pop']:
        myfile1 = request.FILES['pop']
        request_id = request.POST.get('request_id')
        
        import os
        path = "uploads/payment_tickets/pops/"+str(request_id)
        # Check whether the specified path exists or not
        # #print"path ",path)
        isExist = os.path.exists(path)
        if not isExist:

          # Create a new directory because it does not exist
          os.makedirs(path)



        fs = FileSystemStorage()
        filename1 = fs.save(path+"/"+myfile1.name, myfile1)
        uploaded_file_url1 = fs.url(filename1)




        record = PaymentTicketPOP()
        record.payment_ticket_id = request_id
        record.pop_path = uploaded_file_url1
        record.save()
        return redirect('/procurement/payment_tickets')
    else:
          return render(request, 'pages/payment_ticket/upload_pop.html')



















            
# ***********************************************************************************************************************

#Suppliers 

# ************************************************************************************************************************



@login_required(login_url='login')
@csrf_exempt
def suppliers_reject(request):
    if request.method == "POST":
      
      _id = request.POST.get('id',default=None)
      message = request.POST.get('message',default=None)
      username = request.user.username
        # objs = Record.objects.get(id=_id)
      record = Supplier.objects.get(id=_id)
      record.rejector = username
      record.rejector_message = message

      d = datetime.datetime.now()
          # record.date_of_request = "{:%B %d, %Y  %H:%M:%S}".format(d)
      record.rejector_date= "{:%B %d, %Y  %H:%M:%S}".format(d)
      notice = Notifications()
      notice.to = record.added_by
      record.save()

  
      notice.message = " "+ username +" has rejected your Supplier add ."
      notice.date_time = "{:%B %d, %Y  %H:%M:%S}".format(d)
      notice.trigger = username
      notice.save()
      return JsonResponse( {'message':"success","tab":"7"})
    else:
      return render(request, 'pages/suppliers/list.html', {})
    




@login_required(login_url='login')
def suppliers(request):
    return render(request, 'pages/suppliers/suppliers.html')

@login_required(login_url='login')
def suppliers_all(request):
      username = request.user.username
      records = GoodsReceivedNote.objects.filter(Q(receiver = username) | Q(approver = username) )
      context = {"records":records,"tab":"7"}


      return render(request, 'pages/goods_received/list.html', context)

@login_required(login_url='login')
def suppliers_completed(request):
      username = request.user.username
      records = Supplier.objects.filter(  ~Q(approver_by_date="None") )
      context = {"records":records,"tab":"7"}


      return render(request, 'pages/goods_received/list_completed.html', context)


@login_required(login_url='login')
def suppliers_add(request):
      # username = request.user.username
      # records = PaymentTicket.objects.filter(Q(creator = username) )
      context = {"tab":"7"}


      return render(request, 'pages/suppliers/add.html', context)

@login_required(login_url='login')
def suppliers_view(request):
      username = request.user.username
      records = Supplier.objects.all()
      context = {'records':records, "tab":"7"}


      return render(request, 'pages/suppliers/list.html', context)



@login_required(login_url='login')
def suppliers_pending(request):
      username = request.user.username
      records = Supplier.objects.filter(Q(approved_by = username) & Q(approved_by_date="None"))
      context = {'records':records , "tab":"7"}


      return render(request, 'pages/suppliers/list_pending.html', context)

@login_required(login_url="login")
def suppliers_open_record(request):
    if request.method == "POST":
      finance = False

      # user = request.user
    
    # Get the groups the user belongs to
      # groups = user.groups.all()


      _id = request.POST.get('id',default=None)
      # if request.user.groups.all()[0].name == "finance":
      #     finance = True
        # objs = Record.objects.get(id=_id)
      record = Supplier.objects.get(id=_id)
      context = {'record':record, "finance":finance , "tab":"7"}
      # #print"finance",finance)
      return render(request, 'pages/suppliers/view_record.html', context)
    else:
       redirect("/procurement/suppliers_all")


@login_required(login_url="login")
def suppliers_open_record_for_edit(request):
    if request.method == "POST":
      finance = False

      # user = request.user
    
    # Get the groups the user belongs to
      # groups = user.groups.all()


      _id = request.POST.get('id',default=None)
      # if request.user.groups.all()[0].name == "finance":
      #     finance = True
        # objs = Record.objects.get(id=_id)
      record = Supplier.objects.get(id=_id)
      context = {'record':record, "finance":finance, "tab":"7"}
      # #print"finance",finance)

      return render(request, 'pages/suppliers/edit_record.html', context)

    else:
      redirect("/procurement/suppliers_all")




@login_required(login_url='login')
@csrf_exempt
def suppliers_get_record(request):
    context={}
    if request.method == "POST":
        _id = request.POST.get('id',default=None)

        record = Supplier.objects.get(id=_id)

        pdf = SupplierDocs.objects.get(id=1)

        try:
          pdf = SupplierDocs.objects.get(request_id=_id)
        except:
          pass
        dic = {
           

          "vat_path":"/procurement"+pdf.vat_path,
          "tax_clearance_path":"/procurement"+pdf.tax_clearance_path,
          "profile_path":"/procurement"+pdf.profile_path,
          "certificate_path":"/procurement"+pdf.certificate_path,
          # "pop":"/procurement"+pdf.dnote_path,

          "name": record.name,

          "address": record.address,
          "bank_name": record.bank_name,
          "bank_branch": record.bank_branch,
          "bank_account": record.bank_account,
          "contact_person": record.contact_person,
          "alt_contact_number": record.alt_contact_number,


          "contact_number": record.contact_number, 
          "contact_email": record.contact_email,

          "vat_valid_expiry_date": record.vat_valid_expiry_date, 
          "tax_clearance_expiry_date": record.tax_clearance_expiry_date,

          "added_by": record.added_by, 
          "added_by_date": record.added_by_date,
          "approved_by": record.approved_by, 

          "approved_by_date": record.approved_by_date, 
          "tax_complient": record.tax_complient,

          "evaluated": record.evaluated, 
          "evaluated_by_date": record.evaluated_by_date,
          "evaluation_decision": record.evaluation_decision, 

          "message":"success",
        }
        context = {'addTabActive': True, "record":"","tab":"7"}
        return JsonResponse(dic)
    else:
        return redirect('/procurement/suppliers_all')

@login_required(login_url='login')
@csrf_exempt
@app.route("/send_record")
def suppliers_send_record(request):

    with app.app_context():
        try:
           

          name= request.POST.get('name',default=None)
          address= request.POST.get('address',default=None)
          bank_name= request.POST.get('bank_name',default=None)
          meta_data= request.POST.get('meta_data',default=None)


          SupplierDocs.objects.get_or_create(
            supplier_id = "0",
            vat_path = "#",
            tax_clearance_path = "#",
            profile_path = "#",
            certificate_path = "#",

          )

          d = datetime.datetime.now()

          bank_branch= request.POST.get('bank_branch',default=None)
          bank_account= request.POST.get('bank_account',default=None)

          contact_person= request.POST.get('contact_person',default=None)
          alt_contact_number= request.POST.get('alt_contact_number',default=None)

          contact_number= request.POST.get('contact_number',default=None)
          contact_email= request.POST.get('contact_email',default=None)
          # vat_valid_expiry_date= request.POST.get('vat_valid_expiry_date',default=None)
          tax_clearance_expiry_date= request.POST.get('tax_clearance_expiry_date',default=None)
          tax_complient= request.POST.get('tax_complient',default=None)
          approved_by= request.POST.get('approved_by',default=None)


          record = Supplier()

          record.added_by = request.user.username
          record.name= name


          record.added_by_date=  "{:%B %d, %Y  %H:%M:%S}".format(d)
          record.address= address

          record.bank_name= bank_name
          record.bank_branch= bank_branch

          record.bank_account= bank_account
          record.meta_data= meta_data

          record.contact_person= contact_person
          record.alt_contact_number= alt_contact_number
          record.contact_number= contact_number
          record.contact_email= contact_email
          # record.vat_valid_expiry_date= vat_valid_expiry_date
          record.tax_clearance_expiry_date= tax_clearance_expiry_date

          record.tax_complient= tax_complient
          record.approved_by= approved_by



          notice = Notifications()
          notice.to= record.approved_by
          notice.trigger = request.user.username
          notice.message = request.user.username +" has added a Supplier for you to approve"

          d = datetime.datetime.now()
          notice.date_time = "{:%B %d, %Y  %H:%M:%S}".format(d)
          notice.status = "New"
          notice.save()
          # record.approved_by_date= approved_by_date


          record.save()

          _id = record.pk
          return JsonResponse( {'message':"success",'id':_id})

        except Exception as e  :
            f= open("supplier.txt","w")
            f.write(str(e))
            f.close()
            return JsonResponse({'message':"failed","tab":"1"})

@login_required(login_url='login')
@csrf_exempt
def suppliers_upload_docs(request):
    if request.method == 'POST' and request.FILES['vat'] and request.FILES['profile']and request.FILES['tax'] and request.FILES['cert']:
        myfile1 = request.FILES['vat']
        myfile2 = request.FILES['cert']
        myfile3 = request.FILES['profile']
        myfile4 = request.FILES['tax']

        request_id = request.POST.get('request_id')
        
        import os
        path = "uploads/suppliers/docs/"+str(request_id)
        # Check whether the specified path exists or not
        # #print"path ",path)
        isExist = os.path.exists(path)
        if not isExist:

          # Create a new directory because it does not exist
          os.makedirs(path)



        fs = FileSystemStorage()
        filename1 = fs.save(path+"/"+myfile1.name, myfile1)
        uploaded_file_url1 = fs.url(filename1)

        filename2 = fs.save(path+"/"+myfile2.name, myfile2)
        uploaded_file_url2 = fs.url(filename2)

        filename3 = fs.save(path+"/"+myfile3.name, myfile3)
        uploaded_file_url3 = fs.url(filename3)

        filename4 = fs.save(path+"/"+myfile4.name, myfile4)
        uploaded_file_url4 = fs.url(filename4)



        record = SupplierDocs()
        record.request_id = request_id

        record.vat_path = uploaded_file_url1
        record.tax_clearance_path = uploaded_file_url4
        record.profile_path = uploaded_file_url3
        record.certificate_path = uploaded_file_url2


        record.save()
        return redirect('/procurement/suppliers_all')
    else:
          return render(request, 'pages/suppliers/upload_pop.html')






@login_required(login_url='login')
@csrf_exempt
def suppliers_approve(request):
    
    try:
      if request.method == "POST":
        
        _id = request.POST.get('id',default=None)

        record = Supplier.objects.get(id=_id)
        record.approved_by = request.user.username
        d = datetime.datetime.now()
        record.approved_by_date= "{:%B %d, %Y  %H:%M:%S}".format(d)

        notice = Notifications()
        notice.to = record.added_by
        record.save()

        notice.message = " "+ request.user.username +" approved your Supplier Add."
        notice.date_time = "{:%B %d, %Y  %H:%M:%S}".format(d)
        notice.trigger = request.user.username
        notice.save()

        return JsonResponse( {'message':"success","tab":"7"})

    except Exception as e:
       return JsonResponse( {'message': str(e)})





     
# ***********************************************************************************************************************

#Budget Lines 

# ************************************************************************************************************************



@login_required(login_url='login')
@csrf_exempt
def budget_reject(request):
    if request.method == "POST":
      
      _id = request.POST.get('id',default=None)
      message = request.POST.get('message',default=None)
      username = request.user.username
        # objs = Record.objects.get(id=_id)
      record = Supplier.objects.get(id=_id)
      record.rejector = username
      record.rejector_message = message

      d = datetime.datetime.now()
          # record.date_of_request = "{:%B %d, %Y  %H:%M:%S}".format(d)
      record.rejector_date= "{:%B %d, %Y  %H:%M:%S}".format(d)
      notice = Notifications()
      notice.to = record.added_by
      record.save()

  
      notice.message = " "+ username +" has rejected your Supplier add ."
      notice.date_time = "{:%B %d, %Y  %H:%M:%S}".format(d)
      notice.trigger = username
      notice.save()
      return JsonResponse( {'message':"success","tab":"7"})
    else:
      return render(request, 'pages/suppliers/list.html', {})
    




@login_required(login_url='login')
def budget_lines(request):
    return render(request, 'pages/budget_lines/budgets.html')

@login_required(login_url='login')
def budget_lines_all(request):
      username = request.user.username
      records = BudgetLines.objects.filter(Q(receiver = username) | Q(approver = username) )
      context = {"records":records,"tab":"7"}


      return render(request, 'pages/goods_received/list.html', context)

# @login_required(login_url='login')
# def suppliers_completed(request):
#       username = request.user.username
#       records = Supplier.objects.filter(  ~Q(approver_by_date="None") )
#       context = {"records":records,"tab":"7"}


#       return render(request, 'pages/goods_received/list_completed.html', context)


@login_required(login_url='login')
def budget_lines_add(request):
      # username = request.user.username
      # records = PaymentTicket.objects.filter(Q(creator = username) )
      context = {"tab":"8"}


      return render(request, 'pages/budget_lines/add.html', context)

# @login_required(login_url='login')
# def suppliers_view(request):
#       username = request.user.username
#       records = BudgetLines.objects.all()
#       context = {'records':records, "tab":"8"}


#       return render(request, 'pages/budget/list.html', context)



# @login_required(login_url='login')
# def suppliers_pending(request):
#       username = request.user.username
#       records = Supplier.objects.filter(Q(approved_by = username) & Q(approved_by_date="None"))
#       context = {'records':records , "tab":"7"}


#       return render(request, 'pages/suppliers/list_pending.html', context)

@login_required(login_url="login")
def budget_line_open_record(request):
    if request.method == "POST":
      finance = False

      # user = request.user
    
    # Get the groups the user belongs to
      # groups = user.groups.all()


      _id = request.POST.get('id',default=None)
      # if request.user.groups.all()[0].name == "finance":
      #     finance = True
        # objs = Record.objects.get(id=_id)
      record = BudgetLines.objects.get(id=_id)
      context = {'record':record, "finance":finance , "tab":"8"}
      # #print"finance",finance)
      return render(request, 'pages/suppliers/view_record.html', context)
    else:
       redirect("/procurement/budget_lines_all")


# @login_required(login_url="login")
# def suppliers_open_record_for_edit(request):
#     if request.method == "POST":
#       finance = False

#       # user = request.user
    
#     # Get the groups the user belongs to
#       # groups = user.groups.all()


#       _id = request.POST.get('id',default=None)
#       # if request.user.groups.all()[0].name == "finance":
#       #     finance = True
#         # objs = Record.objects.get(id=_id)
#       record = Supplier.objects.get(id=_id)
#       context = {'record':record, "finance":finance, "tab":"7"}
#       # #print"finance",finance)

#       return render(request, 'pages/suppliers/edit_record.html', context)

#     else:
#       redirect("/procurement/suppliers_all")


@login_required(login_url='login')
@csrf_exempt
def get_budget_lines(request):
   try:
      dic = {}
      # User = get_user_model()
      schedules = BudgetLines.objects.all()

      for schedule in schedules: 
          dic[schedule.id]= schedule.name+", Project : "+ schedule.project +", Department : "+ schedule.dpt+", Balance  : "+schedule.balance
      return JsonResponse(dic)
   except Exception as e:
          return JsonResponse(str(e)) 

@login_required(login_url='login')
@csrf_exempt
def get_departments(request):
   try:
      dic = {}
      # User = get_user_model()
      schedules = Department.objects.all()

      for schedule in schedules: 
          dic[schedule.id]= schedule.name+", Head : "+ schedule.head 
      return JsonResponse(dic)
   except Exception as e:
          return JsonResponse(str(e)) 

@login_required(login_url='login')
@csrf_exempt
def get_projects(request):
   try:
      dic = {}
      # User = get_user_model()
      schedules = Project.objects.all()

      for schedule in schedules: 
          dic[schedule.id]= schedule.name+", Manager : "+ schedule.manager 
      return JsonResponse(dic)
   except Exception as e:
          return JsonResponse(str(e)) 

@login_required(login_url='login')
@csrf_exempt
def get_suppliers(request):
   try:
      dic = {}
      # User = get_user_model()
      schedules = Supplier.objects.filter(~Q(approved_by_date = "None"))

      for schedule in schedules: 
          dic[schedule.id]= schedule.item_name+", Total Cost : "+ schedule.total_cost +", raised by : "+ schedule.compiled_by+", raised on : "+schedule.date+", Supplier : "+schedule.sup_name
      return JsonResponse(dic)
   except Exception as e:
          return JsonResponse(str(e)) 


@login_required(login_url='login')
@csrf_exempt
def budget_line_get_record(request):
    context={}
    if request.method == "POST":
        _id = request.POST.get('id',default=None)

        record = BudgetLines.objects.get(id=_id)

        # pdf = SupplierDocs.objects.get(id=1)

        # try:
        #   pdf = SupplierDocs.objects.get(request_id=_id)
        # except:
        #   pass
        dic = {
           

          # "vat_path":"/procurement"+pdf.vat_path,
          # "tax_clearance_path":"/procurement"+pdf.tax_clearance_path,
          # "profile_path":"/procurement"+pdf.profile_path,
          # "certificate_path":"/procurement"+pdf.certificate_path,
          # "pop":"/procurement"+pdf.dnote_path,

          "name": record.name,

          "project": record.project,
          "code": record.code,
          "amount": record.amount,
          "balance": record.balance,
          "subtract": record.subtract,
          "added_by": record.added_by,


          "added_by_date": record.added_by_date, 

          # "contact_email": record.contact_email,

          # "vat_valid_expiry_date": record.vat_valid_expiry_date, 
          # "tax_clearance_expiry_date": record.tax_clearance_expiry_date,

          # "added_by": record.added_by, 
          # "added_by_date": record.added_by_date,
          # "approved_by": record.approved_by, 

          # "approved_by_date": record.approved_by_date, 
          # "tax_complient": record.tax_complient,

          # "evaluated": record.evaluated, 
          # "evaluated_by_date": record.evaluated_by_date,
          # "evaluation_decision": record.evaluation_decision, 

          "message":"success",
        }
        context = {'addTabActive': True, "record":"","tab":"8"}
        return JsonResponse(dic)
    else:
        return redirect('/procurement/budget_lines_all')

@login_required(login_url='login')
@csrf_exempt
@app.route("/send_record")
def budget_line_send_record(request):

    with app.app_context():
        try:
           

          name= request.POST.get('name',default=None)
          project= request.POST.get('project',default=None)
          code= request.POST.get('code',default=None)
          dpt= request.POST.get('dpt',default=None)


          # SupplierDocs.objects.get_or_create(
          #   supplier_id = "0",
          #   vat_path = "#",
          #   tax_clearance_path = "#",
          #   profile_path = "#",
          #   certificate_path = "#",

          # )

          d = datetime.datetime.now()

          amount= request.POST.get('amount',default=None)

          # contact_person= request.POST.get('contact_person',default=None)
          # alt_contact_number= request.POST.get('alt_contact_number',default=None)

          # contact_number= request.POST.get('contact_number',default=None)
          # contact_email= request.POST.get('contact_email',default=None)
          # vat_valid_expiry_date= request.POST.get('vat_valid_expiry_date',default=None)
          # tax_clearance_expiry_date= request.POST.get('tax_clearance_expiry_date',default=None)
          # tax_complient= request.POST.get('tax_complient',default=None)
          # approved_by= request.POST.get('approved_by',default=None)



          record = BudgetLines()

          record.added_by = request.user.username
          record.name= name


          record.added_by_date=  "{:%B %d, %Y  %H:%M:%S}".format(d)
          record.project= project

          record.code= code
          record.amount= amount

          # record.bank_account= bank_account
          # record.meta_data= meta_data

          # record.contact_person= contact_person
          # record.alt_contact_number= alt_contact_number
          # record.contact_number= contact_number
          # record.contact_email= contact_email
          # record.vat_valid_expiry_date= vat_valid_expiry_date
          # record.tax_clearance_expiry_date= tax_clearance_expiry_date

          # record.tax_complient= tax_complient
          # record.approved_by= approved_by



          notice = Notifications()
          notice.to= record.approved_by
          notice.trigger = request.user.username
          notice.message = request.user.username +" has added a Supplier for you to approve"

          d = datetime.datetime.now()
          notice.date_time = "{:%B %d, %Y  %H:%M:%S}".format(d)
          notice.status = "New"
          notice.save()
          # record.approved_by_date= approved_by_date


          record.save()

          _id = record.pk
          return JsonResponse( {'message':"success",'id':_id})

        except Exception as e  :
            f= open("supplier.txt","w")
            f.write(str(e))
            f.close()
            return JsonResponse({'message':"failed","tab":"1"})

@login_required(login_url='login')
@csrf_exempt
def suppliers_upload_docs(request):
    if request.method == 'POST' and request.FILES['vat'] and request.FILES['profile']and request.FILES['tax'] and request.FILES['cert']:
        myfile1 = request.FILES['vat']
        myfile2 = request.FILES['cert']
        myfile3 = request.FILES['profile']
        myfile4 = request.FILES['tax']

        request_id = request.POST.get('request_id')
        
        import os
        path = "uploads/suppliers/docs/"+str(request_id)
        # Check whether the specified path exists or not
        # #print"path ",path)
        isExist = os.path.exists(path)
        if not isExist:

          # Create a new directory because it does not exist
          os.makedirs(path)



        fs = FileSystemStorage()
        filename1 = fs.save(path+"/"+myfile1.name, myfile1)
        uploaded_file_url1 = fs.url(filename1)

        filename2 = fs.save(path+"/"+myfile2.name, myfile2)
        uploaded_file_url2 = fs.url(filename2)

        filename3 = fs.save(path+"/"+myfile3.name, myfile3)
        uploaded_file_url3 = fs.url(filename3)

        filename4 = fs.save(path+"/"+myfile4.name, myfile4)
        uploaded_file_url4 = fs.url(filename4)



        record = SupplierDocs()
        record.request_id = request_id

        record.vat_path = uploaded_file_url1
        record.tax_clearance_path = uploaded_file_url4
        record.profile_path = uploaded_file_url3
        record.certificate_path = uploaded_file_url2


        record.save()
        return redirect('/procurement/suppliers_all')
    else:
          return render(request, 'pages/suppliers/upload_pop.html')






@login_required(login_url='login')
@csrf_exempt
def suppliers_approve(request):
    
    try:
      if request.method == "POST":
        
        _id = request.POST.get('id',default=None)

        record = Supplier.objects.get(id=_id)
        record.approved_by = request.user.username
        d = datetime.datetime.now()
        record.approved_by_date= "{:%B %d, %Y  %H:%M:%S}".format(d)

        notice = Notifications()
        notice.to = record.added_by
        record.save()

        notice.message = " "+ request.user.username +" approved your Supplier Add."
        notice.date_time = "{:%B %d, %Y  %H:%M:%S}".format(d)
        notice.trigger = request.user.username
        notice.save()

        return JsonResponse( {'message':"success","tab":"7"})

    except Exception as e:
       return JsonResponse( {'message': str(e)})








#***************************************************************************************************************************

#GRN
#***************************************************************************************************************************


@login_required(login_url='login')
@csrf_exempt
def goods_received_notes_reject(request):
    if request.method == "POST":
      
      _id = request.POST.get('id',default=None)
      message = request.POST.get('message',default=None)
      username = request.user.username
        # objs = Record.objects.get(id=_id)
      record = GoodsReceivedNote.objects.get(id=_id)
      record.rejector = username
      record.rejector_message = message

      d = datetime.datetime.now()
          # record.date_of_request = "{:%B %d, %Y  %H:%M:%S}".format(d)
      record.rejector_date= "{:%B %d, %Y  %H:%M:%S}".format(d)
      notice = Notifications()
      notice.to = record.receiver
      record.save()

  
      notice.message = " "+ username +" has rejected your GRN ."
      notice.date_time = "{:%B %d, %Y  %H:%M:%S}".format(d)
      notice.trigger = username
      notice.save()
      return JsonResponse( {'message':"success","tab":"6"})
    else:
      return render(request, 'pages/purchase_requests/list.html', {})
    




@login_required(login_url='login')
def goods_received_notes(request):
    return render(request, 'pages/goods_received/goods_received_notes.html')

@login_required(login_url='login')
def goods_received_notes_all(request):
      username = request.user.username
      records = GoodsReceivedNote.objects.filter(Q(receiver = username) | Q(approver = username) )
      context = {"records":records,"tab":"6"}


      return render(request, 'pages/goods_received/list.html', context)

@login_required(login_url='login')
def goods_received_notes_completed(request):
      username = request.user.username
      records = GoodsReceivedNote.objects.filter( Q(Q(receiver = username) | Q(approver = username)) & ~Q(approver_date="None") )
      context = {"records":records,"tab":"6"}


      return render(request, 'pages/goods_received/list_completed.html', context)


@login_required(login_url='login')
def goods_received_notes_add(request):
      # username = request.user.username
      # records = PaymentTicket.objects.filter(Q(creator = username) )
      context = {"tab":"6"}


      return render(request, 'pages/goods_received/add.html', context)

@login_required(login_url='login')
def goods_received_notes_view(request):
      username = request.user.username
      records = GoodsReceivedNote.objects.filter(Q(receiver = username) )
      context = {'records':records, "tab":"6"}


      return render(request, 'pages/goods_received/list.html', context)



@login_required(login_url='login')
def goods_received_notes_pending(request):
      username = request.user.username
      records = GoodsReceivedNote.objects.filter(Q(approver = username) & Q(approver_date="None"))
      context = {'records':records , "tab":"6"}


      return render(request, 'pages/goods_received/list_pending.html', context)

@login_required(login_url="login")
def goods_received_notes_open_record(request):
    if request.method == "POST":
      finance = False

      # user = request.user
    
    # Get the groups the user belongs to
      # groups = user.groups.all()


      _id = request.POST.get('id',default=None)
      # if request.user.groups.all()[0].name == "finance":
      #     finance = True
        # objs = Record.objects.get(id=_id)
      record = GoodsReceivedNote.objects.get(id=_id)
      context = {'record':record, "finance":finance , "tab":"6"}
      # #print"finance",finance)
      return render(request, 'pages/goods_received/view_record.html', context)
    else:
       redirect("/procurement/goods_received_all")


@login_required(login_url="login")
def goods_received_notes_open_record_for_edit(request):
    if request.method == "POST":
      finance = False

      # user = request.user
    
    # Get the groups the user belongs to
      # groups = user.groups.all()


      _id = request.POST.get('id',default=None)
      # if request.user.groups.all()[0].name == "finance":
      #     finance = True
        # objs = Record.objects.get(id=_id)
      record = GoodsReceivedNote.objects.get(id=_id)
      context = {'record':record, "finance":finance, "tab":"6"}
      # #print"finance",finance)

      return render(request, 'pages/goods_received/edit_record.html', context)

    else:
      redirect("/procurement/goods_received_all")




@login_required(login_url='login')
@csrf_exempt
def goods_received_notes_get_record(request):
    context={}
    if request.method == "POST":
        _id = request.POST.get('id',default=None)

        record = GoodsReceivedNote.objects.get(id=_id)

        pdf = GoodsReceivedNoteDnote.objects.get(id=1)

        try:
          pdf = GoodsReceivedNoteDnote.objects.get(request_id=_id)
        except:
          pass
        dic = {
           

          "pop":"/procurement"+pdf.dnote_path,

          "payment_request": record.payment_request,

          "status": record.status,
          "purchase_order": record.purchase_order,
          "item_name": record.item_name,
          "supplier": record.supplier,
          "dpt": record.dpt,
          "desc": record.desc,


          "qnty": record.qnty, 
          "serial": record.serial,

          "comments": record.comments, 
          "receiver": record.receiver,

          "approver": record.approver, 
          "receiver_date": record.receiver_date,
          "approver_date": record.approver_date, 


          "message":"success",
        }
        context = {'addTabActive': True, "record":"","tab":"1"}
        return JsonResponse(dic)
    else:
        return redirect('/procurement/goods_received')

@login_required(login_url='login')
@csrf_exempt
@app.route("/send_record")
def goods_received_notes_send_record(request):

    with app.app_context():
        try:
           

          status= request.POST.get('status',default=None)
          payment_request_id= request.POST.get('request_id',default=None)
          purchase_order= request.POST.get('purchase_order',default=None)


          GoodsReceivedNoteDnote.objects.get_or_create(
            request_id = "0",
            dnote_path = "#",

          )

          d = datetime.datetime.now()

          supplier= request.POST.get('supplier',default=None)
          dpt= request.POST.get('dpt',default=None)

          item_name= request.POST.get('item_name',default=None)
          desc= request.POST.get('desc',default=None)

          qnty= request.POST.get('qnty',default=None)
          serial= request.POST.get('serial',default=None)
          qnty= request.POST.get('qnty',default=None)
          comments= request.POST.get('comments',default=None)
          receiver= request.POST.get('receiver',default=None)
          approver= request.POST.get('approver',default=None)



          record = GoodsReceivedNote()

          record.receiver = request.user.username
          record.status= status


          record.receiver_date=  "{:%B %d, %Y  %H:%M:%S}".format(d)
          record.payment_request= payment_request_id

          record.purchase_order= purchase_order
          record.item_name= item_name

          record.supplier= supplier
          record.dpt= dpt

          record.desc= desc
          record.qnty= qnty
          record.serial= serial
          record.comments= comments
          record.approver= approver
          record.supplier= supplier

          notice = Notifications()
          notice.to= record.receiver
          notice.trigger = request.user.username
          notice.message = request.user.username +" has created a GRN for you to sign"

          d = datetime.datetime.now()
          notice.date_time = "{:%B %d, %Y  %H:%M:%S}".format(d)
          notice.status = "New"
          notice.save()
          # record.approved_by_date= approved_by_date


          record.save()

          _id = record.pk
          return JsonResponse( {'message':"success",'id':_id})

        except Exception as e  :
            f= open("goods_received_notes_send_record.txt","w")
            f.write(str(e))
            f.close()
            return JsonResponse({'message':"failed","tab":"1"})

@login_required(login_url='login')
@csrf_exempt
def goods_received_notes_upload_dnote(request):
    if request.method == 'POST' and request.FILES['dnote']:
        myfile1 = request.FILES['dnote']
        request_id = request.POST.get('request_id')
        
        import os
        path = "uploads/goods_received_notes/dnotes/"+str(request_id)
        # Check whether the specified path exists or not
        # #print"path ",path)
        isExist = os.path.exists(path)
        if not isExist:

          # Create a new directory because it does not exist
          os.makedirs(path)



        fs = FileSystemStorage()
        filename1 = fs.save(path+"/"+myfile1.name, myfile1)
        uploaded_file_url1 = fs.url(filename1)




        record = GoodsReceivedNoteDnote()
        record.request_id = request_id
        record.dnote_path = uploaded_file_url1
        record.save()
        return redirect('/procurement/goods_received_notes_all')
    else:
          return render(request, 'pages/goods_received/upload_pop.html')






@login_required(login_url='login')
@csrf_exempt
def goods_received_notes_approve(request):
    
    try:
      if request.method == "POST":
        
        _id = request.POST.get('id',default=None)

        record = GoodsReceivedNote.objects.get(id=_id)
        record.approver = request.user.username
        d = datetime.datetime.now()
        record.approver_date= "{:%B %d, %Y  %H:%M:%S}".format(d)

        notice = Notifications()
        notice.to = record.receiver
        record.save()

        notice.message = " "+ request.user.username +" approved your GRN."
        notice.date_time = "{:%B %d, %Y  %H:%M:%S}".format(d)
        notice.trigger = request.user.username
        notice.save()

        return JsonResponse( {'message':"success","tab":"1"})

    except Exception as e:
       return JsonResponse( {'message': str(e)})







# ************************************************************************************************************************* 

#PURCHASE ORDER


# ***********************************************************************************************************************
# purchase order




@login_required(login_url='login')
@csrf_exempt
def purchase_order_reject(request):
    if request.method == "POST":
      
      _id = request.POST.get('id',default=None)
      message = request.POST.get('message',default=None)
      username = request.user.username
        # objs = Record.objects.get(id=_id)
      record = PurchaseOrder.objects.get(id=_id)
      record.rejector = username
      record.rejector_message = message

      d = datetime.datetime.now()
          # record.date_of_request = "{:%B %d, %Y  %H:%M:%S}".format(d)
      record.rejector_date= "{:%B %d, %Y  %H:%M:%S}".format(d)
      notice = Notifications()
      notice.to = record.compiled_by
      record.save()

  
      notice.message = " "+ username +" has rejected your  Purchase order ."
      notice.date_time = "{:%B %d, %Y  %H:%M:%S}".format(d)
      notice.trigger = username
      notice.save()
      return JsonResponse( {'message':"success","tab":"1"})
    else:
      return render(request, 'pages/purchase_requests/list.html', {})
   

@login_required(login_url='login')
def purchase_order(request):
    records = PurchaseOrder.objects.all()
    context = {'records':records , "tab":"3"}
    return render(request, 'pages/purchase_orders/purchase_orders.html', context)

@login_required(login_url='login')
def purchase_order_all(request):
    username = request.user.username
    user_id = request.user.id
    # records = PurchaseOrder.objects.all()

    records = PurchaseOrder.objects.filter( Q(compiled_by=username) | Q(ordered_by=username) | Q(required_by= username) | Q(approved_by=username))
    context = {'records':records, "tab":"3"}
    return render(request, 'pages/purchase_orders/list.html', context)

def purchase_order_quote_upload(request):
    if request.method == 'POST' and request.FILES['quote']:
        myfile = request.FILES['quote']
        request_id = request.POST.get('request_id')
        
        import os
        path = "uploads/purchase_orders/"+str(request_id)
        # Check whether the specified path exists or not
        #print"path ",path)
        isExist = os.path.exists(path)
        if not isExist:

          # Create a new directory because it does not exist
          os.makedirs(path)



        fs = FileSystemStorage()
        filename1 = fs.save(path+"/"+myfile.name, myfile)
        uploaded_file_url1 = fs.url(filename1)



        record = PurchaseOrderQuotation()
        record.request_id = request_id
        record.quote_path = uploaded_file_url1
        record.save()
        return redirect('/procurement/purchase_order')
    else:
          return render(request, 'pages/purchase_orders/upload_quote.html')

@login_required(login_url='login')
def purchase_order_view(request):
    if request.method == "POST":
      
      _id = request.POST.get('id',default=None)

        # objs = Record.objects.get(id=_id)
      record = PurchaseOrder.objects.get(id=_id)
      context = {'record':record, "tab":"3"}


      return render(request, 'pages/purchase_orders/view_record.html', context)
    else:
         return redirect("/procurement/purchase_order_pending")
      
@login_required(login_url='login')
def purchase_order_edit_options(request):
    
    if request.method == "POST":
      
      _id = request.POST.get('id',default=None)

        # objs = Record.objects.get(id=_id)
      record = PurchaseOrder.objects.get(id=_id)
      context = {'record':record, "tab":"3"}
      # #print"IN POST")
      if record.required_by_date == "None" and record.required_by == request.user.username:
        #  #print"certified")
         return render(request, 'pages/purchase_orders/required.html', context)
      
      elif record.approved_by_date == "None" and record.approved_by == request.user.username:
        #  #print"cleared")

         return render(request, 'pages/purchase_orders/approve.html', context)

      elif record.ordered_by_date == "None" and record.ordered_by == request.user.username:
        #  #print"cleared")

         return render(request, 'pages/purchase_orders/ordered.html', context)
      else:
         return render(request, 'pages/comparative_schedules/not_auth.html', {})
      

    else:
         return redirect("/procurement/purchase_order_pending")
    


@login_required(login_url="login")
def purchase_order_open_record(request):
    if request.method == "POST":
      
      _id = request.POST.get('id',default=None)

        # objs = Record.objects.get(id=_id)
      record = PurchaseOrder.objects.get(id=_id)
      context = {'record':record, "tab":"3"}
      #print"IN POST")
      return render(request, 'pages/purchase_orders/view_record.html', context)
    else:
       redirect("/procurement/purchase_order_all")


# def purchase_order_view2(request):
#     if request.method == "POST":
      
#       _id = request.POST.get('id',default=None)

#         # objs = Record.objects.get(id=_id)
#       record = PaymentRequest.objects.get(id=_id)
#       context = {'record':record}
#       #print"IN POST")
#       return render(request, 'pages/purchase_orders/view2.html', context)
#     else:
#        redirect("/procurement/purchase_order_all")

@login_required(login_url='login')
def purchase_order_pending_view(request):
    if request.method == "POST":
      
      _id = request.POST.get('id',default=None)

        # objs = Record.objects.get(id=_id)
      record = PaymentRequest.objects.get(id=_id)
      context = {'record':record, "tab":"3"}

      #print"IN POST")
      if record.certified_by_date == "None" and record.certified_by == request.user.username and record.rejector == "None":
         #print"certified")
         return render(request, 'pages/purchase_orders/certify.html', context)
      elif record.cleared_by_fin_man_date == "None" and record.cleared_by_fin_man == request.user.username and record.rejector == "None":
         #print"cleared")

         return render(request, 'pages/purchase_orders/clear.html', context)
      
      elif record.approved_by_date == "None" and record.approved_by == request.user.username and record.rejector == "None":
         #print"approved")

         return render(request, 'pages/purchase_orders/approve.html', context)


    else:
      return render(request, 'pages/purchase_orders/list2.html', {})


@login_required(login_url='login')
@csrf_exempt
def purchase_order_print(request):
    # if request.method == "POST":
        current_url = request.path
        x= current_url.split("/")[-1]
        #printx)

        # _id = request.POST.get(x)
        # #print_id)

        record = PurchaseOrder.objects.get(id=x)
        # _id = record.purchase_id
        # record_purchase_request = PuchaseRequest.objects.get(id=_id)
        # record_comp_scheuldue  = ComparativeSchedule.objects.get(id=record_purchase_request.request_id)



        
        data = {
        "purchase_id": record.purchase_id,

        "name": record.name,
        "contact_person":record.contact_person,
        "contact_number":record.contact_number,
        "address": record.address,
        "project":record.project,
        "date": record.date,
        "budget_line_item": record.budget_line_item,

        "item": record.item,
        "dept":record.dept,
        "description":record.description,
        "quantity":record.quantity,
        "unit_cost":record.unit_cost,
        "total_cost": record.total_cost,

        "ordered_by":record.ordered_by,
        "required_by":record.required_by,
        "approved_by":record.approved_by,
        
        "message":"success","tab":"1"}   

        pdf = render_to_pdf('pages/purchase_orders/print.html', data)
        return HttpResponse(pdf, content_type='application/pdf')

    # if request.method == "POST":
    #   _id = request.POST.get('id',default=None)

      
    #   #printcurrent_url)

    #   l = current_url.split('/')
    #   #printl)

      

    #   record = PaymentRequest.objects.filter(id=x)
    #   context = {'record':record}
    #   return render(request, 'pages/purchase_orders/print.html', context)
@login_required(login_url='login')
def purchase_order_super(request):
    records = PurchaseOrder.objects.all()
    context = {'records':records, "tab":"3"}
    return render(request, 'pages/purchase_orders/list2.html', context)

@login_required(login_url='login')
def purchase_order_edit(request):
    form = PurchaseOrder.objects.all()
    context = {'form':form, "tab":"3"}
    return render(request, 'pages/purchase_orders/add.html', context)



@login_required(login_url='login')
def purchase_order_certification(request):
    if request.method == "POST":
      
      _id = request.POST.get('id',default=None)

        # objs = Record.objects.get(id=_id)
      record = PurchaseOrder.objects.get(id=_id)
      context = {'record':record, "tab":"3"}
      return render(request, 'pages/purchase_orders/view.html', context)
    else:
      return render(request, 'pages/purchase_orders/list.html', {})






@login_required(login_url='login')
def purchase_order_clearance(request):
    if request.method == "POST":
      
      _id = request.POST.get('id',default=None)

        # objs = Record.objects.get(id=_id)
      record = PurchaseOrder .objects.get(id=_id)
      context = {'record':record, "tab":"3"}
      return render(request, 'pages/purchase_orders/view.html', context)
    else:
      return render(request, 'pages/purchase_orders/list.html', {})

# @login_required(login_url='login')
# def purchase_order_clear(request):
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




#       return JsonResponse( {'message':"success","tab":"1"})

#     else:
#       return render(request, 'pages/purchase_orders/list.html', {})



@login_required(login_url='login')
def purchase_order_pending_approval(request):
    records = PaymentRequest.objects.filter(Q(rejector="None")&Q(approved_by="None"))
    context = {'records':records, "tab":"3"}
    return render(request, 'pages/purchase_orders/list.html', context)


# @login_required(login_url='login')
# def purchase_order_approval(request):
#     if request.method == "POST":
      
#       _id = request.POST.get('id',default=None)

#         # objs = Record.objects.get(id=_id)
#       record = PaymentRequest.objects.get(id=_id)




#       context = {'record':record}
#       return render(request, 'pages/purchase_orders/view.html', context)
#     else:
#       return render(request, 'pages/purchase_orders/list.html', {})

# @login_required(login_url='login')
# def purchase_order_approve(request):
#     if request.method == "POST":
      
#       _id = request.POST.get('id',default=None)

#         # objs = Record.objects.get(id=_id)
#       record = PaymentRequest.objects.get(id=_id)
#       record.approved_by = request.user.username
#       # record.certified_by_date = request.user.username
#       d = datetime.datetime.now()
#           # record.date_of_request = "{:%B %d, %Y  %H:%M:%S}".format(d)
#       record.approved_by_date= "{:%B %d, %Y  %H:%M:%S}".format(d)





#       return JsonResponse( {'message':"success","tab":"1"})

#     else:
#       return render(request, 'pages/purchase_orders/list.html', {})

@login_required(login_url='login')
@csrf_exempt
def purchase_order_certify(request):
    
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

        return JsonResponse( {'message':"success","tab":"1"})
      else:
        return render(request, 'pages/purchase_orders/list.html', {})

    except:
       return JsonResponse( {'message':"failed","tab":"1"})

@login_required(login_url='login')
@csrf_exempt
def purchase_order_clear(request):
    
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

        return JsonResponse( {'message':"success","tab":"1"})
      else:
        return render(request, 'pages/purchase_orders/list.html', {})


    except:
       return JsonResponse( {'message':"failed","tab":"1"})



@login_required(login_url='login')
@csrf_exempt
def purchase_order_required(request):
    
    try:
      if request.method == "POST":
        
        _id = request.POST.get('id',default=None)
        approver = request.POST.get('approver',default=None)

          # objs = Record.objects.get(id=_id)
        record = PurchaseOrder.objects.get(id=_id)
        record.approved_by = approver
        # record.certified_by_date = request.user.username
        d = datetime.datetime.now()
            # record.date_of_request = "{:%B %d, %Y  %H:%M:%S}".format(d)
        record.required_by_date= "{:%B %d, %Y  %H:%M:%S}".format(d)



        notice = Notifications()
        notice.to = record.compiled_by
        record.save()

        notice.message = " "+ request.user.username +" Updated your Purchase Order."
        notice.date_time = "{:%B %d, %Y  %H:%M:%S}".format(d)
        notice.trigger = request.user.username
        notice.save()

        return JsonResponse( {'message':"success","tab":"1"})
      else:
        return render(request, 'pages/purchase_orders/list.html', {})


    except:
       return JsonResponse( {'message':"failed","tab":"1"})



@login_required(login_url='login')
@csrf_exempt
def purchase_order_ordered(request):
    
    try:
      if request.method == "POST":
        
        _id = request.POST.get('id',default=None)
        required = request.POST.get('required',default=None)

          # objs = Record.objects.get(id=_id)
        record = PurchaseOrder.objects.get(id=_id)
        record.ordered_by = request.user.username
        record.required_by = required
        d = datetime.datetime.now()
            # record.date_of_request = "{:%B %d, %Y  %H:%M:%S}".format(d)
        record.required_by_date= "{:%B %d, %Y  %H:%M:%S}".format(d)



        notice = Notifications()
        notice.to = record.compiled_by
        record.save()

        notice.message = " "+ request.user.username +" Updated your Purchase Order."
        notice.date_time = "{:%B %d, %Y  %H:%M:%S}".format(d)
        notice.trigger = request.user.username
        notice.save()

        return JsonResponse( {'message':"success","tab":"1"})
      else:
        return render(request, 'pages/purchase_orders/list.html', {})


    except:
       return JsonResponse( {'message':"failed","tab":"1"})




@login_required(login_url='login')
@csrf_exempt
def purchase_order_approve(request):
    
    try:
      if request.method == "POST":
        
        _id = request.POST.get('id',default=None)

          # objs = Record.objects.get(id=_id)
        record = PurchaseOrder.objects.get(id=_id)
        record.approved_by = request.user.username
        # record.certified_by_date = request.user.username
        d = datetime.datetime.now()
            # record.date_of_request = "{:%B %d, %Y  %H:%M:%S}".format(d)
        record.approved_by_date= "{:%B %d, %Y  %H:%M:%S}".format(d)



        notice = Notifications()
        notice.to = record.compiled_by
        record.save()

        notice.message = " "+ request.user.username +" Updated your Purchase Order."
        notice.date_time = "{:%B %d, %Y  %H:%M:%S}".format(d)
        notice.trigger = request.user.username
        notice.save()

        return JsonResponse( {'message':"success","tab":"1"})
      else:
        return render(request, 'pages/purchase_orders/list.html', {})


    except:
       return JsonResponse( {'message':"failed","tab":"1"})




@login_required(login_url='login')
@csrf_exempt
def purchase_ordered_approve(request):
    
    try:
      if request.method == "POST":
        
        _id = request.POST.get('id',default=None)

          # objs = Record.objects.get(id=_id)
        record = PurchaseOrder.objects.get(id=_id)
        record.ordered_by = request.user.username
        # record.certified_by_date = request.user.username
        d = datetime.datetime.now()
            # record.date_of_request = "{:%B %d, %Y  %H:%M:%S}".format(d)
        record.ordered_by_date= "{:%B %d, %Y  %H:%M:%S}".format(d)



        notice = Notifications()
        notice.to = record.compiled_by
        record.save()

        notice.message = " "+ request.user.username +" Updated your Purchase Order."
        notice.date_time = "{:%B %d, %Y  %H:%M:%S}".format(d)
        notice.trigger = request.user.username
        notice.save()

        return JsonResponse( {'message':"success","tab":"1"})
      else:
        return render(request, 'pages/purchase_orders/list.html', {})


    except:
       return JsonResponse( {'message':"failed","tab":"1"})




@login_required(login_url='login')
def purchase_order_pending(request):
    username = request.user.username
    records = PurchaseOrder.objects.filter(Q(rejector="None") & ( (Q(approved_by=username) & Q (approved_by_date="None")) | (Q(required_by=username) & Q (required_by_date="None") | (Q(ordered_by=username) & Q (ordered_by_date="None")) )  ) )
    context = {'records':records, "tab":"3"}
    return render(request, 'pages/purchase_orders/list_pending.html', context)


@login_required(login_url='login')
def purchase_order_approved(request):
    username = request.user.username

    records = PurchaseOrder.objects.filter( (Q(approved_by=username) & ~Q(approved_by_date="None") ) | (Q(ordered_by=username) & ~Q(approved_by_date="None") )    )
    context = {'records':records, "tab":"3"}
    return render(request, 'pages/purchase_orders/list_approved.html', context)

@login_required(login_url='login')
def purchase_order_add(request):
    form = PurchaseOrder.objects.all()
    context = {'form':form, "tab":"3"}
    return render(request, 'pages/purchase_orders/add.html', context)


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
def purchase_order_get_record(request):
    context={}
    if request.method == "POST":
        _id = request.POST.get('id',default=None)


        pdf = PurchaseOrderQuotation.objects.get(id=1)


        try:
          pdf = PurchaseOrderQuotation.objects.get(request_id=_id)
        except:
          pass
        record = PurchaseOrder.objects.get(id=_id)

        dic = {
           
          "pdf":"/procurement"+pdf.quote_path,

          "purchase_id": record.purchase_id,
      "rejector":record.rejector,
      "rejector_date":record.rejector_date,
      "rejector_message":record.rejector_message,
          "sup_name": record.sup_name,
          "contact_person": record.contact_person,
          "contact_number": record.contact_number,
          "address": record.address,
          "date": record.date,
          "comp_schedule_id": record.comp_schedule_id,

          "item_name": record.item_name,
          "quantity": record.quantity,
          "unit_cost": record.unit_cost,
          "description": record.description,
          "total_cost": record.total_cost,

          "ordered_by": record.ordered_by,
          "ordered_by_date": record.ordered_by_date,

          "required_by": record.required_by,
          "required_by_date": record.required_by_date,

          "approved_by": record.approved_by,
          "approved_by_date": record.approved_by_date,

          "message":"success",
        }
        context = {'addTabActive': True, "record":"","tab":"1"}
        return JsonResponse(dic)
    else:
        return redirect('/procurement/purchase_orders')

@login_required(login_url='login')
@csrf_exempt
@app.route("/send_record")
def purchase_order_send_record(request):

    with app.app_context():
        try:
          purchase_id= request.POST.get('purchase_id',default=None)
          comp_schedule_id= request.POST.get('comp_schedule_id',default=None)

          sup_name= request.POST.get('sup_name',default=None)
          contact_person= request.POST.get('contact_person',default=None)
          contact_number= request.POST.get('contact_number',default=None)
          address= request.POST.get('address',default=None) 

          item_name= request.POST.get('item_name',default=None)
          description= request.POST.get('description',default=None)
          quantity= request.POST.get('quantity',default=None)
          unit_cost= request.POST.get('unit_cost',default=None)
          total_cost= request.POST.get('total_cost',default=None)
          
          ordered_by= request.user.username
          # ordered_by_date= request.POST.get('ordered_by_date',default=None)

          # approved_by= request.POST.get('approved_by',default=None)
          # approved_by_date= request.POST.get('approved_by_date',default=None)
          
          required_by= request.POST.get('required_by',default=None)
          # required_by_date= request.POST.get('required_by_date',default=None)

          pdf1,pdf = PurchaseOrderQuotation.objects.get_or_create(
          request_id = "0",
          quote_path = "#"

        )


          record = PurchaseOrder()
          d = datetime.datetime.now()

          record.compiled_by = request.user.username
          record.purchase_id= purchase_id

          record.comp_schedule_id= comp_schedule_id

          record.sup_name= sup_name
          record.contact_person= contact_person
          record.contact_number= contact_number
          record.address= address 
          record.date = "{:%B %d, %Y  %H:%M:%S}".format(d)

          record.item_name= item_name
          record.description= description
          record.quantity= quantity
          record.unit_cost= unit_cost
          record.total_cost= total_cost

          record.ordered_by= ordered_by
          record.ordered_by_date= "{:%B %d, %Y  %H:%M:%S}".format(d)

          record.required_by= required_by
          # record.required_by_date= "{:%B %d, %Y  %H:%M:%S}".format(d)

          # record.approved_by= approved_by
          # record.approved_by_date= approved_by_date

          notice = Notifications()
          notice.to= record.required_by
          notice.trigger = request.user.username
          notice.message = request.user.username +" has created a Purchase Order on your behalf to approve."

          d1 = datetime.datetime.now()
          record.date_of_request = "{:%B %d, %Y  %H:%M:%S}".format(d1)
          notice.date_time = "{:%B %d, %Y  %H:%M:%S}".format(d1)
          notice.status = "New"
          notice.save()
          # record.approved_by_date= approved_by_date


          record.save()

          _id = record.pk
          return JsonResponse( {'message':"success",'id':_id})

        except Exception as e  :
            f= open("service3.txt","w")
            f.write(str(e))
            f.close()
            return JsonResponse({'message':"failed","tab":"1"})



@login_required(login_url='login')
@csrf_exempt
def purchase_order_edit_record(request):

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



          return JsonResponse( {'message':"success","tab":"1"})

        except Exception as e  :
            f= open("service1.txt","w")
            f.write(str(e))
            f.close()
            return JsonResponse({'message':"failed","tab":"1"})
        



# @login_required(login_url='login')
# @csrf_exempt
# def purchase_order_approve(request):
#     if request.method == "POST":
      
#       _id = request.POST.get('id',default=None)
#       # clerk = request.POST.get('clerk',default=None)
#       username = request.user.username
#         # objs = Record.objects.get(id=_id)
#       record = PurchaseOrder.objects.get(id=_id)
#       # record.accounts_clerk_approved = clerk
#       d = datetime.datetime.now()
#           # record.date_of_request = "{:%B %d, %Y  %H:%M:%S}".format(d)
#       record.approved_by= "{:%B %d, %Y  %H:%M:%S}".format(d)

#       record.save()

#       notice = Notifications()
#       notice.to = record.ordered_by
#       notice.message = " "+ username +" updated Approved your Purchase Order."
#       notice.date_time = "{:%B %d, %Y  %H:%M:%S}".format(d)
#       notice.trigger = username
#       notice.save()


#       return JsonResponse( {'message':"success","tab":"1"})
#     else:
#       return render(request, 'pages/purchase_orders/list.html', {})
    


# @login_required(login_url='login')
# def purchase_order_view(request):
#     if request.method == "POST":
      
#       _id = request.POST.get('id',default=None)

#         # objs = Record.objects.get(id=_id)
#       record = PurchaseOrder.objects.get(id=_id)
#       context = {'record':record}

#       return render(request, 'pages/purchase_orders/approve.html', context)
#     else:
#         return render(request, 'pages/comparative_schedules/not_auth.html', {})




@login_required(login_url='login')
@csrf_exempt
def get_purchase_orders(request):
   try:
      dic = {}
      # User = get_user_model()
      schedules = PurchaseOrder.objects.filter(~Q(approved_by_date = "None"))

      for schedule in schedules: 
          dic[schedule.id]= schedule.item_name+", Total Cost : "+ schedule.total_cost +", raised by : "+ schedule.compiled_by+", raised on : "+schedule.date+", Supplier : "+schedule.sup_name
      return JsonResponse(dic)
   except Exception as e:
          return JsonResponse(str(e)) 






from PIL import Image, ImageDraw, ImageFont
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

username = "timesheet@brti.co.zw"
password = "p@s3w0rd?1995"

def send_otp(otp,email):
                
                message = "Thank you for Generating your signature with us!\n Your code is: "+otp+" \nSincerely,\nBiomedical Research and Training Institute"
                mimemsg = MIMEMultipart()
                mimemsg['From']="authenticator@brti.co.zw"
                mimemsg['To']=email
                # mimemsg['Cc']=liliosa
                #
                mimemsg['Subject']="Signature Generation OTP"
                mimemsg.attach(MIMEText(message, 'plain'))

                # with open(mail_attachment, "rb") as attachment:
                #     mimefile = MIMEBase('application', 'octet-stream')
                #     #mimefile.set_payload((attachment).read())
                # #     encoders.encode_base64(mimefile)
                # #     mimefile.add_header('Content-Disposition', "attachment; filename= %s" % mail_attachment_name)
                #     #mimemsg.attach(mimefile)
                connection = smtplib.SMTP(host='smtp.office365.com', port=587)
                connection.starttls()
                connection.login('authenticator@brti.co.zw','p@s3w0rd?1995')
                connection.send_message(mimemsg)
                connection.quit()

import random

def gen_number():
   otp = random.randint(1000,9999)

   return str(otp)


def generateOTP(email):
  otp = gen_number()

  send_otp(otp,email)

  return otp



@csrf_exempt
def verify_otp(request):
   if request.method == "POST":
      input = request.POST.get('input',default=None)
      otp = request.session.get('otp')

      if input == otp:
          return JsonResponse( {'message':"success","tab":"1"})
      else:
          return JsonResponse( {'message':"fail","tab":"1"})
   else:
        return render(request, 'pages/comparative_schedules/verify.html', {})





   


@csrf_exempt
def gen_sig(request):


    otp = generateOTP(request.user.email)
    request.session['otp'] = otp

    return redirect("/verify_otp")




@csrf_exempt
def save_sig(request):
   
    fullname = request.user.first_name +" "+ request.user.last_name
  # #printfullname)
    username = request.user.username
      
    # _id = request.POST.get('name',default=None)
   # -*- coding: utf-8 -*-
    path = str(username)



    iw, ih = 500, 120
    text = fullname
    img = Image.new("RGB", (iw, ih), color="white")
    dctx = ImageDraw.Draw(img)

    # courbi.ttf: Courier New Bold Italic (on Microsoft Windows)
    ttf = ImageFont.truetype("home/fonts/CheGuevaraSign-Regular.ttf", 100)
  
    w, h = ttf.getsize(text)
    off_x, off_y = ttf.getoffset(text)
    mx, my = (iw - w) // 2, (ih - h) // 2

    # dctx.line(((mx + off_x, my + off_y), (iw - mx, my + off_y)),
    #           fill="blue")

    # dctx.rectangle(((mx, my), (iw - mx, ih - my)), outline="red")
    dctx.text((mx, my), text, font=ttf, fill="black")
    #img.show()
    new_path = os.path.join("signatures",path)
    if os.path.exists:
       pass
    else:
      os.mkdir(new_path)

    img.save(os.path.join(new_path,path+".png"))
    return redirect("/")


import qrcode
from qrcode import make
from time import time

# def qr_code(request):
#     current_url = request.path
#     x= current_url.split("/")[-1]
    
#     record = ComparativeSchedule.objects.get(id=x)
    
#     data = 'https://lorkas.co.zw/procurement/comp_schedule_print/'+ x
#     img = make(data)
#     img_name = f'lolo.png'
#     img.save(img_name)
#     context = {'img_name': img_name}
#     return render(request, 'pages/qr.html', context)

def qr_code(id):

    text='hie'
    img = qrcode.make(text)
    type(img)  # qrcode.image.pil.PilImage
    img_name = f'lolo.png'
    img.save(img_name)


def transcript(request):
    
    # if request.method == "POST":
        current_url = request.path
        x= current_url.split("/")[-1]
        #printx)

        # _id = request.POST.get(x)
        # #print_id)

        record1 = PaymentTicket.objects.get(id=x)
        _id = record1.payment_request_id

        record2 = PaymentRequest.objects.get(id=_id)
        _id2 = record2.purchase_id

        record = PurchaseOrder.objects.get(id=_id2)
        _id3 = record.purchase_id

        record4 = PuchaseRequest.objects.get(id=_id3)
        _id4 = record4.schedule_id

        record5 = ComparativeSchedule.objects.get(id=_id4)
        _id5 = record5.request_id
       

        data = {
           
        #PAYMENT TICKET STUFF
        "payment_request_id": record1.payment_request_id,
        "creator":record1.creator,
        "date_of_ticket": record1.date_of_ticket,
        "status":record1.status, 
        "amount":record1.amount,
        "to_name":record1.to_name,
        "to_bank_name":record1.to_bank_name,
        "to_bank_account":record1.to_bank_account,
        "narration":record1.narration,

        #PAYMENT REQUEST STUFF
        "payee": record2.payee,
        "compiled_by": record2.compiled_by,
        "date_of_request": record2.date_of_request,
        "payment_type": record2.payment_type,
        "project_number": record2.project_number,
        "account_code": record2.account_code,
        "details": record2.details,
        "amount": record2.amount,
        "total": record2.total,
        "certified_by": record2.certified_by,
        "certified_by_date": record2.certified_by_date,
        "cleared_by_fin_man": record2.cleared_by_fin_man,
        "cleared_by_fin_man_date": record2.cleared_by_fin_man_date,
        "approved_by_project_man": record2.approved_by_project_man,
        "approved_by_project_man_date": record2.approved_by_project_man_date,
        "approved_by": record2.approved_by,
        "approved_by_date": record2.approved_by_date,
           
      #PURCHASE ORDER STUFF
        "purchase_id": record.purchase_id,

        "name": record.name,
        "contact_person":record.contact_person,
        "contact_number":record.contact_number,
        "address": record.address,
        "project":record.project,
        "date": record.date,
        "budget_line_item": record.budget_line_item,

        "item": record.item,
        "dept":record.dept,
        "description":record.description,
        "quantity":record.quantity,
        "unit_cost":record.unit_cost,
        "total_cost": record.total_cost,

        "ordered_by":record.ordered_by,
        "required_by":record.required_by,
        "approved_by":record.approved_by,

        #COMPARATIVE SCHEDULE STUFF
        "service_request": record5.service_request,
        "request_id": record5.request_id,
        "payee": record5.payee,

        "company_name_supplier1": record5.company_name_supplier1,
        "company_name_supplier2": record5.company_name_supplier2,
        "company_name_supplier3": record5.company_name_supplier3,

        "item_number_supplier1": record5.item_number_supplier1,
        "item_number_supplier2": record5.item_number_supplier2,
        "item_number_supplier3": record5.item_number_supplier3,

        "desc_supplier1": record5.desc_supplier1,
        "desc_supplier2": record5.desc_supplier2,
        "desc_supplier3": record5.desc_supplier3,

        "qnty_supplier1": record5.qnty_supplier1,
        "qnty_supplier2": record5.qnty_supplier2,
        "qnty_supplier3": record5.qnty_supplier3,

        "unit_price_supplier1": record5.unit_price_supplier1,
        "unit_price_supplier2": record5.unit_price_supplier2,
        "unit_price_supplier3": record5.unit_price_supplier3,

        "total_price_supplier1": record5.total_price_supplier1,
        "total_price_supplier2": record5.total_price_supplier2,
        "total_price_supplier3": record5.total_price_supplier3,

        "requested_by": record5.requested_by,
        "requested_by_sig": record5.requested_by_sig,
        "requested_by_date": record5.requested_by_date,

        "tech_person_by": record5.tech_person_by,
        "tech_person_by_sig": record5.tech_person_by_sig,
        "tech_person_date": record5.tech_person_date,

        "dpt_head_by": record5.dpt_head_by,
        "dpt_head_by_sig": record5.dpt_head_by_sig,
        "dpt_head_date": record5.dpt_head_date,

        "team_lead_by": record5.team_lead_by,
        "team_lead_by_sig": record5.team_lead_by_sig,
        "team_lead_date": record5.team_lead_date,

        "approved_by": record5.approved_by,
        "approved_by_sig": record5.approved_by_sig,
        "approved_date": record5.approved_date,

        "recommended_supplier": record5.recommended_supplier,
        "recommended_supplier_reason": record5.recommended_supplier_reason,

        "upload_name": record5.upload_name,

        "dpt_project_requesting": record5.dpt_project_requesting,

        "project_number": record5.project_number,

        
        "message":"success","tab":"1"}   

        pdf = render_to_pdf('pages/transcript.html', data)
        return HttpResponse(pdf, content_type='application/pdf')
    
    # return render(request,'transcript.html')