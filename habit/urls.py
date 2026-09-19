from django.urls import path
from django.views.generic import TemplateView
from habit.views import *

urlpatterns = [
    path('list/', HabitListView.as_view(), name='habit-list'),
    path('detail/<int:pk>', HabitDetailView.as_view(), name='habit-detail'),
    path('create/', CreateHabitView.as_view(), name='create-habit'),
    path('update/<int:pk>', UpdateHabitView.as_view(), name='update-habit'),
    path('delete/<int:pk>', DeleteHabitView.as_view(template_name='habits/habit_confirm_delete.html'), name='delete-habit'),
]