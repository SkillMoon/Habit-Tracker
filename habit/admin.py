from django.contrib import admin
from django.contrib.admin import register
from habit.models import Habit, HabitLog

@register(Habit)
class HabitAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'description', 'is_active', 'created_at', 'updated_at')
    list_filter = ('is_active', 'created_at', 'updated_at')
    search_fields = ('name', )
    ordering = ('-created_at',)

@register(HabitLog)
class HabitLog(admin.ModelAdmin):
    list_display = ('habit', 'date')
    list_filter = ('habit', 'date')
    search_fields = ('habit', )
    ordering = ('-date',)
