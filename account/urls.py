from django.urls import path,include
from django.conf.urls import url

from django.contrib.auth import views as auth_views
from . import views


# app_name = "account"

urlpatterns = [
    path('login/',auth_views.LoginView.as_view(), name='login'),
    path('logout/',auth_views.LogoutView.as_view(), name='logout'),
    # #password change url
    # path('password_change/',auth_views.PasswordChangeView.as_view(),name='password_change'),
    # path('password_change/done/',auth_views.PasswordChangeDoneView.as_view(),name='password_change_done'),
    # #password reset url
    # path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    # path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    # path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    path('', include('django.contrib.auth.urls')),

    #registration
    path('register/',views.register,name="register"),
    path('',views.dashboard, name='dashboard'),

    #profile edit
    path('edit/',views.edit,name='edit'),
    #profile details
    path('@/<slug:username>/',views.profile_details,name='profile_details'),

    path('all_members/',views.all_members,name='all_members'),
    # url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    #     views.activate, name='activate'),
    path('activate/<uidb64>/<token>/',views.activate, name='activate'),
]