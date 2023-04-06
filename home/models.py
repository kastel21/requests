from django.db import models

# Create your models here.



class PuchaseRequest(models.Model):
    request_id = models.CharField(max_length=30, default="username")
    requester = models.CharField(max_length=30, default="username")
    date_of_request = models.CharField(max_length=15, default="2023")
    requesting_dpt = models.CharField(max_length=150, default="None")
    request_justification = models.CharField(max_length=450, default="None")
    name_address_of_supplier = models.CharField(max_length=550, default="None")
    budget_line_item = models.CharField(max_length=150, default="None")
   
    qnty = models.CharField(max_length=150, default="None")
    item_number = models.CharField(max_length=150, default="None")
    description = models.CharField(max_length=150, default="None")
    unit_price = models.CharField(max_length=150, default="None")
    total = models.CharField(max_length=150, default="None")
   
    supervisor_approved = models.CharField(max_length=150, default="None")
    supervisor_approved_date= models.CharField(max_length=150, default="None")
    accounts_clerk_approved= models.CharField(max_length=150, default="None")
    accounts_clerk_approved_date= models.CharField(max_length=150, default="None")




class PaymentRequest(models.Model):
    request_id = models.CharField(max_length=30, default="username")
    compiled_by = models.CharField(max_length=30, default="username")
    date_of_request = models.CharField(max_length=15, default="2023")
    payee = models.CharField(max_length=150, default="None")
    payment_type = models.CharField(max_length=450, default="None")
    # amount = models.CharField(max_length=550, default="None")
    project_number = models.CharField(max_length=150, default="None")
   
    account_code = models.CharField(max_length=150, default="None")
    details = models.CharField(max_length=150, default="None")
    amount = models.CharField(max_length=150, default="None")
    qnty = models.CharField(max_length=150, default="None")
    total = models.CharField(max_length=150, default="None")
   
    certified_by = models.CharField(max_length=150, default="None")
    certified_by_date = models.CharField(max_length=150, default="None")

    cleared_by_fin_man= models.CharField(max_length=150, default="None")
    cleared_by_fin_man_date= models.CharField(max_length=150, default="None")

    approved_by_project_man= models.CharField(max_length=150, default="None")
    approved_by_project_man_date= models.CharField(max_length=150, default="None")

    approved_by= models.CharField(max_length=150, default="None")
    approved_by_date= models.CharField(max_length=150, default="None")


class ComparativeSchedule(models.Model):
    request_id = models.CharField(max_length=30, default="username")
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

    recommended_supplier = models.CharField(max_length=15, default="2023")
    recommended_supplier_reason = models.CharField(max_length=150, default="None")

    
    dpt_project_requesting = models.CharField(max_length=15, default="2023")

    requested_by = models.CharField(max_length=30, default="username")
    requested_by_sig = models.CharField(max_length=30, default="username")
    requested_by_date = models.CharField(max_length=30, default="username")


    
    tech_person_by = models.CharField(max_length=30, default="username")
    tech_person_by_sig = models.CharField(max_length=30, default="username")
    tech_person_date = models.CharField(max_length=30, default="username")

    dpt_head_by = models.CharField(max_length=30, default="username")
    dpt_head_by_sig = models.CharField(max_length=30, default="username")
    dpt_head_date = models.CharField(max_length=30, default="username")

    team_lead_by = models.CharField(max_length=30, default="username")
    team_lead_by_sig = models.CharField(max_length=30, default="username")
    team_lead_date = models.CharField(max_length=30, default="username")

    approved_by = models.CharField(max_length=30, default="username")
    approved_by_sig = models.CharField(max_length=30, default="username")
    approved_date = models.CharField(max_length=30, default="username")

    project_number = models.CharField(max_length=150, default="None")

# =======
# class Purchase_Requisition(models.Model):
#     requesting_department = models.CharField(max_length=220)
#     request_justification = models.CharField(max_length=120)
#     name_of_supplier = models.CharField(max_length=220)
#     name_address_of_supplier = models.DateField(auto_now_add=True)
#     budget_line_item = models.CharField(max_length=220)
#     qty = models.CharField(max_length=220)
#     item_no = models.CharField(max_length=220)
#     description = models.CharField(max_length=220)
#     unit_price = models.CharField(max_length=220)
#     total = models.CharField(max_length=220)
#     signature_of_requestor =models.CharField(max_length=220)
#     date_requestor = models.DateField(auto_now_add=True)
#     signature_of_supervisor_pi = models.CharField(max_length=220)
#     date_supervisor_pi = models.DateField(auto_now_add=True)
#     Signature_of_accounts_cleck = models.CharField(max_length=220)
#     date_accounts_cleck = models.DateField(auto_now_add=True)

#     def __str__(self):
#         return self.requesting_department
# >>>>>>> 4db80039bb00407c8d8198d042496bf317a9bc6e
