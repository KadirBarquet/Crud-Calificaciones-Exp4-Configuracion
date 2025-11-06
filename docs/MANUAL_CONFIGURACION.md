# Manual de Configuración - Línea de Productos Sistema Académico

## 1. Introducción

Este manual describe cómo configurar y gestionar las diferentes variantes del Sistema Académico basado en Django. El sistema implementa una arquitectura de Línea de Productos de Software (SPL) que permite activar o desactivar características según las necesidades.

## 2. Requisitos Previos

- Python 3.8 o superior
- Django 5.2.8
- Dependencias especificadas en `requirements.txt`

## 3. Instalación Base
```bash
# Clonar el repositorio
git clone <url-repositorio>

# Crear entorno virtual
python -m venv venv

# Activar entorno virtual
# En Windows:
venv\Scripts\activate
# En Linux/Mac:
source venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar migraciones
python manage.py migrate

# Crear superusuario
python manage.py createsuperuser

# Iniciar servidor
python manage.py runserver
```

## 4. Configuración de Variantes

### 4.1 Archivo de Configuración Principal

El archivo `core/config_product.py` contiene la configuración de todas las variantes disponibles.

**Estructura:**
```python
PRODUCT_A = {
    'name': 'Sistema Académico Básico',
    'version': '1.0',
    'ENABLE_REPORTS': False,
    'ENABLE_NOTIFICATIONS': False,
    'ENABLE_ADVANCED_SEARCH': False,
    'ENABLE_STATISTICS': False,
}

PRODUCT_B = {
    'name': 'Sistema Académico Completo',
    'version': '2.0',
    'ENABLE_REPORTS': True,
    'ENABLE_NOTIFICATIONS': True,
    'ENABLE_ADVANCED_SEARCH': True,
    'ENABLE_STATISTICS': True,
}

ACTIVE_PRODUCT = 'B'  # Cambiar entre 'A' o 'B'
```

### 4.2 Cambiar entre Variantes

Para cambiar la variante activa:

1. Abrir `core/config_product.py`
2. Modificar la variable `ACTIVE_PRODUCT`:
   - `ACTIVE_PRODUCT = 'A'` para Sistema Básico
   - `ACTIVE_PRODUCT = 'B'` para Sistema Completo
3. Reiniciar el servidor Django

**⚠️ IMPORTANTE:** Siempre reiniciar el servidor después de cambiar la configuración.

## 5. Activar/Desactivar Características Individuales

### 5.1 Sistema de Reportes (ENABLE_REPORTS)

**Cuando está activado:**
- Aparece el enlace "📊 Reportes" en el menú de navegación
- Se puede acceder a `/reports/export-grades/`
- Permite exportar datos académicos

**Para activar:**
```python
'ENABLE_REPORTS': True
```

**Para desactivar:**
```python
'ENABLE_REPORTS': False
```

### 5.2 Centro de Notificaciones (ENABLE_NOTIFICATIONS)

**Cuando está activado:**
- Aparece el enlace "🔔 Notificaciones" en el menú
- Se puede acceder a `/notifications/`
- Muestra alertas y eventos académicos

**Para activar:**
```python
'ENABLE_NOTIFICATIONS': True
```

**Para desactivar:**
```python
'ENABLE_NOTIFICATIONS': False
```

### 5.3 Búsqueda Avanzada (ENABLE_ADVANCED_SEARCH)

**Cuando está activado:**
- Filtros adicionales en las páginas de listado
- Búsqueda por múltiples criterios

**Para activar:**
```python
'ENABLE_ADVANCED_SEARCH': True
```

### 5.4 Panel de Estadísticas (ENABLE_STATISTICS)

**Cuando está activado:**
- Gráficos de rendimiento académico
- Indicadores y métricas

**Para activar:**
```python
'ENABLE_STATISTICS': True
```

## 6. Crear una Nueva Variante Personalizada

Para crear una nueva variante (por ejemplo, PRODUCT_C):

1. Abrir `core/config_product.py`

2. Agregar la nueva configuración:
```python
PRODUCT_C = {
    'name': 'Sistema Académico Premium',
    'version': '3.0',
    'ENABLE_REPORTS': True,
    'ENABLE_NOTIFICATIONS': True,
    'ENABLE_ADVANCED_SEARCH': True,
    'ENABLE_STATISTICS': True,
    'ENABLE_MOBILE_APP': True,  # Nueva característica
}
```

3. Modificar la función `get_active_config()`:
```python
def get_active_config():
    if ACTIVE_PRODUCT == 'A':
        return PRODUCT_A
    elif ACTIVE_PRODUCT == 'B':
        return PRODUCT_B
    elif ACTIVE_PRODUCT == 'C':
        return PRODUCT_C
    else:
        return PRODUCT_A
```

4. Activar la nueva variante:
```python
ACTIVE_PRODUCT = 'C'
```

## 7. Estructura de Apps Modulares

El sistema está organizado en apps Django independientes:
```
proyecto/
├── core/                 # Configuración principal
├── notas/               # App base (obligatoria)
├── reports/             # App de reportes (opcional)
├── notifications/       # App de notificaciones (opcional)
└── docs/                # Documentación
```

### 7.1 Apps Obligatorias
- **core**: Configuración del proyecto
- **notas**: Gestión académica base (estudiantes, facultades, carreras, etc.)

### 7.2 Apps Opcionales
- **reports**: Sistema de exportación y reportes
- **notifications**: Centro de notificaciones

## 8. Recomendaciones para Reutilización

### 8.1 Reutilizar una App en Otro Proyecto Django

Para reutilizar una app (por ejemplo, `reports`) en otro proyecto:

1. Copiar la carpeta completa de la app:
```bash
cp -r reports/ /ruta/otro-proyecto/
```

2. Agregar la app en `INSTALLED_APPS` del nuevo proyecto:
```python
INSTALLED_APPS = [
    # ...
    'reports',
]
```

3. Incluir las URLs:
```python
urlpatterns = [
    # ...
    path('reports/', include('reports.urls')),
]
```

4. Verificar dependencias en `requirements.txt`

### 8.2 Patrón de Reutilización Usado

**Patrón: Feature Toggle (Feature Flags)**

Este patrón permite:
- ✅ Activar/desactivar funcionalidades sin modificar código
- ✅ Mantener una única base de código para múltiples variantes
- ✅ Desplegar diferentes configuraciones según el cliente
- ✅ Realizar pruebas A/B de funcionalidades

## 9. Solución de Problemas

### 9.1 La característica no se activa/desactiva

**Solución:** Reiniciar el servidor Django después de cambiar `config_product.py`

### 9.2 Error al acceder a una característica desactivada

**Comportamiento esperado:** El sistema debe mostrar un mensaje de "Funcionalidad no disponible"

### 9.3 Enlaces aparecen aunque la característica esté desactivada

**Solución:** Verificar que el context processor esté configurado correctamente en `settings.py`

## 10. Mantenimiento

### 10.1 Agregar Nueva Característica

1. Crear nueva app Django
2. Agregar bandera en `config_product.py`
3. Configurar en `settings.py`
4. Incluir URLs condicionalmente
5. Actualizar plantillas con `{% if ENABLE_FEATURE %}`

### 10.2 Actualizar Documentación

Al agregar nuevas características, actualizar:
- `docs/feature_model.md`
- `docs/MANUAL_CONFIGURACION.md`
- Tabla de variantes en la documentación

## 11. Contacto y Soporte

Para soporte o consultas sobre la configuración del sistema, contactar al equipo de desarrollo.
```

## Paso 3: Crear diagrama SPL visual

Crea el archivo `docs/diagrama_spl.txt` (diagrama en texto):
```
┌─────────────────────────────────────────────────────────────┐
│          LÍNEA DE PRODUCTOS - SISTEMA ACADÉMICO             │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│                    CARACTERÍSTICAS CORE                      │
│                      (Obligatorias)                          │
├─────────────────────────────────────────────────────────────┤
│  • Autenticación y Autorización                             │
│  • Gestión de Estudiantes                                   │
│  • Gestión de Facultades                                    │
│  • Gestión de Carreras                                      │
│  • Gestión de Asignaturas                                   │
│  • Gestión de Profesores                                    │
│  • Gestión de Semestres                                     │
│  • Gestión de Notas                                         │
└─────────────────────────────────────────────────────────────┘
                              │
                              │
                  ┌───────────┴──────────┐
                  │                      │
         ┌────────▼────────┐    ┌───────▼────────┐
         │   VARIANTE A    │    │   VARIANTE B   │
         │     (Básico)    │    │   (Completo)   │
         └─────────────────┘    └────────────────┘
                  │                      │
    ┌─────────────┤                      ├──────────────┐
    │             │                      │              │
    ▼             ▼                      ▼              ▼
┌────────┐  ┌──────────┐         ┌──────────┐   ┌──────────┐
│ Core   │  │ Features │         │   Core   │   │ Features │
│        │  │          │         │          │   │          │
│ ✅ Sí  │  │ ❌ No    │         │  ✅ Sí   │   │ ✅ Sí    │
└────────┘  └──────────┘         └──────────┘   └──────────┘

┌─────────────────────────────────────────────────────────────┐
│              CARACTERÍSTICAS OPCIONALES                      │
│                    (Variables)                               │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  ┌──────────────────┐  ┌────────────────────┐              │
│  │ Sistema Reportes │  │  Notificaciones    │              │
│  │  (ENABLE_REPORTS)│  │(ENABLE_NOTIFICATIONS)             │
│  │                  │  │                    │              │
│  │  A: ❌  B: ✅    │  │   A: ❌  B: ✅     │              │
│  └──────────────────┘  └────────────────────┘              │
│                                                              │
│  ┌──────────────────┐  ┌────────────────────┐              │
│  │Búsqueda Avanzada │  │   Estadísticas     │              │
│  │(ENABLE_ADVANCED_ │  │ (ENABLE_STATISTICS)│              │
│  │     SEARCH)      │  │                    │              │
│  │  A: ❌  B: ✅    │  │   A: ❌  B: ✅     │              │
│  └──────────────────┘  └────────────────────┘              │
└─────────────────────────────────────────────────────────────┘

LEYENDA:
✅ = Característica incluida
❌ = Característica no incluida
A = Variante A (Sistema Básico v1.0)
B = Variante B (Sistema Completo v2.0)