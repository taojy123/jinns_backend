from django.conf.urls import url, include
from rest_framework import routers

from shops.views import oauth_jump, GenerateTokenView

router = routers.DefaultRouter()


urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^oauth/jump/$', oauth_jump),  # 这是一个重定向的 page 不是 api
    url(r'^oauth/token/$', GenerateTokenView.as_view(), name='generate_token'),
]
