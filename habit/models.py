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

    class Meta:
        verbose_name = _('habit log')
        verbose_name_plural = _('habit logs')
        constraints = [models.UniqueConstraint(fields=['habit', 'date'], name='unique_habit_date')]

    def __str__(self):
        return f'{self.habit} - {self.date}'