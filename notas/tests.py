from django.test import TestCase
from django.contrib.auth.models import User
from .models import Facultad, Carrera, Asignatura, Profesor, Semestre, Student, Nota
from datetime import date


class NotaModelTest(TestCase):
	def setUp(self):
		# usuario
		self.user = User.objects.create_user(username='tester', password='pass')

		# datos relacionados
		self.facultad = Facultad.objects.create(description='Facultad de Prueba')
		self.carrera = Carrera.objects.create(facultad=self.facultad, description='Ing. Prueba')
		self.asignatura = Asignatura.objects.create(name='Matemáticas')
		self.profesor = Profesor.objects.create(firstname='Juan', lastname='Perez')
		self.semestre = Semestre.objects.create(description='2025-1', dateBegin=date.today(), dateEnd=date.today())
		self.student = Student.objects.create(firstname='Ana', lastname='Lopez', user=self.user)

	def test_nota_promedio_y_str(self):
		nota = Nota.objects.create(
			facultad=self.facultad,
			carrera=self.carrera,
			asignatura=self.asignatura,
			student=self.student,
			profesor=self.profesor,
			semestre=self.semestre,
			nota1=4.5,
			nota2=3.5,
			notarecuperacion=2.0,
			user=self.user,
		)

		# El campo promedio se calcula en save(); recuperar instancia
		nota.refresh_from_db()
		expected = nota.nota1 + nota.nota2 + nota.notarecuperacion
		self.assertEqual(float(nota.promedio), float(expected))

		# __str__ contiene el estudiante y la asignatura
		s = str(nota)
		self.assertIn('Ana', s)
		self.assertIn('Matemáticas', s)

