from django.contrib import admin
from . models import IndividualBalance,OrganizationBalance
# Register your models here.

@admin.register(IndividualBalance)
class IndividualBalanceAdmin(admin.ModelAdmin):
    list_display = ('user','balance','due_month','payment_details')
    list_filter = ('user','balance','updated')
    search_fields = ('user','balance')
    date_hierarchy = 'updated'


@admin.register(OrganizationBalance)
class IndividualBalanceAdmin(admin.ModelAdmin):
    list_display = ('capital','total_profit','total_loss','investment_details')
