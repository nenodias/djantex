from django.conf.urls import include, url
from django.contrib import admin
import nucleo.urls as urls_nucleo
from rest_framework.authtoken.views import obtain_auth_token
from rest_api.urls import router as rest_route

urlpatterns = [
    urls_nucleo.urlpatterns[0],
    url(r'^api/token/', obtain_auth_token, name='api-token'),
    url(r'^api/', include(rest_route.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^nucleo/', include(urls_nucleo.urlpatterns)),
]
