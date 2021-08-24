from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import RedirectView
from django.urls import re_path
from django.views.static import serve

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('flmate.urls')),
    url(r'^$', RedirectView.as_view(url='index/', permanent=False), name='index'),
]
if settings.DEBUG:
    urlpatterns += [
        re_path(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)