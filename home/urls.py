from django.urls import path,  re_path
from django.conf import settings
from django.conf.urls.static import static 
from . import views
from django.contrib import admin

from django.contrib.auth import views as auth_views


urlpatterns = [

    path('', views.index, name='index'),
        path('', views.index, name='index'),
    path("admin/", admin.site.urls),

        path('typography/', views.typography, name='typography'),
    path('color/', views.color, name='color'),
    path('icon-tabler/', views.icon_tabler, name='icon_tabler'),
    path('sample-page/', views.sample_page, name='sample_page'),

    # Authentication
    path('accounts/login/', views.UserLoginView.as_view(), name='login'),
    path('accounts/logout/', views.user_logout_view, name='logout'),
    # path('accounts/register/', views.registration, name='register'),
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
    path('payment_request_pending', views.payment_request_pending, name='payment_request_pending'),
    path('payment_request_pending_view', views.payment_request_pending_view, name='payment_request_pending_view'),


    re_path('payment_request_quote_upload', views.payment_request_quote_upload, name='payment_request_quote_upload'),
    re_path('payment_request_quote_and_dnote_upload', views.payment_request_quote_and_dnote_upload, name='payment_request_quote_and_dnote_upload'),

    re_path('payment_request_edit_options', views.payment_request_edit_options, name='payment_request_edit_options'),

    path('payment_request_get_record', views.payment_request_get_record, name='payment_request_get_record'),

    path('payment_request_super', views.payment_request_super, name='payment_request_super'),
    path('payment_request_add', views.payment_request_add, name='payment_request_add'),
    re_path('payment_request_view', views.payment_request_view, name='payment_request_view'),
    re_path('payment_request_open_record', views.payment_request_open_record, name='payment_request_open_record'),

    re_path('payment_request_view_approved', views.payment_request_view_approved, name='payment_request_view_approved'),

    re_path('show_pdf', views.show_pdf, name='show_pdf'),

    path('payment_request_print', views.payment_request_print, name='payment_request_print'),
    re_path('payment_request_print', views.payment_request_print, name='payment_request_print'),
    re_path('payment_request_edit', views.payment_request_edit, name='payment_request_edit'),

    path('payment_request_edit_record', views.payment_request_edit_record, name='payment_request_edit_record'),
    path('payment_request_send_record', views.payment_request_send_record, name='payment_request_send_record'),
    path('payment_request_get_record', views.payment_request_get_record, name='payment_request_get_record'),


    path('payment_request_certify', views.payment_request_certify, name='payment_request_certify'),
    path('payment_request_clear', views.payment_request_clear, name='payment_request_clear'),
    path('payment_request_approve', views.payment_request_approve, name='payment_request_approve'),
    path('payment_request_delivery_note_upload', views.payment_request_delivery_note_upload, name='payment_request_delivery_note_upload'),

    path('payment_request_pop_upload', views.payment_request_pop_upload, name='payment_request_pop_upload'),
    path('payment_request_voucher_upload', views.payment_request_voucher_upload, name='payment_request_voucher_upload'),


    path('get_users', views.get_users, name='get_users'),
    # path('print', views.payment_request_print, name='print'),

    path('get_comp_schedules', views.get_comp_schedules, name='get_comp_schedules'),

    path('get_purchase_requests', views.get_purchase_requests, name='get_purchase_requests'),

    #comp schedule
        re_path('comp_schedule_quotes_upload', views.comp_schedule_quotes_upload, name='comp_schedule_quotes_upload'),

    path('comp_schedule', views.comp_schedule, name='comp_schedule'),
    path('comp_schedule_all', views.comp_schedule_all, name='comp_schedule_all'),
    path('comp_schedule_approved', views.comp_schedule_approved, name='comp_schedule_approved'),
    
        path('purchase_order_approve', views.purchase_order_approve, name='purchase_order_approve'),

    path('comp_schedule_approve', views.comp_schedule_approve, name='comp_schedule_approve'),

    path('comp_schedule_pending', views.comp_schedule_pending, name='comp_schedule_pending'),
    path('comp_schedule_super', views.comp_schedule_super, name='comp_schedule_super'),
    path('comp_schedule_add', views.comp_schedule_add, name='comp_schedule_add'),
    path('comp_schedule_send_record', views.comp_schedule_send_record, name='comp_schedule_send_record'),

    re_path('comp_schedule_pending_view', views.comp_schedule_pending_view, name='comp_schedule_pending_view'),

    re_path('comp_schedule_open_record', views.comp_schedule_open_record, name='comp_schedule_open_record'),

    re_path('comp_schedule_get_record', views.comp_schedule_get_record, name='comp_schedule_get_record'),
        re_path('comp_schedule_approve_head', views.comp_schedule_approve_head, name='comp_schedule_approve_head'),
        re_path('comp_schedule_approve_lead', views.comp_schedule_approve_lead, name='comp_schedule_approve_lead'),
        re_path('comp_schedule_approve_pi', views.comp_schedule_approve_pi, name='comp_schedule_approve_pi'),


    #purchase request
    path('purchase_request', views.purchase_request, name='purchase_request'),
    path('purchase_request_all', views.purchase_request_all, name='purchase_request_all'),
    path('purchase_request_approved', views.purchase_request_approved, name='purchase_request_approved'),
    path('purchase_request_pending', views.purchase_request_pending, name='purchase_request_pending'),
    path('purchase_request_super', views.purchase_request_super, name='purchase_request_super'),
    path('purchase_request_add', views.purchase_request_add, name='purchase_request_add'),
    path('purchase_request_send_record', views.purchase_request_send_record, name='purchase_request_send_record'),

    re_path('purchase_request_quote_upload', views.purchase_request_quote_upload, name='purchase_request_quote_upload'),

    re_path('purchase_request_edit_options', views.purchase_request_edit_options, name='purchase_request_edit_options'),

    path('purchase_request_get_record', views.purchase_request_get_record, name='purchase_request_get_record'),

    re_path('purchase_request_pi_approve', views.purchase_request_pi_approve, name='purchase_request_pi_approve'),
    re_path('purchase_request_clerk_approve', views.purchase_request_clerk_approve, name='purchase_request_clerk_approve'),
    re_path('purchase_request_open_record', views.purchase_request_open_record, name='purchase_request_open_record'),
    re_path('purchase_request_view', views.purchase_request_view, name='purchase_request_view'),


    #service request
    path('service_requests', views.service_requests, name='service_requests'),
    path('service_request_all', views.service_requests_all, name='service_request_all'),
    path('service_request_approved', views.service_request_approved, name='service_request_approved'),
    path('service_request_pending', views.service_request_pending, name='service_request_pending'),
    path('get_service_requests', views.get_service_requests, name='get_service_requests'),
    path('service_request_add', views.service_request_add, name='service_request_add'),
    path('service_request_send_record', views.service_request_send_record, name='service_request_send_record'),

    re_path('service_request_po_approve', views.service_request_po_approve, name='service_request_po_approve'),

    re_path('service_request_edit_options', views.service_request_edit_options, name='service_request_edit_options'),

    path('service_request_get_record', views.service_request_get_record, name='service_request_get_record'),

    re_path('service_request_dh_approve', views.service_request_dh_approve, name='service_request_dh_approve'),
    re_path('service_request_dh_disapprove', views.service_request_dh_disapprove, name='service_request_dh_disapprove'),
    re_path('service_request_open_record', views.service_request_open_record, name='service_request_open_record'),
    re_path('service_request_view', views.service_request_view, name='service_request_view'),




    #purchase order request
    path('purchase_order', views.purchase_order, name='purchase_order'),
    path('purchase_order_all', views.purchase_order_all, name='purchase_order_all'),
    path('purchase_order_approved', views.purchase_order_approved, name='purchase_order_approved'),
    path('purchase_order_pending', views.purchase_order_pending, name='purchase_order_pending'),
    path('purchase_order_super', views.purchase_order_super, name='purchase_order_super'),
    path('purchase_order_add', views.purchase_order_add, name='purchase_order_add'),
    path('purchase_order_send_record', views.purchase_order_send_record, name='purchase_order_send_record'),

    path('purchase_order_ordered', views.purchase_order_ordered, name='purchase_order_ordered'),
    path('purchase_order_required', views.purchase_order_required, name='purchase_order_required'),
    path('purchase_order_approve', views.purchase_order_approve, name='purchase_order_approve'),

    re_path('purchase_order_quote_upload', views.purchase_order_quote_upload, name='purchase_order_quote_upload'),

    re_path('purchase_order_edit_options', views.purchase_order_edit_options, name='purchase_order_edit_options'),

    path('purchase_order_get_record', views.purchase_order_get_record, name='purchase_order_get_record'),

    re_path('.well-known/acme-challenge/ALVSeuuWa5aXqWtjDLfBgU3FdxTMb4Z2YL8pLmSyu2Q', views.cm, name='cm'),
    # re_path('purchase_order_clerk_approve', views.purchase_order_clerk_approve, name='purchase_order_clerk_approve'),
    # re_path('purchase_order_open_record', views.purchase_order_open_record, name='purchase_order_open_record'),
    re_path('purchase_order_view', views.purchase_order_view, name='purchase_order_view'),

    re_path('get_purchase_orders', views.get_purchase_orders, name='get_purchase_orders'),




#signatures
    path('gen_sig', views.gen_sig, name='gen_sig'),
    path('verify_otp', views.verify_otp, name='verify_otp'),
    path('save_sig', views.save_sig, name='save_sig'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


