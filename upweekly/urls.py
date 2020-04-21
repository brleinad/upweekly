from django.urls import path

from .views import (
        CurrentWeekView, 
        WeekView, 
        ReportView, 
        StartView,
        DeleteTaskView,
        )

urlpatterns = [
        path('report/', ReportView.as_view(), name='report'),
        path('<int:year>/week/<int:week>/', WeekView.as_view(), name="week"),
        path('current_week/', CurrentWeekView.as_view(), name='current_week'),
        path('delete/<int:pk>', DeleteTaskView.as_view(), name='delete_task'),
        path('', StartView.as_view(), name='start'),
        ]
