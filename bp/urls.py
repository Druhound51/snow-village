from django.conf.urls import include, url
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from bp.views import IndexView

urlpatterns = [
    # url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^admin_tools/', include('admin_tools.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^feedback/', include('app.dynamic_form.urls', namespace='feedback')),
    url(r'^order/', include('app.orders.urls', namespace='orders')),
    url(r'^store/', include('app.store.urls', namespace='store')),
    url(r'^cart/', include('app.cart.urls', namespace='cart')),
    url(r'^album/', include('app.album.urls', namespace='album')),
]
urlpatterns += [url(r'^', include('app.pages.urls', namespace='pages'))]
urlpatterns += staticfiles_urlpatterns()
if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
                      url(r'^__debug__/', include(debug_toolbar.urls)),
                  ] + urlpatterns
