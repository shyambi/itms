from django.conf.urls import url


from . import views
app_name = 'itmsapp'

urlpatterns = [
    url(r'^$', views.resources, name='resources'),
    url(r'^networktopology/', views.network_topology, name='networktopology'),
    url(r'^backups/', views.backups, name='backups'),

]
