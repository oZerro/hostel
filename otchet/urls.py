from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('otchet', views.otchet, name='otchet'),
    path('payments/', views.payments, name='payments'),
    path('update_payments/<int:id_pay>', views.update_payments, name='update_payments'),
    path('delete_payments/<int:id_pay>', views.delete_payments, name='delete_payments'),
    path('peoples/', views.peoples, name='peoples'),
    path('update_peoples/<int:id_people>', views.update_peoples, name='update_peoples'),
    path('delete_peoples/<int:id_people>', views.delete_peoples, name='delete_peoples'),

    path('spendinghostel/', views.spendinghostel, name='spendinghostel'),
    path('update_spendinghostel/<int:id_spend>', views.update_spendinghostel, name='update_spendinghostel'),
    path('delete_spendinghostel/<int:id_spend>', views.delete_spendinghostel, name='delete_spendinghostel'),

    path('spendingadmin/', views.spendingadmin, name='spendingadmin'),
    path('update_spendingadmin/<int:id_spend>', views.update_spendingadmin, name='update_spendingadmin'),
    path('delete_spendingadmin/<int:id_spend>', views.delete_spendingadmin, name='delete_spendingadmin'),

    path('spendingboss/', views.spendingboss, name='spendingboss'),
    path('update_spendingboss/<int:id_spend>', views.update_spendingboss, name='update_spendingboss'),
    path('delete_spendingboss/<int:id_spend>', views.delete_spendingboss, name='delete_spendingboss'),

    path('events/', views.events, name='events'),
    path('update_events/<int:id_event>', views.update_events, name='update_events'),
    path('delete_events/<int:id_event>', views.delete_events, name='delete_events'),

    path('register/', views.register, name='register'),
    path('login', views.user_login, name='login'),
    path('logout', views.user_logout, name='logout'),


]