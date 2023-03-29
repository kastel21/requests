from django.db import models

# Create your models here.



class PuchaseRequest(models.Model):
    request_id = models.CharField(max_length=30, default="username")
    requester = models.CharField(max_length=30, default="username")
    date_of_request = models.CharField(max_length=15, default="2023")
    requesting_dpt = models.CharField(max_length=150, default=".")
    request_justification = models.CharField(max_length=450, default=".")
    name_address_of_supplier = models.CharField(max_length=550, default=".")
    budget_line_item = models.CharField(max_length=150, default=".")
   
    qnty = models.CharField(max_length=150, default=".")
    item_number = models.CharField(max_length=150, default=".")
    description = models.CharField(max_length=150, default=".")
    unit_price = models.CharField(max_length=150, default=".")
    total = models.CharField(max_length=150, default=".")
   
    supervisor_approved = models.CharField(max_length=150, default=".")
    supervisor_approved_date= models.CharField(max_length=150, default=".")
    accounts_clerk_approved= models.CharField(max_length=150, default=".")
    accounts_clerk_approved_date= models.CharField(max_length=150, default=".")




class PaymentRequest(models.Model):
    request_id = models.CharField(max_length=30, default="username")
    compiled_by = models.CharField(max_length=30, default="username")
    date_of_request = models.CharField(max_length=15, default="2023")
    payee = models.CharField(max_length=150, default=".")
    payment_type = models.CharField(max_length=450, default=".")
    amount = models.CharField(max_length=550, default=".")
    project_number = models.CharField(max_length=150, default=".")
   
    account_code = models.CharField(max_length=150, default=".")
    details = models.CharField(max_length=150, default=".")
    amount = models.CharField(max_length=150, default=".")
    # unit_price = models.CharField(max_length=150, default=".")
    total = models.CharField(max_length=150, default=".")
   
    certified_by = models.CharField(max_length=150, default=".")
    certified_by_date = models.CharField(max_length=150, default=".")

    cleared_by_fin_man= models.CharField(max_length=150, default=".")
    cleared_by_fin_man_date= models.CharField(max_length=150, default=".")

    approved_by_project_man= models.CharField(max_length=150, default=".")
    approved_by_project_man_date= models.CharField(max_length=150, default=".")

    approved_by= models.CharField(max_length=150, default=".")
    approved_by_date= models.CharField(max_length=150, default=".")


class ComparativeSchedule(models.Model):
    request_id = models.CharField(max_length=30, default="username")
    payee = models.CharField(max_length=150, default=".")
   
    company_name_supplier1 = models.CharField(max_length=450, default=".")
    company_name_supplier2 = models.CharField(max_length=450, default=".")
    company_name_supplier3 = models.CharField(max_length=450, default=".")
    
    item_number_supplier1 = models.CharField(max_length=450, default=".")
    item_number_supplier2 = models.CharField(max_length=450, default=".")
    item_number_supplier3 = models.CharField(max_length=450, default=".")

    desc_supplier1 = models.CharField(max_length=450, default=".")
    desc_supplier2 = models.CharField(max_length=450, default=".")
    desc_supplier3 = models.CharField(max_length=450, default=".")


    qnty_supplier1 = models.CharField(max_length=450, default=".")
    qnty_supplier2 = models.CharField(max_length=450, default=".")
    qnty_supplier3 = models.CharField(max_length=450, default=".")


    unit_price_supplier1 = models.CharField(max_length=450, default=".")
    unit_price_supplier2 = models.CharField(max_length=450, default=".")
    unit_price_supplier3 = models.CharField(max_length=450, default=".")

    total_price_supplier1 = models.CharField(max_length=450, default=".")
    total_price_supplier2 = models.CharField(max_length=450, default=".")
    total_price_supplier3 = models.CharField(max_length=450, default=".")

    recommended_supplier = models.CharField(max_length=15, default="2023")
    recommended_supplier_reason = models.CharField(max_length=150, default=".")

    
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

    project_number = models.CharField(max_length=150, default=".")

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
