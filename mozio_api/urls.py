from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^json_rest_api/', include('json_rest_api.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^docs/', include('rest_framework_swagger.urls')),
]