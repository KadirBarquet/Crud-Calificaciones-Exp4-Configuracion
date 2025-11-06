# Checklist de Implementación - Línea de Productos

## ✅ Sesión 2: Modularización y separación de variantes

- [ ] Se creó la app `reports` separada de la app principal
- [ ] Se implementó la bandera `ENABLE_REPORTS` en settings.py
- [ ] Se crearon vistas condicionales en `reports/views.py`
- [ ] Se crearon plantillas para la funcionalidad de reportes
- [ ] Se configuró el context_processor para exponer banderas
- [ ] Se probó activar y desactivar la funcionalidad
- [ ] Se tomaron capturas con funcionalidad activada
- [ ] Se tomaron capturas con funcionalidad desactivada
- [ ] La funcionalidad se muestra/oculta correctamente en el menú

**Producto entregado:**
- ✅ App separada para funcionalidad opcional
- ✅ Capturas de vista con/sin la funcionalidad activada

---

## ✅ Sesión 3: Configuración de variabilidad

- [ ] Se creó el archivo `core/config_product.py`
- [ ] Se definieron las variantes PRODUCT_A y PRODUCT_B
- [ ] Se implementó la función `get_active_config()`
- [ ] Se modificó `settings.py` para usar configuración de productos
- [ ] Se creó la app `notifications`
- [ ] Se implementaron vistas para notificaciones
- [ ] Se configuraron URLs condicionales en `core/urls.py`
- [ ] Se actualizó `base.html` para mostrar nombre de variante
- [ ] Se actualizó la página de inicio para mostrar características
- [ ] Se probó Variante A (todas las características desactivadas)
- [ ] Se probó Variante B (todas las características activadas)
- [ ] Se tomaron capturas de ambas variantes

**Producto entregado:**
- ✅ Dos capturas distintas del mismo sistema con variabilidad funcional
- ✅ Explicación técnica de cómo se gestionan variantes
- ✅ Tabla de variantes y configuración

---

## ✅ Sesión 4: Documentación y línea de productos

- [ ] Se creó la carpeta `docs/`
- [ ] Se creó `docs/feature_model.md`
- [ ] Se creó `docs/MANUAL_CONFIGURACION.md`
- [ ] Se creó `docs/diagrama_spl.txt`
- [ ] Se creó `docs/tabla_variantes.md`
- [ ] Se creó `README.md` en la raíz del proyecto
- [ ] Se creó `docs/ejemplo_configuracion.py`
- [ ] Se documentó el patrón de reutilización usado (Feature Flags)
- [ ] Se documentaron instrucciones para activar/desactivar características
- [ ] Se documentaron recomendaciones para reutilizar apps
- [ ] Se creó diagrama SPL visual o en texto
- [ ] Se creó tabla comparativa de variantes
- [ ] Se tomaron capturas finales de ambas variantes
- [ ] Se tomó captura de la estructura del proyecto
- [ ] Se tomó captura del archivo de configuración

**Producto entregado:**
- ✅ Manual PDF: "Línea de productos basada en Django"
- ✅ Diagrama de variabilidad
- ✅ Capturas de interfaz por variante

---

## 📊 Resumen de Entregables

### Documentación en Word debe incluir:

#### Sesión 2:
1. Código de `reports/views.py`
2. Código de configuración en `settings.py`
3. Capturas con funcionalidad activada/desactivada
4. Explicación técnica breve

#### Sesión 3:
1. Código completo de `config_product.py`
2. Capturas de Variante A (4 capturas mínimo)
3. Capturas de Variante B (4 capturas mínimo)
4. Tabla comparativa de variantes
5. Explicación técnica de gestión de variantes

#### Sesión 4:
1. Manual de configuración (puede ser PDF o texto en Word)
2. Instrucciones para activar/desactivar características
3. Recomendaciones para reutilización de apps
4. Diagrama SPL (visual o texto)
5. Tabla de variantes y configuración
6. Capturas finales del sistema completo
7. Diagrama de variabilidad (árbol de decisiones o modelo de características)

---

## 🎯 Criterios de Evaluación

- [ ] El sistema tiene al menos 2 variantes claramente diferenciadas
- [ ] Las funcionalidades se pueden activar/desactivar mediante configuración
- [ ] No hay código duplicado entre variantes
- [ ] Las apps son modulares y reutilizables
- [ ] La documentación es clara y completa
- [ ] Las capturas de pantalla muestran las diferencias entre variantes
- [ ] El patrón de reutilización está claramente documentado
- [ ] El diagrama SPL muestra la estructura de la línea de productos