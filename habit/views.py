import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from habit.models import Habit, HabitLog


class CreateHabitView(LoginRequiredMixin, View):
    template_name = 'habits/habit_form.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        description = request.POST.get('description')
        try:
            habit = Habit.objects.create(user=request.user, name=name, description=description)
            print(habit)
            return redirect('habit-list')
        except Exception as e:
            return HttpResponse(e)

class UpdateHabitView(LoginRequiredMixin, View):
    template_name = 'habits/habit_form.html'

    def get(self, request, pk):
        try:
            habit = Habit.objects.get(pk=pk)
            return render(request, self.template_name, {'habit': habit})
        except Habit.DoesNotExist:
            return HttpResponse('Habit not found')

    def post(self, request, pk):
        habit = get_object_or_404(Habit, pk=pk)

        name = request.POST.get('name')
        description = request.POST.get('description')
        is_active = request.POST.get('is_active')
        habit.name = name
        habit.description = description

        habit.is_active = True if is_active == 'on' else False
        habit.save()
        print(habit)
        return redirect('habit-list')

class DeleteHabitView(LoginRequiredMixin, View):
    template_name = 'habits/habit_confirm_delete.html'

    def get(self, request, pk):
        try:
            habit = Habit.objects.get(pk=pk)
            return render(request, self.template_name, {'habit': habit})
        except Habit.DoesNotExist:
            return HttpResponse('Habit not found')

    def post(self, request, pk):
        habit = get_object_or_404(Habit, pk=pk)
        habit.delete()
        return redirect('habit-list')

class HabitDetailView(LoginRequiredMixin, View):
    template_name = 'habits/habit_detail.html'

    def get(self, request, pk):
        habit = get_object_or_404(Habit, pk=pk)
        logs = HabitLog.objects.filter(habit=habit)
        return render(request, self.template_name, {'habit': habit, 'logs' : logs})

    def post(self, request, pk):
        habit = get_object_or_404(Habit, pk=pk)
        today = datetime.date.today()
        if HabitLog.check_exist(habit):
            habit_log = HabitLog.objects.create(habit=habit, date=today)
            return redirect('habit-detail', pk=pk)
        else:
            return HttpResponse('you\'ve already checked out this habit')

class HabitListView(LoginRequiredMixin, View):
    template_name = 'habits/habit_list.html'

    def get(self, request):
        habits = Habit.objects.filter(user=request.user)
        return render(request, self.template_name, {'habits': habits})
