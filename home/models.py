from django.db import models

# Create your models here.
class Purchase_Requisition(models.Model):
    requesting_department = models.CharField(max_length=220)
    request_justification = models.CharField(max_length=120)
    name_of_supplier = models.CharField(max_length=220)
    name_address_of_supplier = models.DateField(auto_now_add=True)
    budget_line_item = models.CharField(max_length=220)
    qty = models.CharField(max_length=220)
    item_no = models.CharField(max_length=220)
    description = models.CharField(max_length=220)
    unit_price = models.CharField(max_length=220)
    total = models.CharField(max_length=220)
    signature_of_requestor =models.CharField(max_length=220)
    date_requestor = models.DateField(auto_now_add=True)
    signature_of_supervisor_pi = models.CharField(max_length=220)
    date_supervisor_pi = models.DateField(auto_now_add=True)
    Signature_of_accounts_cleck = models.CharField(max_length=220)
    date_accounts_cleck = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.requesting_department