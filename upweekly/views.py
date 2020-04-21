from django.views.generic import (
        ListView, 
        TemplateView, 
        WeekArchiveView,
        )
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.edit import FormMixin, CreateView
from django.views.generic.dates import WeekMixin
from django.utils import timezone
from django.urls import reverse_lazy

from datetime import datetime
from .models import CompletedTask



class StartView(TemplateView):
    template_name = 'start.html'


class WeekView(LoginRequiredMixin, UserPassesTestMixin, CreateView, WeekMixin, ListView):
    template_name = 'week.html'
    week_format = "%W"
    date_field = "date"
    template_name_suffix = ''
    queryset = CompletedTask.objects.all()
    #model = CompletedTask
    ordering = ['date']
    fields = ('date', 'detail', 'highlight',)
    login_url = 'login'

    def test_func(self):
        #for task in self.queryset:
        #    if task.user != self.request.user:
        #        return False
        return True
        #obj = self.get_object()
        #return obj.user == self.request.user


    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        week = self.get_week()
        week = str(week)
        context = super(WeekView, self).get_context_data(**kwargs)
        context.update({'week': week})
        worked_yearweeks = CompletedTask.get_all_yearweeks(self.request)
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

