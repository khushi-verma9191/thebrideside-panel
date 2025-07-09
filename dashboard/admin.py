from django.contrib import admin
from .models import Lead, SalesRep, CallSchedule
# Register your models here.

admin.site.register(Lead)
admin.site.register(SalesRep)
admin.site.register(CallSchedule)
