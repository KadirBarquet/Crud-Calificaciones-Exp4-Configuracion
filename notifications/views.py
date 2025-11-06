from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.conf import settings

@login_required
def notifications_list(request):
    """Vista para mostrar notificaciones del usuario"""
    if not settings.ENABLE_NOTIFICATIONS:
        return render(request, 'feature_disabled.html', {
            'title': 'Funcionalidad no disponible',
            'message': 'El sistema de notificaciones está desactivado en esta versión'
        })
    
    # Simulación de notificaciones
    notifications = [
        {
            'id': 1,
            'type': 'info',
            'icon': '📢',
            'title': 'Nueva asignatura registrada',
            'message': 'Se ha agregado una nueva asignatura al sistema',
            'date': '2025-11-05',
        },
        {
            'id': 2,
            'type': 'success',
            'icon': '✅',
            'title': 'Notas actualizadas',
            'message': 'Las notas del semestre han sido actualizadas',
            'date': '2025-11-04',
        },
        {
            'id': 3,
            'type': 'warning',
            'icon': '⚠️',
            'title': 'Recordatorio',
            'message': 'Recuerde completar el registro de notas pendientes',
            'date': '2025-11-03',
        },
    ]
    
    context = {
        'title': 'Centro de Notificaciones',
        'notifications': notifications,
    }
    
    return render(request, 'notifications/list.html', context)