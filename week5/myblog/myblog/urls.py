from django.contrib import admin
from django.conf.urls import url, include
from posts.views import index
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^posts/', include(('posts.urls','posts'), namespace='posts')),
    url(r'^$', view=index)
]\
              #+static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
