from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.postlist, name='post_list'),

]