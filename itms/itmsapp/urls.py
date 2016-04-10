from django.conf.urls import url


from . import views
app_name = 'itmsapp'

urlpatterns = [
    #url(r'^$', views.index, name='index'),
    url(r'^networks/$', views.resource_list, name='resource_list'),
    #url(r'^name/$', views.get_name, name='name'),
    url(r'^$', views.get_name, name='name'),



]
