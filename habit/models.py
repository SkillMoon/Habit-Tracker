import datetime
from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Habit(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='habits',
        verbose_name=_('user'),
    )
    name = models.CharField(max_length=100, verbose_name=_('name'))
    description = models.TextField(verbose_name=_('description'), blank=True)
    is_active = models.BooleanField(verbose_name=_('is active'), default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



    @property
    def current_streak(self):
        today = datetime.date.today()
        log_dates = set(
            self.logs.values_list('date', flat=True)
        )
        current_day = today
        streak = 0
        if current_day not in log_dates:
            current_day -= datetime.timedelta(days=1)
        while current_day in log_dates:
            streak += 1
            current_day -= datetime.timedelta(days=1)
        return streak

    class Meta:
        verbose_name = _('habit')
        verbose_name_plural = _('habits')

    def __str__(self):
        return f'{self.name} => {self.user.username}'

class HabitLog(models.Model):
    habit = models.ForeignKey(
        Habit, on_delete=models.CASCADE,
        related_name='logs',
        verbose_name=_('habit'),
    )
    date = models.DateField(verbose_name=_('date'))

    @classmethod
    def get_completed_today(cls, user):
        today = datetime.date.today()
        habit_logs = HabitLog.objects.select_related('habit').filter(habit__user=user, date=today)
        completed_today = habit_logs.count()
        return completed_today

    @classmethod
    def get_completion_rate(cls, completed_today, user):
        habits = Habit.objects.filter(user=user).count()
        success_rate = completed_today / habits * 100
        return int(success_rate)

    class Meta:
        verbose_name = _('habit log')
        verbose_name_plural = _('habit logs')
        constraints = [models.UniqueConstraint(fields=['habit', 'date'], name='unique_habit_date')]

    def __str__(self):
        return f'{self.habit} - {self.date}'