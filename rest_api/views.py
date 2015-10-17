# *-* coding:utf-8 *-*
from django.contrib.auth import get_user_model
from rest_framework import authentication, permissions, viewsets, filters
from .forms import UsuarioFilter
from .models import Usuario
from .serializers import UsuarioSerializer

class DefaultMixin(object):
	'''Configurações default para autenticação, permissões, filtragem e paginação da view '''
	authentication_classes = (
		authentication.BasicAuthentication,
		authentication.TokenAuthentication,
	)
	permission_classes = (
		permissions.IsAuthenticated,
	)

	paginated_by = 25
	paginated_by_param = 'page_size'
	max_paginate_by = 100

	filter_backends = (
		filters.DjangoFilterBackend,
		filters.SearchFilter,
		filters.OrderingFilter,
	)

class UsuarioViewSet(DefaultMixin, viewsets.ModelViewSet):
    '''Endpoint da API para listar e criar Usuários'''
    queryset = Usuario.objects.order_by('nome')
    serializer_class = UsuarioSerializer
    filter_class = UsuarioFilter
    search_fields = ('nome','email',)
    ordering_fields = ('nome', 'email',)
