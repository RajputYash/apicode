
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from warehouse import celery
from warehouse.webapp.tasks import mqtt_client


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include('warehouse.webapp.urls'))
]

mqtt_client.delay()