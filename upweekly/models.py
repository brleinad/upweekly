from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.urls import reverse
from datetime import datetime


class CompletedTask(models.Model):
    date = models.DateField(default=timezone.now())
    #TODO: change detail to something else
    detail = models.CharField(max_length = 255)
    highlight =  models.BooleanField(default=False)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,)
    test = False

    def __str__(self):
        return self.detail

    def get_absolute_url(self):
        date_object = self._meta.get_field('date')
        date_value = date_object.value_from_object(self)
        week = date_object.to_python(date_value).isocalendar()[1]
        year = date_object.to_python(date_value).isocalendar()[0]
        return reverse('week', args=[str(year), str(week)])

    def get_all_yearweeks(request):
        """Returns a dictionary of all the weeks: years for which there is a task."""
        weeks2years = {}
        weeks = []
        years = []

        for task in CompletedTask.objects.all():
            if task.user == request.user:
                date_object = CompletedTask._meta.get_field('date')
                date_value = date_object.value_from_object(task)
                week = date_object.to_python(date_value).isocalendar()[1]
                year = date_object.to_python(date_value).isocalendar()[0]
                #print(f'BOB {task}, year {year} in week {week}')
                if week in weeks: 
                    next
                weeks.append(int(week))
                years.append(int(year))

        weeks2years = dict(zip(weeks, years))
        print(weeks2years)

        return weeks2years



#class PlannedTask(models.Model):
