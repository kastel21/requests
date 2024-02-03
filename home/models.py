from django.db import models
from django.contrib.auth.models import AbstractUser





class PuchaseRequest(models.Model):

    requester = models.CharField(max_length=100, default="None")
    date_of_request = models.CharField(max_length=200, default="2023")
    requesting_dpt = models.CharField(max_length=150, default="None")
    request_justification = models.CharField(max_length=2000, default="None")
    budget_line_item = models.CharField(max_length=200, default="None")
   
    qnty = models.CharField(max_length=150, default="None")

    item_name = models.CharField(max_length=450, default="None")
    description = models.CharField(max_length=150, default="None")
   
    supervisor_approved = models.CharField(max_length=150, default="None")
    supervisor_approved_date= models.CharField(max_length=150, default="None")
    finance_officer= models.CharField(max_length=150, default="None")
    finance_officer_approved_date= models.CharField(max_length=150, default="None")
    rejector= models.CharField(max_length=150, default="None")
    rejector_message= models.CharField(max_length=500, default="None")
    rejector_date= models.CharField(max_length=500, default="None")
    completed= models.CharField(max_length=50, default="0")

    def __str__(self):
        return "Item : "+self.item_name +", Quantity"+self.qnty+", Requester"+self.requester+", Department : "+self.requesting_dpt+", Details : "+self.description




class PurchaseOrder(models.Model):
    comp_schedule_id = models.CharField(max_length=300, default="None")

    purchase_id = models.CharField(max_length=300, default="None")
    sup_name = models.CharField(max_length=200, default="None")
    contact_person = models.CharField(max_length=300, default="None")
    contact_number = models.CharField(max_length=250, default="2023")
    address = models.CharField(max_length=150, default="None")
    date = models.CharField(max_length=550, default="None")
   

    compiled_by = models.CharField(max_length=150, default="None")

    item_name = models.CharField(max_length=250, default="None")
    quantity = models.CharField(max_length=150, default="None")
    description = models.CharField(max_length=550, default="None")
    unit_cost = models.CharField(max_length=150, default="None")
    total_cost = models.CharField(max_length=150, default="None")
   
    ordered_by = models.CharField(max_length=150, default="None")
    ordered_by_date= models.CharField(max_length=150, default="None")
    
    required_by = models.CharField(max_length=150, default="None")
    required_by_date= models.CharField(max_length=150, default="None")

    approved_by= models.CharField(max_length=250, default="None",null=True)
    approved_by_date= models.CharField(max_length=150, default="None")
    rejector= models.CharField(max_length=150, default="None")
    rejector_message= models.CharField(max_length=500, default="None")
    rejector_date= models.CharField(max_length=500, default="None")
    completed= models.CharField(max_length=50, default="0")
    def __str__(self):
        return "Item : "+self.item_name +", Quantity"+self.qnty+", Requester"+self.requester+", Total Cost : "+self.total_cost+", Details : "+self.description +", Supplier"+self.sup_name

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

    purchase_id= models.CharField(max_length=300, default="None")
    request_id = models.CharField(max_length=300, default="None")
    compiled_by = models.CharField(max_length=300, default="None")
    date_of_request = models.CharField(max_length=100, default="None")
    payee = models.CharField(max_length=150, default="None")
    payment_type = models.CharField(max_length=450, default="None")
    type_of_payment = models.CharField(max_length=550, default="None")
   
    details = models.CharField(max_length=150, default="None")
    amount = models.CharField(max_length=150, default="None")
    qnty = models.CharField(max_length=150, default="None")
    total = models.CharField(max_length=150, default="None")
   
    certified_by = models.CharField(max_length=150, default="None")
    certified_by_date = models.CharField(max_length=150, default="None")

    cleared_by_fin_man= models.CharField(max_length=150, default="None")
    cleared_by_fin_man_date= models.CharField(max_length=250, default="None")

    accepted_by = models.CharField(max_length=150, default="None")
    accepted_by_date = models.CharField(max_length=150, default="None")
    rejector= models.CharField(max_length=150, default="None")
    rejector_message= models.CharField(max_length=500, default="None")
    rejector_date= models.CharField(max_length=500, default="None")
    completed= models.CharField(max_length=50, default="0")
    grnote= models.CharField(max_length=50, default="0")
    def __str__(self):
        return "Quantity "+self.qnty+", Requester"+self.compiled_by+", Total Cost : "+self.total+", Details : "+self.details +", Supplier"+self.payee+", DOR "+self.date_of_request


class PaymentTicket(models.Model):
    payment_request_id = models.CharField(max_length=150, default="None")
    creator = models.CharField(max_length=150, default="None")
    date_of_ticket = models.CharField(max_length=150, default="None")
    status = models.CharField(max_length=150, default="None")

    amount = models.CharField(max_length=150, default="None")
    to_name = models.CharField(max_length=150, default="None")
    to_bank_name = models.CharField(max_length=150, default="None")
    to_bank_account = models.CharField(max_length=150, default="None")
    narration = models.CharField(max_length=150, default=".")



class PaymentTicketPOP(models.Model):
    payment_ticket_id = models.CharField(max_length=150, default="None")
    pop_path = models.CharField(max_length=500, default="#")




class Supplier(models.Model):
    name = models.CharField(max_length=150, default="None")
    address = models.CharField(max_length=300, default="None")
    bank_name = models.CharField(max_length=150, default="None")
    bank_branch = models.CharField(max_length=150, default="None")
    bank_account = models.CharField(max_length=150, default="None")
    meta_data = models.CharField(max_length=1500, default="None")

    contact_person = models.CharField(max_length=150, default="None")
    alt_contact_number = models.CharField(max_length=150, default="None")

    contact_number = models.CharField(max_length=150, default="None")
    contact_email = models.CharField(max_length=150, default="None")
    vat_valid_expiry_date = models.CharField(max_length=150, default=".")
    tax_clearance_expiry_date = models.CharField(max_length=150, default=".")
    added_by = models.CharField(max_length=150, default=".")
    added_by_date = models.CharField(max_length=150, default=".")
    approved_by = models.CharField(max_length=150, default=".")
    approved_by_date = models.CharField(max_length=150, default=".")
    tax_complient = models.CharField(max_length=150, default=".")
    evaluated_by = models.CharField(max_length=150, default=".")

    evaluated = models.CharField(max_length=150, default=".")
    evaluated_by_date = models.CharField(max_length=150, default=".")
    evaluation_decision = models.CharField(max_length=150, default=".")
    rejector= models.CharField(max_length=150, default="None")
    rejector_message= models.CharField(max_length=500, default="None")
    rejector_date= models.CharField(max_length=500, default="None")
    def __str__(self):
        return self.name +", Supplies : "+self.meta_data
    
class SupplierDocs(models.Model):
    supplier_id = models.CharField(max_length=150, default="None")
    vat_path = models.CharField(max_length=500, default="#")
    tax_clearance_path = models.CharField(max_length=500, default="#")
    profile_path  = models.CharField(max_length=500, default="#")
    certificate_path  = models.CharField(max_length=500, default="#")




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
    purchase_request = models.CharField(max_length=100, default="None")

   
    company_name_supplier1 = models.CharField(max_length=450, default="None")
    company_name_supplier2 = models.CharField(max_length=450, default="None")
    company_name_supplier3 = models.CharField(max_length=450, default="None")
    
    item_name_supplier1 = models.CharField(max_length=450, default="None")
    item_name_supplier2 = models.CharField(max_length=450, default="None")
    item_name_supplier3 = models.CharField(max_length=450, default="None")

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

    rejector= models.CharField(max_length=150, default="None")
    rejector_message= models.CharField(max_length=500, default="None")
    rejector_date= models.CharField(max_length=500, default="None")
    completed= models.CharField(max_length=50, default="0")

    def __str__(self):
        return "Item : "+self.item_name_supplier1 +", Recommended Supplier"+self.recommended_supplier+", Supplier 1"+self.company_name_supplier1+", Supplier 2 : "+self.company_name_supplier2+", Supplier 3 : "+self.company_name_supplier1 +", Details"+self.desc_supplier1+", DOR "+self.requested_by_date



class Notifications(models.Model):
    trigger = models.CharField(max_length=220)
    date_time = models.CharField(max_length=120)
    message = models.CharField(max_length=420)
    to = models.CharField(max_length=200)
    status = models.CharField(max_length=220)

    def __str__(self):
        return self.message


class GoodsReceivedNote(models.Model):
    purchase_order = models.CharField(max_length=220,default="None")
    payment_request = models.CharField(max_length=220,default="None")
    status = models.CharField(max_length=220,default="None")
    supplier = models.CharField(max_length=220,default="None")
    dpt = models.CharField(max_length=220,default="None")
    item_name = models.CharField(max_length=220,default="None")
    desc = models.CharField(max_length=220,default="None")
    qnty = models.CharField(max_length=220,default="None")
    serial = models.CharField(max_length=220,default="None")
    comments = models.CharField(max_length=220,default="None")
    receiver = models.CharField(max_length=220,default="None")
    approver = models.CharField(max_length=220,default="None")

    receiver_date = models.CharField(max_length=220,default="None")
    approver_date = models.CharField(max_length=220,default="None")
    completed= models.CharField(max_length=50, default="0")
    rejector= models.CharField(max_length=150, default="None")
    rejector_message= models.CharField(max_length=500, default="None")
    rejector_date= models.CharField(max_length=500, default="None")

    def __str__(self):
        return "Item : "+self.item_name +", Supplier : "+self.supplier+", Details 1"+self.desc+", Recieving Department : "+self.dpt+", Status  : "+self.status +", DOR "+self.receiver_date

class GoodsReceivedNoteDnote(models.Model):
    request_id = models.CharField(max_length=255, blank=True)

    dnote_path = models.CharField(max_length=500, default="#")



class BudgetLines(models.Model):
    name= models.CharField(max_length=255, blank=True)
    project = models.CharField(max_length=255, blank=True)
    code = models.CharField(max_length=255, blank=True)
    amount = models.CharField(max_length=255, blank=True)
    balance = models.CharField(max_length=255, blank=True)
    subtract = models.CharField(max_length=255, blank=True)
    added_by = models.CharField(max_length=255, blank=True)
    added_by_date = models.CharField(max_length=255, blank=True)
    dpt = models.CharField(max_length=255, blank=True)
    last_used = models.CharField(max_length=255, blank=True)
    def __str__(self):
        return "Name : "+self.name +", Project : "+self.project+", code 1"+self.code+",  Department : "+self.dpt+", Balance  : "+self.balance +", Last Used "+self.last_used

class Project(models.Model):
    name= models.CharField(max_length=255, blank=True)
    code= models.CharField(max_length=255, blank=True)
    duration= models.CharField(max_length=255, blank=True)
    start_date= models.CharField(max_length=255, blank=True)
    end_date= models.CharField(max_length=255, blank=True)
    manager= models.CharField(max_length=255, blank=True)
    pi= models.CharField(max_length=255, blank=True)
    def __str__(self):
        return "Name : "+self.name +", Manager/Coordinator : "+self.manager+", PI "+self.pi+",  Start Date : "+self.start_date+", End Date  : "+self.end_date 


class Department(models.Model):
    name= models.CharField(max_length=255, blank=True)
    head= models.CharField(max_length=255, blank=True)
    def __str__(self):
        return "Name : "+self.name +", Head : "+self.head



class User(AbstractUser):
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        default=None
    )