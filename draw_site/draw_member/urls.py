from django.conf.urls import url
from .views import home, history, draw

urlpatterns = [
    url(r'^$', home, name="home"),
    url(r'^draw/$', draw, name="draw"),
    url(r'^history/$', history, name="history")
]
