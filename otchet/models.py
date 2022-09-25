import datetime

from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User


class Room(models.Model):  # информация о комнате
    number = models.PositiveSmallIntegerField(default=0, verbose_name='Номер комнаты')  # номер комнаты// стройкой лучше
    price_for_period = models.IntegerField(default=7000, verbose_name='Стоимость')  # цена проживания
    number_of_beds = models.PositiveSmallIntegerField(default=1, verbose_name='Количество мест')  # количество мест

    @property
    def is_full(self):
        if self.profile.count() == self.number_of_beds:
            return True
        return False


    def __str__(self):
        if self.number:
            return f'Комната №{self.number}'
        else:
            return ''

    class Meta:
        db_table = "room"
        ordering = ['number']
        verbose_name = "Комната"
        verbose_name_plural = "Комнаты"

        # почитать класс META


class Profile(models.Model):
    date = models.DateTimeField(auto_now=True, verbose_name='Дата')
    name = models.CharField(default="", max_length=100, verbose_name="Имя")
    room = models.ForeignKey(
        Room,
        on_delete=models.SET_NULL,
        verbose_name='Комната',
        null=True,
        related_name="profile"
    )
    room_number = models.CharField(
        max_length=2,
        default="",
        verbose_name="Номер комнаты"
    )
    phone_number = models.CharField(
        default="79876543412",
        max_length=11,
        verbose_name="Номер телефона",
    )


    def __str__(self):
        return f'{self.room} {self.name} {self.phone_number}'


    class Meta:
        db_table = "profile"
        ordering = ['-room']
        verbose_name = "Постоялец"
        verbose_name_plural = "Постояльцы"


class Departures(models.Model):  # выселения
    date = models.DateTimeField(auto_now=True, verbose_name='Дата')
    user = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, verbose_name='Имя')
    name = models.CharField(default="", max_length=100, verbose_name="Имя")
    phone_number = models.CharField(
        default="79876543412",
        max_length=11,
        verbose_name="Номер телефона",
    )
    room = models.CharField(max_length=3, null=True, verbose_name='Номер комнаты')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        db_table = "departures"
        verbose_name = "Выезд"
        verbose_name_plural = "Выезды"


class PaymentsRefunds(models.Model):
    CHOICES = [
        ('card', 'Перевод на карту'),
        ('cash', 'Наличные'),
    ]
    date = models.DateTimeField(auto_now=True, verbose_name='Дата')
    user = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, verbose_name='Профиль')
    name = models.CharField(max_length=100, null=True, default="", verbose_name='Имя')
    method = models.CharField(
        max_length=50,
        choices=CHOICES,
        default='card',
        verbose_name='Способ оплаты'
    )
    summa = models.IntegerField(default=0, verbose_name='Сумма оплаты')
    room = models.CharField(max_length=3, null=True, verbose_name='Номер комнаты')

    def date_check(self):
        if self.date.month < 10:
            month_now = '0' + str(self.date.month)
        else:
            month_now = self.date.month
        return month_now

    class Meta:
        abstract = True


class Payments(PaymentsRefunds):  # платежи
    class Meta:
        db_table = "payments"
        verbose_name = "Платеж"
        verbose_name_plural = "Платежи"
        ordering = ['-date']


class Refunds(PaymentsRefunds):  # возвраты
    class Meta:
        db_table = "refunds"
        verbose_name = "Возврат"
        verbose_name_plural = "Возвраты"


class Spending(models.Model):
    date = models.DateTimeField(auto_now=True, verbose_name='Дата')
    summa = models.PositiveIntegerField(default=0, verbose_name='Сумма')
    note = models.CharField(max_length=200, verbose_name='Примечание')

    def date_check(self):
        if self.date.month < 10:
            month_now = '0' + str(self.date.month)
        else:
            month_now = self.date.month
        return month_now

    class Meta:
        abstract = True



class SpendingAdmin(Spending):  # траты админа
    class Meta:
        db_table = "adminspending"
        verbose_name = "Расходы админа"
        verbose_name_plural = "Расходы админа"
        ordering = ['-date']


class SpendingHostel(Spending):  # траты дома
    class Meta:
        db_table = "hostelspending"
        verbose_name = "Расходы дома"
        verbose_name_plural = "Расходы дома"
        ordering = ['-date']


class SpendingBoss(Spending):  # траты хозяина дома
    class Meta:
        db_table = "bossspending"
        verbose_name = "Расходы хозяина"
        verbose_name_plural = "Расходы хозяина"
        ordering = ['-date']


class Events(models.Model):
    date = models.DateField(auto_now=True, verbose_name='Дата')
    event = models.CharField(max_length=200, verbose_name='Мероприятие')

    class Meta:
        db_table = "events"
        verbose_name = "Мероприятие"
        verbose_name_plural = "Мероприятия"
        ordering = ['-date']


