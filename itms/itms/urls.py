from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls import patterns, include


urlpatterns = [
    url(r'^itms/', include('itmsapp.urls')),

    url(r'^admin/', admin.site.urls),
]

admin.site.site_header = 'ITMS Admin'
admin.site.site_title = "ITMS Admin"
admin.site.index_title = "Dashboard"
admin.site.site_url = "/itms/"