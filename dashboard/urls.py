from django.urls import path
from .views import admin_dashboard
from .views import admin_dashboard, lead_list, schedule_call

urlpatterns = [
    path('', admin_dashboard, name='admin_dashboard'),
    path('dashboard/', admin_dashboard, name='admin_dashboard_alt'),
    path('leads/', lead_list, name='lead_list'),
    path('schedule/<int:lead_id>/', schedule_call, name='schedule_call'),
]