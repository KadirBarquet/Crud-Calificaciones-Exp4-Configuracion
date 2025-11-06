from django.urls import path
from . import views

urlpatterns = [
    path('export-grades/', views.export_grades_report, name='export_grades'),
]