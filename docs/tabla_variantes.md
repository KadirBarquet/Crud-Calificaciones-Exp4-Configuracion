# Tabla de Comparación de Variantes

## Matriz de Características por Variante

| ID | Característica | Tipo | Variante A (Básico) | Variante B (Completo) | Descripción |
|----|---------------|------|--------------------|-----------------------|-------------|
| **CORE-01** | Autenticación | Obligatoria | ✅ Incluida | ✅ Incluida | Sistema de login/logout de usuarios |
| **CORE-02** | Gestión Estudiantes | Obligatoria | ✅ Incluida | ✅ Incluida | CRUD completo de estudiantes |
| **CORE-03** | Gestión Facultades | Obligatoria | ✅ Incluida | ✅ Incluida | CRUD completo de facultades |
| **CORE-04** | Gestión Carreras | Obligatoria | ✅ Incluida | ✅ Incluida | CRUD completo de carreras |
| **CORE-05** | Gestión Asignaturas | Obligatoria | ✅ Incluida | ✅ Incluida | CRUD completo de asignaturas |
| **CORE-06** | Gestión Profesores | Obligatoria | ✅ Incluida | ✅ Incluida | CRUD completo de profesores |
| **CORE-07** | Gestión Semestres | Obligatoria | ✅ Incluida | ✅ Incluida | CRUD completo de semestres |
| **CORE-08** | Gestión Notas | Obligatoria | ✅ Incluida | ✅ Incluida | Registro y cálculo de calificaciones |
| **OPT-01** | Sistema de Reportes | Opcional | ❌ No incluida | ✅ Incluida | Exportación de datos a PDF/Excel |
| **OPT-02** | Centro Notificaciones | Opcional | ❌ No incluida | ✅ Incluida | Alertas y eventos del sistema |
| **OPT-03** | Búsqueda Avanzada | Opcional | ❌ No incluida | ✅ Incluida | Filtros y búsquedas complejas |
| **OPT-04** | Panel Estadísticas | Opcional | ❌ No incluida | ✅ Incluida | Gráficos e indicadores |

## Configuración Técnica por Variante

### Variante A - Sistema Académico Básico v1.0
```python
PRODUCT_A = {
    'name': 'Sistema Académico Básico',
    'version': '1.0',
    'ENABLE_REPORTS': False,
    'ENABLE_NOTIFICATIONS': False,
    'ENABLE_ADVANCED_SEARCH': False,
    'ENABLE_STATISTICS': False,
}
```

**Apps Django instaladas:**
- `core` (configuración)
- `notas` (funcionalidad base)

**URLs activas:**
- `/` (inicio)
- `/students/` (estudiantes)
- `/facultades/` (facultades)
- `/carreras/` (carreras)
- `/asignaturas/` (asignaturas)
- `/profesores/` (profesores)
- `/semestres/` (semestres)
- `/notas/` (notas)
- `/login/` `/logout/` `/register/` (autenticación)

### Variante B - Sistema Académico Completo v2.0
```python
PRODUCT_B = {
    'name': 'Sistema Académico Completo',
    'version': '2.0',
    'ENABLE_REPORTS': True,
    'ENABLE_NOTIFICATIONS': True,
    'ENABLE_ADVANCED_SEARCH': True,
    'ENABLE_STATISTICS': True,
}
```

**Apps Django instaladas:**
- `core` (configuración)
- `notas` (funcionalidad base)
- `reports` (sistema de reportes)
- `notifications` (centro de notificaciones)

**URLs activas:**
- Todas las URLs de Variante A
- `/reports/export-grades/` (exportar reportes)
- `/notifications/` (centro de notificaciones)

## Casos de Uso Recomendados

### Variante A - Sistema Básico
**Ideal para:**
- 🏫 Instituciones educativas pequeñas (< 500 estudiantes)
- 📚 Centros de capacitación
- 🎓 Academias con necesidades básicas
- 💰 Presupuestos limitados

**Ventajas:**
- Menor consumo de recursos
- Interfaz más simple
- Fácil de aprender
- Menor costo de mantenimiento

### Variante B - Sistema Completo
**Ideal para:**
- 🏛️ Universidades
- 🏢 Instituciones educativas medianas y grandes (> 500 estudiantes)
- 📊 Organizaciones que requieren reportes detallados
- 🔔 Instituciones que necesitan notificaciones automatizadas

**Ventajas:**
- Funcionalidad completa
- Reportes y análisis avanzados
- Sistema de notificaciones
- Escalable para crecimiento futuro

## Proceso de Migración Entre Variantes

### De Variante A a Variante B (Upgrade)

1. Modificar `core/config_product.py`:
```python
   ACTIVE_PRODUCT = 'B'
```

2. Reiniciar servidor Django

3. Verificar que las nuevas funcionalidades aparezcan en el menú

4. No se pierden datos existentes

### De Variante B a Variante A (Downgrade)

1. Modificar `core/config_product.py`:
```python
   ACTIVE_PRODUCT = 'A'
```

2. Reiniciar servidor Django

3. Las funcionalidades avanzadas quedan ocultas pero los datos se conservan

4. Se puede regresar a Variante B en cualquier momento

**⚠️ Nota:** Los datos creados en cualquier variante se conservan al cambiar de versión.