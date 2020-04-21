from django.views.generic import (
        ListView, 
        TemplateView, 
        WeekArchiveView,
        )
from django.views.generic.edit import FormMixin, CreateView
from django.views.generic.dates import WeekMixin
from django.utils import timezone
from django.urls import reverse_lazy

from datetime import datetime
from .models import CompletedTask



class WeekView(CreateView, WeekMixin, ListView):
    template_name = 'week.html'
    week_format = "%W"
    date_field = "date"
    template_name_suffix = ''
    queryset = CompletedTask.objects.all()
    ordering = ['date']
    fields = ('date', 'detail', 'highlight',)

    #def form_valid(self, form):
        #form.instance.date = self.request.date
        #return super().form_valid(form)

    def get_context_data(self, **kwargs):
        week = self.get_week()
        week = str(week)
        context = super(WeekView, self).get_context_data(**kwargs)
        context.update({'week': week})
        worked_yearweeks = CompletedTask.get_all_weeks()
        context.update({'worked_yearweeks': worked_yearweeks})
        return context


class CurrentWeekView(WeekView):
    week = str(timezone.now().isocalendar()[1])
    year = timezone.now().isocalendar()[0]
    success_url = reverse_lazy('current_week')


class ReportView(ListView):
    """To see all the highlighted tasks during the year"""
    model = CompletedTask
    template_name = 'report.html'
    ordering = ['date']
