from django.contrib import admin
from django.urls import path, include
from notas import views
from core import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    
    path('students/', views.student, name='students'),
    path('students/create/', views.create_student, name='create_student'),
    path('students/<int:id>/', views.detail_student, name='detail_student'),
    path('students/update/<int:id>/', views.update_student, name='update_student'),
    path('students/delete/<int:id>/', views.delete_student, name='delete_student'),

    path('facultades/', views.facultad, name='facultades'),
    path('facultades/create/', views.create_facultad, name='create_facultad'),
    path('facultades/<int:id>/', views.detail_facultad, name='detail_facultad'),
    path('facultades/update/<int:id>/', views.update_facultad, name='update_facultad'),
    path('facultades/delete/<int:id>/', views.delete_facultad, name='delete_facultad'),

    path('carreras/', views.carrera, name='carreras'),
    path('carreras/create/', views.create_carrera, name='create_carrera'),
    path('carreras/<int:id>/', views.detail_carrera, name='detail_carrera'),
    path('carreras/update/<int:id>/', views.update_carrera, name='update_carrera'),
    path('carreras/delete/<int:id>/', views.delete_carrera, name='delete_carrera'),

    path('asignaturas/', views.asignatura, name='asignaturas'),
    path('asignaturas/create/', views.create_asignatura, name='create_asignatura'),
    path('asignaturas/<int:id>/', views.detail_asignatura, name='detail_asignatura'),
    path('asignaturas/update/<int:id>/', views.update_asignatura, name='update_asignatura'),
    path('asignaturas/delete/<int:id>/', views.delete_asignatura, name='delete_asignatura'),

    path('profesores/', views.profesor, name='profesores'),
    path('profesores/create/', views.create_profesor, name='create_profesor'),
    path('profesores/<int:id>/', views.detail_profesor, name='detail_profesor'),
    path('profesores/update/<int:id>/', views.update_profesor, name='update_profesor'),
    path('profesores/delete/<int:id>/', views.delete_profesor, name='delete_profesor'),

    path('semestres/', views.semestre, name='semestres'),
    path('semestres/create/', views.create_semestre, name='create_semestre'),
    path('semestres/<int:id>/', views.detail_semestre, name='detail_semestre'),
    path('semestres/update/<int:id>/', views.update_semestre, name='update_semestre'),
    path('semestres/delete/<int:id>/', views.delete_semestre, name='delete_semestre'),

    path('notas/', views.nota, name='notas'),
    path('notas/create/', views.create_nota, name='create_nota'),
    path('notas/<int:id>/', views.detail_nota, name='detail_nota'),
    path('notas/update/<int:id>/', views.update_nota, name='update_nota'),
    path('notas/delete/<int:id>/', views.delete_nota, name='delete_nota'),

    path('register/', views.register, name='register'),
    path('login/', views.iniciarSesion, name='login'),
    path('logout/', views.cerrarSesion, name='logout'),
]

# URLs condicionales basadas en configuración de producto
if settings.ENABLE_REPORTS:
    urlpatterns += [
        path('reports/', include('reports.urls')),
    ]

if settings.ENABLE_NOTIFICATIONS:
    urlpatterns += [
        path('notifications/', include('notifications.urls')),
    ]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)