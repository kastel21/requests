from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(PaymentRequestPOP)
admin.site.register(Supplier)
admin.site.register(SupplierDocs)

admin.site.register(Project)
admin.site.register(BudgetLines)
admin.site.register(Department)
admin.site.register(User)




