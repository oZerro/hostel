from django.contrib import admin

from .models import *


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ['number', 'price_for_period', 'number_of_beds']
    list_editable = ['price_for_period', 'number_of_beds']


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['date', 'name', 'phone_number', 'room']
    list_editable = ['room']

@admin.register(Departures)
class DeparturesAdmin(admin.ModelAdmin):
    list_display = ['date', 'user', 'phone_number']
    list_editable = []


@admin.register(Payments)
class PaymentsAdmin(admin.ModelAdmin):
    list_display = ['user', 'name', 'date', 'method', 'summa']
    list_editable = []


@admin.register(Refunds)
class RefundsAdmin(admin.ModelAdmin):
    list_display = ['user', 'date', 'method', 'summa']
    list_editable = []


@admin.register(SpendingAdmin)
class SpendingAdmin(admin.ModelAdmin):
    list_display = ['date', 'summa', 'note']
    list_editable = ['summa', 'note']


@admin.register(SpendingHostel)
class SpendingHostelAdmin(admin.ModelAdmin):
    list_display = ['date', 'summa', 'note']
    list_editable = ['summa', 'note']


@admin.register(SpendingBoss)
class SpendingBossAdmin(admin.ModelAdmin):
    list_display = ['date', 'summa', 'note']
    list_editable = ['summa', 'note']


@admin.register(Events)
class EventsAdmin(admin.ModelAdmin):
    list_display = ['date', 'event']
    list_editable = ['event']







# Register your models here.
