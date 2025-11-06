from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.conf import settings
from notas.models import Nota, Student

@login_required
def export_grades_report(request):
    """Vista para exportar reporte de notas"""
    if not settings.ENABLE_REPORTS:
        return render(request, 'feature_disabled.html', {
            'title': 'Funcionalidad no disponible',
            'message': 'La funcionalidad de reportes está desactivada'
        })
    
    # Obtener datos para el reporte
    notas = Nota.objects.filter(user=request.user)
    students = Student.objects.filter(user=request.user)
    
    context = {
        'title': 'Exportar Reporte de Notas',
        'notas': notas,
        'students': students,
    }
    
    return render(request, 'reports/export_grades.html', context)
