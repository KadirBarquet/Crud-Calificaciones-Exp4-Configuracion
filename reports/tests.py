from django.test import TestCase, override_settings
from django.contrib.auth.models import User
from notas.models import Nota, Student, Facultad, Carrera, Asignatura, Profesor, Semestre
from datetime import date


class ReportsViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='reporter', password='secret')
        self.facultad = Facultad.objects.create(description='F')
        self.carrera = Carrera.objects.create(facultad=self.facultad, description='C')
        self.asignatura = Asignatura.objects.create(name='A')
        self.profesor = Profesor.objects.create(firstname='P', lastname='Q')
        self.semestre = Semestre.objects.create(description='S', dateBegin=date.today(), dateEnd=date.today())
        self.student = Student.objects.create(firstname='Stu', lastname='Dent', user=self.user)
        # crear una nota asociada al usuario
        self.nota = Nota.objects.create(
            facultad=self.facultad,
            carrera=self.carrera,
            asignatura=self.asignatura,
            student=self.student,
            profesor=self.profesor,
            semestre=self.semestre,
            nota1=1, nota2=2, notarecuperacion=3, user=self.user
        )

    def test_export_grades_view_enabled(self):
        self.client.force_login(self.user)
        # La URL incluida en `core.urls` es bajo el prefijo /reports/ y la ruta definida es export-grades/
        response = self.client.get('/reports/export-grades/')
        # Debería devolver 200 y contener el título del template
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Exportar Reporte de Notas')

    @override_settings(ENABLE_REPORTS=False)
    def test_export_grades_disabled(self):
        self.client.force_login(self.user)
        response = self.client.get('/reports/export-grades/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Funcionalidad no disponible')

