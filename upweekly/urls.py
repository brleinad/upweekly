from django.urls import path

from .views import DashboardView, StartView

urlpatterns = [
        #path(r'^(?P<year>\d{4})/week/(?P<week>\d+)$', DashboardView.as_view(), name='dashboard'),
        path('<int:year>/week/<int:week>/', DashboardView.as_view(), name="dashboard"),
        path('', StartView.as_view(), name='start'),
        ]
