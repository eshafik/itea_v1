from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .custom_decorator import finance_user_required, executive_user_required
from .models import IndividualBalance, OrganizationBalance
from .forms import IndividualBalanceForm, OrganizationBalanceForm
from account.models import Profile
# Create your views here.

@finance_user_required
def add_balance(request,username):
    user = get_object_or_404(User,username=username)
    if request.method=='POST':
        balance_form = IndividualBalanceForm(instance=user.individualbalance, data=request.POST)
        if balance_form.is_valid():
            amount = balance_form.cleaned_data['add_balance']
            new_balance = balance_form.save(commit=False)
            new_balance.balance += amount
            new_balance.user = user
            new_balance.save()
            messages.success(request,'Balance updated successfully.')
        else:
            messages.error(request,'Error updating your Balance.')
    else:
        balance_form = IndividualBalanceForm(instance=user.individualbalance)
    return render(request,'balance/individual_balance.html',{'balance_form':balance_form,'user':user})
    

@finance_user_required
def active_members(request):
    members = Profile.objects.filter(status=True)
    return render(request,'balance/active_members.html',{'members':members})


@login_required
def org_detail(request):
    org_details = get_object_or_404(OrganizationBalance,id=1)
    return render(request,'balance/org_detail.html',{'org_details':org_details})
   

@executive_user_required
def org_edit(request):
    org_obj = get_object_or_404(OrganizationBalance,id=1)
    if request.method == 'POST':
        org_form = OrganizationBalanceForm(instance=org_obj,data=request.POST)
        if org_form.is_valid():
            org_form.save()
            messages.success(request,'Organization Status edited successfully.')
        else:
             messages.error(request,'Error editing your Organization Status.')
    else:
        org_form = OrganizationBalanceForm(instance=org_obj)

    return render(request,'balance/org_edit.html',{'org_form':org_form})
        
