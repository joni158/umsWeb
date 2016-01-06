from django.conf.urls import url, include
from . import views

urlpatterns = [
  # url(r'^$', views.home, name='home'),
  url(r'^$', views.home, name='home'),
  url(r'^berita/(?P<id_berita>\d+)/$', views.berita, name='berita'),

]