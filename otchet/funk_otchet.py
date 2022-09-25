from .models import *
from .forms import *
import datetime
from django.shortcuts import render

def data_d(request):
    data = {}
    if request.user.is_authenticated and User.is_staff:
        name = request.user.first_name
        surname = request.user.last_name
        payments = list(Payments.objects.all())[:5]
        data = {
            'name': name,
            'surname': surname,
            'payments': payments
        }

    elif request.user.is_authenticated:
        name = request.user.first_name
        surname = request.user.last_name
        data = {
            'name': name,
            'surname': surname
        }

    data['form'] = AddPepForm()
    data['form1'] = AddPaymentsForm()
    data['form2'] = AddSpendingAdminForm()
    data['form3'] = AddSpendingHostelForms()
    data['form4'] = AddSpendingBossForms()
    data['form5'] = AddEventsForms()
    data['form6'] = AddRefundsForms()
    data['form7'] = DepartmentForm()

    return data


def summ_room(number):
    arr_suum = []
    for pay in Payments.objects.all():
        if (
                int(pay.room) == number and
                datetime.datetime.now().month == pay.date.month
        ):
            arr_suum.append(pay.summa)
    return point_in_number(sum(arr_suum))

def point_in_number(arr):  # расставляет точки в больших числах
    if arr < 0:
        s = list(str(arr)[1:])
    else:
        s = list(str(arr))

    count = 0
    i = 0
    while i < len(s) - 1:
        count += 1
        i += 1
        if count == 3:
            s.insert(len(s) - i, '.')
            count = 0
            i += 1
    if arr < 0:
        return "-" + "".join(s)
    else:
        return "".join(s)

def suum_vsego():
    arr_suum = []
    for pay in Payments.objects.all():
        if datetime.datetime.now().month == pay.date.month:
            arr_suum.append(pay.summa)
    summa = sum(arr_suum)

    return point_in_number(summa), sum(arr_suum)


def spend_vsego(r):
    arr_suum = []
    for pay in r.objects.all():
        if datetime.datetime.now().month == pay.date.month:
            arr_suum.append(pay.summa)
    summa = sum(arr_suum)

    return point_in_number(summa), sum(arr_suum)


def spending_for_month(s):
    arr_spend = []
    for pay in s.objects.all():
        if datetime.datetime.now().month == pay.date.month:
            arr_spend.append(pay)
    return arr_spend


def dict_from_list_room(arrivals):
    new_people_room = {}
    while len(arrivals) > 0:
        com = arrivals[0]
        x = arrivals.count(com)
        new_people_room[com] = x
        if x > 0:
            while x > 0:
                arrivals.remove(com)
                x -= 1

    return new_people_room


def count_new_people():
    summ = 0

    arrivals = []  # заезды
    for profile in Profile.objects.all():
        if profile.date.month == datetime.datetime.now().month:
            if profile.room:
                arrivals.append(profile.room.number)

    for people in Profile.objects.all():
        if datetime.datetime.now().month == people.date.month:
            summ += 1

    return summ, dict_from_list_room(arrivals)


def arrivals_departures():
    summ = 0

    arrivals = []  # выезды
    for profile in Departures.objects.all():
        if profile.date.month == datetime.datetime.now().month:
            arrivals.append(profile.room)

    for people in Departures.objects.all():
        if datetime.datetime.now().month == people.date.month:
            summ += 1

    return summ, dict_from_list_room(arrivals)


def addRefaunds(request):
    data = data_d(request)

    form6 = AddRefundsForms(data=request.POST)
    data['form6'] = form6
    if form6.is_valid():
        if form6.cleaned_data['summa'] > 0:
            pay = Payments(
                user=form6.cleaned_data['user'],
                method=form6.cleaned_data['method'],
                name=form6.cleaned_data['user'].name,
                summa=form6.cleaned_data['summa'] * (-1),
                room=form6.cleaned_data['user'].room.number
            )
            pay.save()

            refa = Refunds(
                user=form6.cleaned_data['user'],
                method=form6.cleaned_data['method'],
                name=form6.cleaned_data['user'].name,
                summa=form6.cleaned_data['summa'] * (-1),
                room=form6.cleaned_data['user'].room.number
            )
            refa.save()
        else:
            pay = Payments(
                user=form6.cleaned_data['user'],
                method=form6.cleaned_data['method'],
                name=form6.cleaned_data['user'].name,
                summa=form6.cleaned_data['summa'],
                room=form6.cleaned_data['user'].room.number
            )
            pay.save()

            refa = Refunds(
                user=form6.cleaned_data['user'],
                method=form6.cleaned_data['method'],
                name=form6.cleaned_data['user'].name,
                summa=form6.cleaned_data['summa'],
                room=form6.cleaned_data['user'].room.number
            )
            refa.save()


def addPayments(request):
    data = data_d(request)
    form1 = AddPaymentsForm(data=request.POST)
    data['form1'] = form1
    if form1.is_valid():
        form1 = Payments(
            user=form1.cleaned_data['user'],
            method=form1.cleaned_data['method'],
            name=form1.cleaned_data['user'].name,
            summa=form1.cleaned_data['summa'],
            room=form1.cleaned_data['user'].room.number

        )
        form1.save()




