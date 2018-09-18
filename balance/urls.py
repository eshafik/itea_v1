from django.urls import path
from . import views

app_name="balance"

urlpatterns=[
    path('active_members/',views.active_members,name="active_members"),
    path('add_balance/<slug:username>',views.add_balance,name="add_balance"),
    path('org_edit/',views.org_edit,name='org_edit'),
    path('org_detail/',views.org_detail,name='org_detail'),
]