from datetime import date
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView as Login
from django.http import Http404
from django.urls import reverse_lazy
from django.views import View
import account.validation
from django.contrib.auth import login
from django.shortcuts import redirect, render

from habit.models import HabitLog, Habit


class RegisterView(View):
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('dashboard')
    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        repass = request.POST.get('repass')
        validation = account.validation.validate_data(password, repass)
        if validation:
            user = User.objects.create_user(username=username, email=email, password=password)
            login(request, user)
            return redirect('dashboard')
        else:
            return Http404
class LoginView(Login):
    template_name = 'accounts/login.html'
    redirect_authenticated_user = True
    success_url = reverse_lazy('dashboard')

class DashboardView(LoginRequiredMixin, View):
    template_name = 'accounts/dashboard.html'
    def get(self, request):
        completed_today = HabitLog.get_completed_today(request.user)
        completion_rate = HabitLog.get_completion_rate(completed_today, request.user)
        habits = Habit.objects.filter(user=request.user)
        return render(request, self.template_name, {
            'user' : request.user, 'completed_today' : completed_today,
            'completion_rate' : completion_rate, 'habits' : habits,
        })


