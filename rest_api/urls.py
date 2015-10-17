# *-* coding:utf-8 *-*
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter(trailing_slash=False)
router.register(r'usuarios', views.UsuarioViewSet)
