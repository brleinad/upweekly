from django.urls import path

from .views import CurrentWeekView, WeekView, ReportView

urlpatterns = [
        path('<int:year>/week/<int:week>/', WeekView.as_view(), name="week"),
        path('report/', ReportView.as_view(), name='report'),
        path('', CurrentWeekView.as_view(), name='current_week'),
        ]
