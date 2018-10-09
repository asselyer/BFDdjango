from django.conf.urls import url
from .views import post_list, post_det, post_create, form_o, home

urlpatterns = [
    url(r'^$', view=post_list, name='post_list'),
    url(r'^det/(?P<pk>[0-9]+)$', view=post_det, name='post_det'),
    url(r'^create/$', view=post_create, name='post_create'),
    url(r'^form/$', view=form_o),
    url(r'^home/$', view=home)
]