# *-* coding:utf-8 *-*
from datetime import date
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _
from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Usuario

class UsuarioSerializer(serializers.ModelSerializer):
    links = serializers.SerializerMethodField()
    class Meta:
        model = Usuario
        fields = ('id', 'nome', 'email', 'senha' ,'links',)

    def get_links(self, obj):
        request = self.context['request']
        return {
			#'self':reverse('sprint-detail', kwargs={'pk':obj.pk}, request=request),
			#'tasks':reverse('task-list', request=request) + '?sprint={}'.format(obj.pk),
		}
