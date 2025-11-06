"""
Configuración de variantes de productos
Define las características disponibles en cada variante del sistema
"""

# Variante A: Sistema básico
PRODUCT_A = {
    'name': 'Sistema Académico Básico',
    'version': '1.0',
    'ENABLE_REPORTS': False,
    'ENABLE_NOTIFICATIONS': False,
    'ENABLE_ADVANCED_SEARCH': False,
    'ENABLE_STATISTICS': False,
}

# Variante B: Sistema completo
PRODUCT_B = {
    'name': 'Sistema Académico Completo',
    'version': '2.0',
    'ENABLE_REPORTS': True,
    'ENABLE_NOTIFICATIONS': True,
    'ENABLE_ADVANCED_SEARCH': True,
    'ENABLE_STATISTICS': True,
}

# Configuración activa (cambiar entre 'A' o 'B')
ACTIVE_PRODUCT = 'A'

# Obtener configuración activa
def get_active_config():
    """Retorna la configuración del producto activo"""
    if ACTIVE_PRODUCT == 'A':
        return PRODUCT_A
    elif ACTIVE_PRODUCT == 'B':
        return PRODUCT_B
    else:
        return PRODUCT_A  