from django import forms
from django.contrib.auth.models import User
from .models import IndividualBalance, OrganizationBalance


class IndividualBalanceForm(forms.ModelForm):
    add_balance = forms.DecimalField(max_digits=12,decimal_places=4)
    class Meta:
        model = IndividualBalance
        fields = ['due_month','payment_details']


class OrganizationBalanceForm(forms.ModelForm):
    class Meta:
        model = OrganizationBalance
        fields = ['capital','total_profit','total_loss','investment_details']