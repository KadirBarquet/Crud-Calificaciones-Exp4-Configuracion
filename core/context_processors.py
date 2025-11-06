from django.conf import settings

def feature_flags(request):
    """Context processor para hacer disponibles las banderas de características"""
    return {
        'ENABLE_REPORTS': settings.ENABLE_REPORTS,
        'ENABLE_NOTIFICATIONS': settings.ENABLE_NOTIFICATIONS,
        'ENABLE_ADVANCED_SEARCH': settings.ENABLE_ADVANCED_SEARCH,
        'ENABLE_STATISTICS': settings.ENABLE_STATISTICS,
        'PRODUCT_NAME': settings.PRODUCT_CONFIG.get('name', 'Sistema Académico'),
        'PRODUCT_VERSION': settings.PRODUCT_CONFIG.get('version', '1.0'),
    }