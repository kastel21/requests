from django.db import models

# Create your models here.
# /Users/it/requests/uploads/comp_schedules/1
# uploads/comp_schedules/1

class PuchaseRequest(models.Model):

    schedule_id = models.CharField(max_length=310, default="None")
    service_request = models.CharField(max_length=100, default="None")
    requester = models.CharField(max_length=100, default="None")
    date_of_request = models.CharField(max_length=200, default="2023")
    requesting_dpt = models.CharField(max_length=150, default="None")
    request_justification = models.CharField(max_length=2000, default="None")
    name_address_of_supplier = models.CharField(max_length=550, default="None")
    budget_line_item = models.CharField(max_length=200, default="None")
   
    qnty = models.CharField(max_length=150, default="None")
    q1 = models.FileField(default="None")

    item_number = models.CharField(max_length=150, default="None")
    description = models.CharField(max_length=150, default="None")
    unit_price = models.CharField(max_length=150, default="None")
    total = models.CharField(max_length=150, default="None")
   
    supervisor_approved = models.CharField(max_length=150, default="None")
    supervisor_approved_date= models.CharField(max_length=150, default="None")
    accounts_clerk_approved= models.CharField(max_length=150, default="None")
    accounts_clerk_approved_date= models.CharField(max_length=150, default="None")




class ProcurementRequest(models.Model):

    service_request_id = models.CharField(max_length=300, default="None")
    requester = models.CharField(max_length=300, default="None")
    date_of_request = models.CharField(max_length=250, default="2023")
    cost_category = models.CharField(max_length=150, default="None")
    procurement_officer = models.CharField(max_length=150, default="None")
    procurement_officer_accept = models.CharField(max_length=150, default="None")

    procurement_officer_accept_date = models.CharField(max_length=150, default="None")
    procurement_officer_reject = models.CharField(max_length=150, default="None")
    procurement_officer_reject_date = models.CharField(max_length=150, default="None")

    procurement_officer_reject_msg = models.CharField(max_length=500, default=".")

    requesting_dpt = models.CharField(max_length=250, default="None")



class ServiceRequest(models.Model):

    # schedule_id = models.CharField(max_length=30, default="None")
    requester = models.CharField(max_length=300, default="None")
    date_of_request = models.CharField(max_length=100, default="2023")
    requesting_dpt = models.CharField(max_length=150, default="None")
    request_justification = models.CharField(max_length=450, default="None")
    # name_address_of_supplier = models.CharField(max_length=550, default="None")
    # budget_line_item = models.CharField(max_length=150, default="None")
   
    qnty = models.CharField(max_length=150, default="None")
    q1 = models.FileField(default="None")

    po = models.CharField(max_length=150, default="None")
    po_approved_date= models.CharField(max_length=150, default="None")

    description = models.CharField(max_length=150, default="None")
    # unit_price = models.CharField(max_length=150, default="None")
    # total = models.CharField(max_length=150, default="None")
   
    supervisor_approved = models.CharField(max_length=150, default="None")
    supervisor_approved_date= models.CharField(max_length=150, default="None")
    supervisor_disapproved_date= models.CharField(max_length=150, default="None")
    supervisor_disapproved_message= models.CharField(max_length=1500, default=".")




class PurchaseOrder(models.Model):
    purchase_id = models.CharField(max_length=300, default="None")
    name = models.CharField(max_length=100, default="None")
    contact_person = models.CharField(max_length=300, default="None")
    contact_number = models.CharField(max_length=250, default="2023")
    address = models.CharField(max_length=150, default="None")
    project = models.CharField(max_length=450, default="None")
    date = models.CharField(max_length=550, default="None")
    budget_line_item = models.CharField(max_length=150, default="None")
   

    compiled_by = models.CharField(max_length=150, default="None")

    item = models.CharField(max_length=150, default="None")
    dept = models.FileField(default="None")
    quantity = models.CharField(max_length=150, default="None")
    description = models.CharField(max_length=150, default="None")
    unit_cost = models.CharField(max_length=150, default="None")
    total_cost = models.CharField(max_length=150, default="None")
   
    ordered_by = models.CharField(max_length=150, default="None")
    ordered_by_date= models.CharField(max_length=150, default="None")
    
    required_by = models.CharField(max_length=150, default="None")
    required_by_date= models.CharField(max_length=150, default="None")

    approved_by= models.CharField(max_length=150, default="None")
    approved_by_date= models.CharField(max_length=150, default="None")

class PurchaseOrderQuotation(models.Model):
    request_id = models.CharField(max_length=255, blank=True)
    quote_path = models.CharField(max_length=500,default="#")

class PuchaseRequestQuote(models.Model):
    request_id = models.CharField(max_length=255, blank=True)
    quote = models.FileField(upload_to='documents/')



class PuchaseRequestQuotation(models.Model):
    request_id = models.CharField(max_length=255, blank=True)
    quote_path = models.CharField(max_length=500,default="#")

class PaymentRequest(models.Model):
    completed= models.CharField(max_length=5, default="0")

    purchase_id= models.CharField(max_length=300, default="None")
    request_id = models.CharField(max_length=300, default="None")
    compiled_by = models.CharField(max_length=300, default="None")
    date_of_request = models.CharField(max_length=100, default="None")
    payee = models.CharField(max_length=150, default="None")
    payment_type = models.CharField(max_length=450, default="None")
    type_of_payment = models.CharField(max_length=550, default="None")
    project_number = models.CharField(max_length=150, default="None")
   
    account_code = models.CharField(max_length=150, default="None")
    details = models.CharField(max_length=150, default="None")
    amount = models.CharField(max_length=150, default="None")
    qnty = models.CharField(max_length=150, default="None")
    total = models.CharField(max_length=150, default="None")
   
    certified_by = models.CharField(max_length=150, default="None")
    certified_by_date = models.CharField(max_length=150, default="None")

    cleared_by_fin_man= models.CharField(max_length=150, default="None")
    cleared_by_fin_man_date= models.CharField(max_length=250, default="None")

    approved_by_project_man= models.CharField(max_length=250, default="None")
    approved_by_project_man_date= models.CharField(max_length=250, default="None")

    approved_by= models.CharField(max_length=150, default="None")
    approved_by_date= models.CharField(max_length=250, default="None")

# class PaymentRequest(models.Model):
#     request_id = models.CharField(max_length=255, blank=True)
#     quote = models.FileField(upload_to='documents/', default="N/A")

class PaymentRequestQuotation(models.Model):
    request_id = models.CharField(max_length=255, blank=True)
    quote_path1 = models.CharField(max_length=500, default="#")
    quote_path2 = models.CharField(max_length=500, default="#")

class PaymentRequestQuotation1(models.Model):
    request_id = models.CharField(max_length=255, blank=True)
    quote_path1 = models.CharField(max_length=500, default="#")
    quote_path2 = models.CharField(max_length=500, default="#")


class PaymentRequestPOP(models.Model):
    request_id = models.CharField(max_length=255, blank=True)

    quote_path1 = models.CharField(max_length=500, default="#")

class CompScheduleQuotation(models.Model):
    request_id = models.CharField(max_length=255, blank=True)
    quote1_path = models.CharField(max_length=500, default="#")
    quote2_path = models.CharField(max_length=500, default="#")
    quote3_path = models.CharField(max_length=500, default="#")

class ComparativeSchedule(models.Model):
    service_request = models.CharField(max_length=100, default="None")

    request_id = models.CharField(max_length=300, default="None")
    payee = models.CharField(max_length=150, default="None")
   
    company_name_supplier1 = models.CharField(max_length=450, default="None")
    company_name_supplier2 = models.CharField(max_length=450, default="None")
    company_name_supplier3 = models.CharField(max_length=450, default="None")
    
    item_number_supplier1 = models.CharField(max_length=450, default="None")
    item_number_supplier2 = models.CharField(max_length=450, default="None")
    item_number_supplier3 = models.CharField(max_length=450, default="None")

    desc_supplier1 = models.CharField(max_length=450, default="None")
    desc_supplier2 = models.CharField(max_length=450, default="None")
    desc_supplier3 = models.CharField(max_length=450, default="None")


    qnty_supplier1 = models.CharField(max_length=450, default="None")
    qnty_supplier2 = models.CharField(max_length=450, default="None")
    qnty_supplier3 = models.CharField(max_length=450, default="None")


    unit_price_supplier1 = models.CharField(max_length=450, default="None")
    unit_price_supplier2 = models.CharField(max_length=450, default="None")
    unit_price_supplier3 = models.CharField(max_length=450, default="None")

    total_price_supplier1 = models.CharField(max_length=450, default="None")
    total_price_supplier2 = models.CharField(max_length=450, default="None")
    total_price_supplier3 = models.CharField(max_length=450, default="None")

    recommended_supplier = models.CharField(max_length=150, default="2023")
    recommended_supplier_reason = models.CharField(max_length=150, default="None")

    upload_name = models.CharField(max_length=550, default="None")

    dpt_project_requesting = models.CharField(max_length=150, default="2023")

    requested_by = models.CharField(max_length=300, default="None")
    requested_by_sig = models.CharField(max_length=300, default="None")
    requested_by_date = models.CharField(max_length=300, default="None")


    
    tech_person_by = models.CharField(max_length=300, default="None")
    tech_person_by_sig = models.CharField(max_length=300, default="None")
    tech_person_date = models.CharField(max_length=300, default="None")

    dpt_head_by = models.CharField(max_length=300, default="None")
    dpt_head_by_sig = models.CharField(max_length=300, default="None")
    dpt_head_date = models.CharField(max_length=300, default="None")

    team_lead_by = models.CharField(max_length=300, default="None")
    team_lead_by_sig = models.CharField(max_length=300, default="None")
    team_lead_date = models.CharField(max_length=300, default="None")

    approved_by = models.CharField(max_length=300, default="None")
    approved_by_sig = models.CharField(max_length=300, default="None")
    approved_date = models.CharField(max_length=300, default="None")

    project_number = models.CharField(max_length=150, default="None")

class Notifications(models.Model):
    trigger = models.CharField(max_length=220)
    date_time = models.CharField(max_length=120)
    message = models.CharField(max_length=420)
    to = models.CharField(max_length=200)
    status = models.CharField(max_length=220)

    def __str__(self):
        return self.message
