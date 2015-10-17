# *-* coding: utf-8 *-*
import django_filters
from django.contrib.auth import get_user_model
from .models import Usuario

class NullFilter(django_filters.BooleanFilter):
	'''Filtra de acordo com um campo definido como nulo ou nao'''

	def filter(self, qs, value):
		if value is not None:
			return qs.filter(**{'%s__isnull'% self.name: value})
		return qs

class UsuarioFilter(django_filters.FilterSet):
	nome = django_filters.CharFilter(name='nome')

	class Meta:
		model = Usuario
		fields = {
				'nome': ['exact', 'icontains'],
				'email': ['exact', 'icontains']
				}
