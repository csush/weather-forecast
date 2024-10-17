from django.urls import path
from .api.v1.views import PlanHolidayView


urlpatterns = [path('v1/plan/', PlanHolidayView.as_view(), name='plan_holiday')]