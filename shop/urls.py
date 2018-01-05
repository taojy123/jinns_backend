from django.conf.urls import url, include
from rest_framework import routers

from shop.views import GenerateTokenView

router = routers.DefaultRouter()


urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^oauth/token/$', GenerateTokenView.as_view(), name='generate_token'),
]
