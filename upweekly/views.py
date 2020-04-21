from django.views.generic import ListView, TemplateView, WeekArchiveView
from django.views.generic.dates import WeekMixin
from django.utils import timezone

from datetime import datetime
from .models import CompletedTask


class DashboardView(WeekArchiveView):
    template_view = 'dashboard.html'
    queryset = CompletedTask.objects.all()
    date_field = "date"
    week_format = "%W"


class StartView(WeekMixin, ListView):
    template_name = 'start.html'
    week_format = "%W"
    date_field = "date"
    template_name_suffix = ''
    queryset = CompletedTask.objects.all()
    ordering = ['date']
    week = str(timezone.now().isocalendar()[1])
    year = timezone.now().isocalendar()[0]

    def get_context_data(self, **kwargs):
        context = super(StartView, self).get_context_data(**kwargs)
        context.update({'week': self.week})
        return context

