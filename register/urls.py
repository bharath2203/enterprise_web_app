from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index),
    path('kannada', views.success_kannada),
    path('hindi', views.success_hindi),
    path('register', views.register),
    path('login', views.login),
    path('success', views.success),
    path('getrelatedtext', views.get_related_text),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
