"""
EJEMPLOS DE CONFIGURACIÓN PARA DIFERENTES ESCENARIOS
Copiar el bloque deseado en core/config_product.py
"""

# ==============================================================================
# ESCENARIO 1: Academia de idiomas pequeña
# Solo necesita gestión básica de estudiantes y notas
# ==============================================================================
ACADEMIA_IDIOMAS = {
    'name': 'Sistema Academia Idiomas',
    'version': '1.0',
    'ENABLE_REPORTS': False,
    'ENABLE_NOTIFICATIONS': False,
    'ENABLE_ADVANCED_SEARCH': False,
    'ENABLE_STATISTICS': False,
}

# ==============================================================================
# ESCENARIO 2: Instituto técnico mediano
# Necesita reportes pero no notificaciones
# ==============================================================================
INSTITUTO_TECNICO = {
    'name': 'Sistema Instituto Técnico',
    'version': '1.5',
    'ENABLE_REPORTS': True,
    'ENABLE_NOTIFICATIONS': False,
    'ENABLE_ADVANCED_SEARCH': True,
    'ENABLE_STATISTICS': False,
}

# ==============================================================================
# ESCENARIO 3: Universidad completa
# Requiere todas las funcionalidades
# ==============================================================================
UNIVERSIDAD_COMPLETA = {
    'name': 'Sistema Universitario Completo',
    'version': '2.0',
    'ENABLE_REPORTS': True,
    'ENABLE_NOTIFICATIONS': True,
    'ENABLE_ADVANCED_SEARCH': True,
    'ENABLE_STATISTICS': True,
}

# ==============================================================================
# ESCENARIO 4: Centro de capacitación corporativa
# Necesita reportes y estadísticas, pero no notificaciones
# ==============================================================================
CENTRO_CORPORATIVO = {
    'name': 'Sistema Capacitación Corporativa',
    'version': '1.8',
    'ENABLE_REPORTS': True,
    'ENABLE_NOTIFICATIONS': False,
    'ENABLE_ADVANCED_SEARCH': False,
    'ENABLE_STATISTICS': True,
}

# ==============================================================================
# INSTRUCCIONES DE USO:
# 
# 1. Identificar el escenario que más se ajuste a tu institución
# 2. Copiar el bloque de configuración correspondiente
# 3. Pegarlo en core/config_product.py como PRODUCT_A o PRODUCT_B
# 4. Ajustar el nombre según sea necesario
# 5. Activar con: ACTIVE_PRODUCT = 'A' (o 'B', 'C', etc.)
# 6. Reiniciar el servidor Django
# ==============================================================================