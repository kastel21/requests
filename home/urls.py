from django.urls import path,  re_path

from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.index, name='index'),
        path('typography/', views.typography, name='typography'),
    path('color/', views.color, name='color'),
    path('icon-tabler/', views.icon_tabler, name='icon_tabler'),
    path('sample-page/', views.sample_page, name='sample_page'),

    # Authentication
    path('accounts/login/', views.UserLoginView.as_view(), name='login'),
    path('accounts/logout/', views.user_logout_view, name='logout'),
    path('accounts/register/', views.registration, name='register'),
    path('accounts/password-change/', views.UserPasswordChangeView.as_view(), name='password_change'),
    path('accounts/password-change-done/', auth_views.PasswordChangeDoneView.as_view(template_name='accounts/password_change_done.html'), name="password_change_done" ),
    path('accounts/password-reset/', views.UserPasswordResetView.as_view(), name='password_reset'),
    path('accounts/password-reset-confirm/<uidb64>/<token>/', 
        views.UserPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('accounts/password-reset-done/', auth_views.PasswordResetDoneView.as_view(
        template_name='accounts/password_reset_done.html'
    ), name='password_reset_done'),
    path('accounts/password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='accounts/password_reset_complete.html'
    ), name='password_reset_complete'),

    path('accounts/password-reset-confirm/<uidb64>/<token>/', views.UserPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('accounts/password-reset-done/', auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'), name='password_reset_done'),
    path('accounts/password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'), name='password_reset_complete'),

    # forms
    path('payment_request', views.payment_request, name='payment_request'),
    path('payment_request_all', views.payment_request_all, name='payment_request_all'),
    path('payment_request_approved', views.payment_request_approved, name='payment_request_approved'),
    re_path('payment_request_pending', views.payment_request_pending, name='payment_request_pending'),
    path('payment_request_pending_view', views.payment_request_pending_view, name='payment_request_pending_view'),

    path('payment_request_super', views.payment_request_super, name='payment_request_super'),
    path('payment_request_add', views.payment_request_add, name='payment_request_add'),
    re_path('payment_request_view', views.payment_request_view, name='payment_request_view'),
    re_path('payment_request_print', views.payment_request_print, name='payment_request_print'),
    re_path('payment_request_edit', views.payment_request_edit, name='payment_request_edit'),

    path('payment_request_edit_record', views.payment_request_edit_record, name='payment_request_edit_record'),
    path('payment_request_send_record', views.payment_request_send_record, name='payment_request_send_record'),
    path('payment_request_get_record', views.payment_request_get_record, name='payment_request_get_record'),


    path('payment_request_certify', views.payment_request_certify, name='payment_request_certify'),
    path('payment_request_clear', views.payment_request_clear, name='payment_request_clear'),
    path('payment_request_approve', views.payment_request_approve, name='payment_request_approve'),
    # path('payment_request_certify', views.payment_request_certify, name='payment_request_certify'),



    path('get_users', views.get_users, name='get_users'),
    # path('print', views.payment_request_print, name='print'),

    #comp schedule
    path('comp_schedule', views.comp_schedule, name='comp_schedule'),
    path('comp_schedule_all', views.comp_schedule_all, name='comp_schedule_all'),
    path('comp_schedule_approved', views.comp_schedule_approved, name='comp_schedule_approved'),
    path('comp_schedule_pending', views.comp_schedule_pending, name='comp_schedule_pending'),
    path('comp_schedule_super', views.comp_schedule_super, name='comp_schedule_super'),
    path('comp_schedule_add', views.comp_schedule_add, name='comp_schedule_add'),
    path('comp_schedule_send_record', views.comp_schedule_send_record, name='comp_schedule_send_record'),



    #purchase request
    path('purchase_request', views.purchase_request, name='purchase_request'),
    path('purchase_request_all', views.purchase_request_all, name='purchase_request_all'),
    path('purchase_request_approved', views.purchase_request_approved, name='purchase_request_approved'),
    path('purchase_request_pending', views.purchase_request_pending, name='purchase_request_pending'),
    path('purchase_request_super', views.purchase_request_super, name='purchase_request_super'),
    path('purchase_request_add', views.purchase_request_add, name='purchase_request_add'),
    path('purchase_request_send_record', views.purchase_request_send_record, name='purchase_request_send_record'),

    
]
