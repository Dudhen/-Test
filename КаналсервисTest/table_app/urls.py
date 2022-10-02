from django.urls import path
from .views import TablePageView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path(r'canal_service/', TablePageView.as_view(), name='canal_service'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
