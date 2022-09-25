from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
from django.template import loader
import datetime
from .models import *
from .funk_otchet import *
from .forms import *
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import *

class ProfileAPIView(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer




def index(request):
    data = data_d(request)
    # добавить обработку имени и фамилии


    if request.method == 'POST' and request.POST['name_form'] == 'AddPepForm':
        form = AddPepForm(data=request.POST)
        data['form'] = form
        if form.is_valid():
            if form.cleaned_data['room'].is_full:
                messages.error(
                    request, f"{form.cleaned_data['room'].__str__()} занята, укажите другую"
                )

                return render(request, 'otchet/index.html', context=data)
            else:
                profile = Profile(
                    name=form.cleaned_data['name'],
                    phone_number=form.cleaned_data['phone_number'],
                    room=form.cleaned_data['room'],
                    room_number=form.cleaned_data['room'].number

                )
                profile.save()
                return render(request, 'otchet/done.html', context=data)

    if request.method == 'POST' and request.POST['name_form'] == 'AddPaymentsForm':
        addPayments(request)
        return render(request, 'otchet/done.html', context=data)

    if request.method == 'POST' and request.POST['name_form'] == 'AddSpendingAdminForm':
        form2 = AddSpendingAdminForm(data=request.POST)
        data['form2'] = form2
        if form2.is_valid():
            form2.save()

            return render(request, 'otchet/done.html', context=data)


    if request.method == 'POST' and request.POST['name_form'] == 'AddSpendingHostelForms':
        form3 = AddSpendingHostelForms(data=request.POST)
        data['form3'] = form3
        if form3.is_valid():
            form3.save()

            return render(request, 'otchet/done.html', context=data)


    if request.method == 'POST' and request.POST['name_form'] == 'AddSpendingBossForms':
        form4 = AddSpendingBossForms(data=request.POST)
        data['form4'] = form4
        if form4.is_valid():
            form4.save()

            return render(request, 'otchet/done.html', context=data)


    if request.method == 'POST' and request.POST['name_form'] == 'AddEventsForms':
        form5 = AddEventsForms(data=request.POST)
        data['form5'] = form5
        if form5.is_valid():
            form5.save()

            return render(request, 'otchet/done.html', context=data)


    if request.method == 'POST' and request.POST['name_form'] == 'DepartmentForm':
        form7 = DepartmentForm(data=request.POST)
        data['form7'] = form7
        if form7.is_valid():
            id = form7.cleaned_data['user'].id
            user_none = Profile.objects.get(id=id)
            depart = Departures(
                name=form7.cleaned_data['user'].name,
                phone_number=form7.cleaned_data['user'].phone_number,
                room=form7.cleaned_data['user'].room.number
            )
            user_none.delete()
            depart.save()

            return render(request, 'otchet/done.html', context=data)

    if request.method == 'POST' and request.POST['name_form'] == 'AddRefundsForms':
        addRefaunds(request)
        return render(request, 'otchet/done.html', context=data)

    return render(request, 'otchet/index.html', context=data)


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Вы успешно зарегистрировались")
            return redirect('login')
        else:
            messages.error(request, "Ошибка регистрации")
    else:
        form = UserRegisterForm()
    return render(request, 'otchet/register.html', {"form": form})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = UserLoginForm()
    return render(request, 'otchet/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('login')


def otchet(request):
    data = data_d(request)

    # проверка - сколько цифр в номере месяца
    if datetime.datetime.now().month < 10:
        month_now = '0' + str(datetime.datetime.now().month)
    else:
        month_now = datetime.datetime.now().month
    # конец проверки

    month_next = int(month_now) + 1

    data['month_now'] = month_now
    data['month_next'] = month_next

    data['summ_2_room'] = summ_room(2)
    data['summ_3_room'] = summ_room(3)
    data['summ_4_room'] = summ_room(4)
    data['summ_5_room'] = summ_room(5)
    data['summ_6_room'] = summ_room(6)
    data['summ_10_room'] = summ_room(10)
    data['summ_11_room'] = summ_room(11)
    data['summ_12_room'] = summ_room(12)
    data['summ_13_room'] = summ_room(13)
    data['summ_14_room'] = summ_room(14)
    data['summ_15_room'] = summ_room(15)
    data['summ_16_room'] = summ_room(16)
    data['summ_17_room'] = summ_room(17)
    data['suum_vsego'] = suum_vsego()[0]
    data['spending_boss'] = spending_for_month(SpendingBoss)
    data['spend_vsego_boss'] = spend_vsego(SpendingBoss)[0]
    data['spending_dom'] = spending_for_month(SpendingHostel)
    data['spend_vsego_dom'] = spend_vsego(SpendingHostel)[0]
    data['count_new_people'] = count_new_people()
    data['count_depart_people'] = arrivals_departures()
    data['events'] = list(Events.objects.all())
    data['spend_admin'] = spend_vsego(SpendingAdmin)[0]
    data['banca'] = point_in_number((
            suum_vsego()[1] -
            (
                spend_vsego(SpendingBoss)[1] +
                spend_vsego(SpendingHostel)[1] +
                spend_vsego(SpendingAdmin)[1]
            )
    ))



    return render(request, 'otchet/otchet.html', context=data)

def payments(request):
    data = data_d(request)
    payments = Payments.objects.all()
    paginator = Paginator(payments, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    data['page_obj'] = page_obj

    if request.method == 'POST' and request.POST['name_form'] == 'AddPaymentsForm':
        addPayments(request)
        return render(request, 'otchet/done.html', context=data)

    if request.method == 'POST' and request.POST['name_form'] == 'AddRefundsForms':
        addRefaunds(request)
        return render(request, 'otchet/done.html', context=data)

    return render(request, 'otchet/payments.html', context=data)


def update_payments(request, id_pay):
    data = data_d(request)
    pay = Payments.objects.get(id=id_pay)

    if request.method == 'POST' and request.POST['name_form'] == 'AddPaymentsForm':
        form1 = AddPaymentsForm(data=request.POST, instance=pay)
        data['form1'] = form1
        if form1.is_valid():
            form1.save()
            return render(request, 'otchet/done.html', context=data)
    else:
        form1 = AddPaymentsForm(instance=pay)
        data['form1'] = form1
    return render(request, 'otchet/update_payments.html', context=data)


def delete_payments(request, id_pay):
    pay = Payments.objects.get(id=id_pay)
    pay.delete()
    return redirect('payments')


def peoples(request):
    data = data_d(request)
    peoples = Profile.objects.all()
    paginator = Paginator(peoples, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    data['page_obj'] = page_obj
    data['peoples'] = peoples
    if request.method == 'POST' and request.POST['name_form'] == 'AddPepForm':
        form = AddPepForm(data=request.POST)
        data['form'] = form
        if form.is_valid():
            if form.cleaned_data['room'].is_full:
                messages.error(
                    request, f"{form.cleaned_data['room'].__str__()} занята, укажите другую"
                )

                return render(request, 'otchet/index.html', context=data)
            else:
                profile = Profile(
                    name=form.cleaned_data['name'],
                    phone_number=form.cleaned_data['phone_number'],
                    room=form.cleaned_data['room'],
                    room_number=form.cleaned_data['room'].number

                )
                profile.save()
                return render(request, 'otchet/done.html', context=data)

    if request.method == 'POST' and request.POST['name_form'] == 'DepartmentForm':
        form7 = DepartmentForm(data=request.POST)
        data['form7'] = form7
        if form7.is_valid():
            id = form7.cleaned_data['user'].id
            user_none = Profile.objects.get(id=id)
            depart = Departures(
                name=form7.cleaned_data['user'].name,
                phone_number=form7.cleaned_data['user'].phone_number,
                room=form7.cleaned_data['user'].room.number
            )
            user_none.delete()
            depart.save()

            return render(request, 'otchet/done.html', context=data)

    return render(request, 'otchet/people.html', context=data)


def update_peoples(request, id_people):
    data = data_d(request)
    people = Profile.objects.get(id=id_people)

    if request.method == 'POST' and request.POST['name_form'] == 'AddPepForm':
        form = AddPepForm(data=request.POST, instance=people)
        data['form'] = form
        if form.is_valid():
            if form.cleaned_data['room'].is_full:
                messages.error(
                    request, f"{form.cleaned_data['room'].__str__()} занята, укажите другую"
                )

                return render(request, 'otchet/index.html', context=data)
            else:
                form.save()
                return render(request, 'otchet/done.html', context=data)
    else:
        form = AddPepForm(instance=people)
        data['form'] = form
    return render(request, 'otchet/update_peoples.html', context=data)


def delete_peoples(request, id_people):
    people = Profile.objects.get(id=id_people)
    people.delete()
    return redirect('peoples')


def spendinghostel(request):
    data = data_d(request)
    spend_hostel = SpendingHostel.objects.all()
    paginator = Paginator(spend_hostel, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    data['page_obj'] = page_obj

    if request.method == 'POST' and request.POST['name_form'] == 'AddSpendingHostelForms':
        form3 = AddSpendingHostelForms(data=request.POST)
        data['form3'] = form3
        if form3.is_valid():
            form3.save()

            return render(request, 'otchet/done.html', context=data)

    return render(request, 'otchet/spending_hostel.html', context=data)


def update_spendinghostel(request, id_spend):
    data = data_d(request)
    spend = SpendingHostel.objects.get(id=id_spend)

    if request.method == 'POST' and request.POST['name_form'] == 'AddSpendingHostelForms':
        form3 = AddSpendingHostelForms(data=request.POST, instance=spend)
        data['form3'] = form3
        if form3.is_valid():
            form3.save()
            return render(request, 'otchet/done.html', context=data)
    else:
        form3 = AddSpendingHostelForms(instance=spend)
        data['form3'] = form3
    return render(request, 'otchet/updadte_spending_hostel.html', context=data)


def delete_spendinghostel(request, id_spend):
    spend = SpendingHostel.objects.get(id=id_spend)
    spend.delete()
    return redirect('spendinghostel')

def spendingadmin(request):
    data = data_d(request)
    spend_admin = SpendingAdmin.objects.all()
    paginator = Paginator(spend_admin, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    data['page_obj'] = page_obj

    if request.method == 'POST' and request.POST['name_form'] == 'AddSpendingAdminForm':
        form2 = AddSpendingAdminForm(data=request.POST)
        data['form2'] = form2
        if form2.is_valid():
            form2.save()

            return render(request, 'otchet/done.html', context=data)

    return render(request, 'otchet/spending_admin.html', context=data)


def update_spendingadmin(request, id_spend):
    data = data_d(request)
    spend = SpendingAdmin.objects.get(id=id_spend)

    if request.method == 'POST' and request.POST['name_form'] == 'AddSpendingAdminForm':
        form2 = AddSpendingAdminForm(data=request.POST, instance=spend)
        data['form2'] = form2
        if form2.is_valid():
            form2.save()
            return render(request, 'otchet/done.html', context=data)
    else:
        form2 = AddSpendingAdminForm(instance=spend)
        data['form2'] = form2
    return render(request, 'otchet/update_spend_admin.html', context=data)


def delete_spendingadmin(request, id_spend):
    spend = SpendingAdmin.objects.get(id=id_spend)
    spend.delete()
    return redirect('spendingadmin')

def spendingboss(request):
    data = data_d(request)
    spend_boss = SpendingBoss.objects.all()
    paginator = Paginator(spend_boss, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    data['page_obj'] = page_obj

    if request.method == 'POST' and request.POST['name_form'] == 'AddSpendingBossForms':
        form4 = AddSpendingBossForms(data=request.POST)
        data['form4'] = form4
        if form4.is_valid():
            form4.save()

            return render(request, 'otchet/done.html', context=data)

    return render(request, 'otchet/spending_boss.html', context=data)

def update_spendingboss(request, id_spend):
    data = data_d(request)
    spend = SpendingBoss.objects.get(id=id_spend)

    if request.method == 'POST' and request.POST['name_form'] == 'AddSpendingBossForms':
        form4 = AddSpendingBossForms(request.POST, instance=spend)
        if form4.is_valid():
            form4.save()

            return render(request, 'otchet/done.html', context=data)
    else:
        form4 = AddSpendingBossForms(instance=spend)
        data['form4'] = form4
    return render(request, 'otchet/update_spending_boss.html', context=data)

def delete_spendingboss(request, id_spend):
    spend = SpendingBoss.objects.get(id=id_spend)
    spend.delete()
    return redirect('spendingboss')


def events(request):
    data = data_d(request)
    events = Events.objects.all()
    paginator = Paginator(events, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    data['page_obj'] = page_obj

    if request.method == 'POST' and request.POST['name_form'] == 'AddEventsForms':
        form5 = AddEventsForms(data=request.POST)
        data['form5'] = form5
        if form5.is_valid():
            form5.save()

            return render(request, 'otchet/done.html', context=data)

    return render(request, 'otchet/events.html', context=data)


def update_events(request, id_event):
    data = data_d(request)
    event = Events.objects.get(id=id_event)

    if request.method == 'POST' and request.POST['name_form'] == 'AddEventsForms':
        form5 = AddEventsForms(request.POST, instance=event)
        if form5.is_valid():
            form5.save()
            return render(request, 'otchet/done.html', context=data)
    else:
        form5 = AddEventsForms(instance=event)
        data['form5'] = form5
    return render(request, 'otchet/update_event.html', context=data)


def delete_events(request, id_event):
    event = Events.objects.get(id=id_event)
    event.delete()
    return redirect('events')


