# Sistema Académico - Línea de Productos de Software (SPL)

## 📋 Descripción

Sistema de gestión académica desarrollado con Django que implementa una arquitectura de Línea de Productos de Software (SPL), permitiendo activar o desactivar funcionalidades según las necesidades de cada institución educativa.

## 🎯 Características Principales

### Funcionalidades Base (Todas las variantes)
- ✅ Gestión de Usuarios (registro, autenticación, autorización)
- ✅ Gestión de Estudiantes
- ✅ Gestión de Facultades
- ✅ Gestión de Carreras
- ✅ Gestión de Asignaturas
- ✅ Gestión de Profesores
- ✅ Gestión de Semestres
- ✅ Gestión de Notas

### Funcionalidades Opcionales
- 📊 Sistema de Reportes (exportación a PDF/Excel)
- 🔔 Centro de Notificaciones
- 🔍 Búsqueda Avanzada
- 📈 Panel de Estadísticas

## 🚀 Variantes Disponibles

### Variante A - Sistema Académico Básico v1.0
Sistema ligero con funcionalidades esenciales para la gestión académica.

### Variante B - Sistema Académico Completo v2.0
Sistema completo con todas las funcionalidades avanzadas incluidas.

## 🛠️ Tecnologías Utilizadas

- **Backend:** Django 5.2.8
- **Frontend:** Bootstrap 5, HTML5, CSS3, JavaScript
- **Base de Datos:** SQLite (desarrollo) / PostgreSQL (producción)
- **Autenticación:** Django Authentication System
- **Forms:** Django Crispy Forms con Bootstrap 5

## 📦 Instalación

### Prerrequisitos
- Python 3.8 o superior
- pip
- virtualenv (recomendado)

### Pasos de Instalación

1. **Clonar el repositorio**
```bash
git clone <url-repositorio>
cd sistema-academico
```

2. **Crear entorno virtual**
```bash
python -m venv venv

# Activar en Windows
venv\Scripts\activate

# Activar en Linux/Mac
source venv/bin/activate
```

3. **Instalar dependencias**
```bash
pip install -r requirements.txt
```

4. **Configurar la variante deseada**
Editar `core/config_product.py`:
```python
ACTIVE_PRODUCT = 'A'  # o 'B'
```

5. **Ejecutar migraciones**
```bash
python manage.py migrate
```

6. **Crear superusuario**
```bash
python manage.py createsuperuser
```

7. **Iniciar el servidor**
```bash
python manage.py runserver
```

8. **Acceder al sistema**
```
http://localhost:8000
```

## ⚙️ Configuración de Variantes

Para cambiar entre variantes, editar el archivo `core/config_product.py`:
```python
# Para Sistema Básico
ACTIVE_PRODUCT = 'A'

# Para Sistema Completo
ACTIVE_PRODUCT = 'B'
```

**Importante:** Reiniciar el servidor después de cambiar la configuración.

## 📚 Documentación

- [Manual de Configuración](docs/MANUAL_CONFIGURACION.md)
- [Modelo de Características](docs/feature_model.md)
- [Tabla de Variantes](docs/tabla_variantes.md)
- [Diagrama SPL](docs/diagrama_spl.txt)

## 🏗️ Estructura del Proyecto
```
sistema-academico/
├── core/                      # Configuración del proyecto
│   ├── config_product.py      # Configuración de variantes
│   ├── context_processors.py  # Procesadores de contexto
│   └── settings.py            # Configuración Django
├── notas/                     # App principal (obligatoria)
├── reports/                   # App de reportes (opcional)
├── notifications/             # App de notificaciones (opcional)
├── static/                    # Archivos estáticos
├── media/                     # Archivos multimedia
├── docs/                      # Documentación
└── requirements.txt           # Dependencias
```

## 🔄 Patrón de Reutilización

El sistema implementa el patrón **Feature Toggle (Feature Flags)** que permite:

- ✅ Activar/desactivar funcionalidades sin modificar código
- ✅ Mantener una única base de código
- ✅ Desplegar diferentes configuraciones
- ✅ Apps modulares reutilizables

### Reutilizar Apps en Otros Proyectos

Las apps `reports` y `notifications` son completamente independientes y pueden ser reutilizadas en otros proyectos Django:
```bash
# Copiar app a otro proyecto
cp -r reports/ /ruta/otro-proyecto/

# Agregar en INSTALLED_APPS
'reports',

# Incluir URLs
path('reports/', include('reports.urls')),
```

## 👥 Equipo de Desarrollo

- **Desarrolladores:** [Tu Nombre]
- **Institución:** Universidad Estatal de Milagro (UNEMI)
- **Asignatura:** Gestión de la Configuración de Software

## 📄 Licencia

Este proyecto fue desarrollado con fines académicos para la materia de Gestión de la Configuración de Software.

## 📞 Soporte

Para consultas o soporte, contactar a través de [tu email o medio de contacto].
```

## Paso 6: Tomar capturas de pantalla finales

Ahora toma las siguientes capturas:

### Para Variante A (Sistema Básico):
1. **Página de inicio** mostrando las características desactivadas
2. **Menú de navegación** sin las opciones avanzadas
3. **Estructura de carpetas del proyecto**

### Para Variante B (Sistema Completo):
1. **Página de inicio** mostrando todas las características activas
2. **Menú de navegación** con todas las opciones
3. **Página de Reportes** funcionando
4. **Página de Notificaciones** funcionando

### Adicionales:
1. **Captura del archivo `config_product.py`**
2. **Captura de la estructura de carpetas completa**

---

## PRODUCTO PARA TU DOCUMENTACIÓN EN WORD (Sesión 4)

Para la **Sesión 4**, incluye en tu documento de Word:

### **Manual PDF: "Línea de productos basada en Django"**

Crea un documento PDF con las siguientes secciones:

#### 1. Portada
- Título: "Línea de Productos de Software - Sistema Académico"
- Subtítulo: "Manual de Configuración y Gestión de Variantes"
- Tu nombre y datos
- Fecha

#### 2. Contenido del Manual
Incluye el contenido de estos archivos que creamos:
- Introducción al proyecto (del README.md)
- Manual de configuración (de MANUAL_CONFIGURACION.md)
- Instrucciones para activar/desactivar características

#### 3. Instrucciones para activar/desactivar características
```
INSTRUCCIONES PARA GESTIÓN DE CARACTERÍSTICAS

1. Cambiar entre variantes completas:
   - Abrir archivo: core/config_product.py
   - Modificar línea: ACTIVE_PRODUCT = 'A' o 'B'
   - Reiniciar servidor Django

2. Activar/desactivar característica individual:
   - Editar el diccionario de la variante deseada
   - Cambiar el valor booleano de la característica
   - Ejemplo: 'ENABLE_REPORTS': True (activado) o False (desactivado)
   - Reiniciar servidor

3. Verificar cambios:
   - Recargar la página en el navegador
   - Verificar que el menú se actualice correctamente
   - Probar acceso a las funcionalidades
```

#### 4. Recomendaciones para reutilizar apps entre proyectos Django
```
GUÍA DE REUTILIZACIÓN DE APPS DJANGO

Paso 1: Identificar la app a reutilizar
- Las apps 'reports' y 'notifications' son modulares e independientes
- Cada app contiene: models, views, templates, urls

Paso 2: Copiar la app al nuevo proyecto
```bash
cp -r reports/ /ruta/nuevo-proyecto/
```

Paso 3: Registrar la app
En settings.py del nuevo proyecto:
```python
INSTALLED_APPS = [
    # ... otras apps
    'reports',
]
```

Paso 4: Incluir URLs
En urls.py del nuevo proyecto:
```python
from django.urls import path, include

urlpatterns = [
    # ... otras URLs
    path('reports/', include('reports.urls')),
]
```

Paso 5: Configurar banderas (opcional)
Si se desea control de activación:
- Agregar ENABLE_REPORTS en settings.py
- Crear context_processor para exponer la bandera
- Usar {% if ENABLE_REPORTS %} en templates

Paso 6: Verificar dependencias
- Revisar que todas las dependencias estén en requirements.txt
- Instalar con: pip install -r requirements.txt

Ventajas de este enfoque:
✅ Apps autocontenidas y reutilizables
✅ Sin dependencias fuertes entre apps
✅ Fácil mantenimiento
✅ Escalabilidad modular