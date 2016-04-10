from django.template import loader
from django.http import Http404
from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import Context, loader
from .models import *
from .forms import NameForm

def index(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render(request))


def resource_list(request):
    latest_resource_list = networks.objects.all()
    template = loader.get_template('networks.html')
    context = {
        'latest_resource_list': latest_resource_list,
    }
    return HttpResponse(template.render(context, request))

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
           #return HttpResponseRedirect('/itms/resources/')
           resource_name = form.cleaned_data['resource_types']
           template = loader.get_template('home.html')
           if resource_name == "networks" :
              latest_resource_list = networks.objects.all()
              context = {
              'latest_resource_list': latest_resource_list,
              'form': form,
              'resource_name': resource_name,
              }

              return HttpResponse(template.render(context, request))
           elif resource_name == "managers" :
              latest_resource_list = managers.objects.all()
              #template = loader.get_template('managers.html')
              context = {
              'latest_resource_list': latest_resource_list,
              'form': form,
              'resource_name': resource_name,
              }
              return HttpResponse(template.render(context, request))
           elif resource_name == "projects" :
              latest_resource_list = projects.objects.all()
              #template = loader.get_template('projects.html')
              context = {
              'latest_resource_list': latest_resource_list,
              'form': form,
              'resource_name': resource_name,
              }

              return HttpResponse(template.render(context, request))
           elif resource_name == "vms" :
              latest_resource_list = vms.objects.all()
              #template = loader.get_template('vms.html')
              context = {
              'latest_resource_list': latest_resource_list,
              'form': form,
              'resource_name': resource_name,
              }

              return HttpResponse(template.render(context, request))
           elif resource_name == "clouds" :
              latest_resource_list = clouds.objects.all()
              #template = loader.get_template('clouds.html')
              context = {
              'latest_resource_list': latest_resource_list,
              'form': form,
              'resource_name': resource_name,
              }

              return HttpResponse(template.render(context, request))
           elif resource_name == "cloud_types" :
              latest_resource_list = cloud_types.objects.all()
              #template = loader.get_template('cloud_types.html')
              context = {
              'latest_resource_list': latest_resource_list,
              'form': form,
              'resource_name': resource_name,
              }

              return HttpResponse(template.render(context, request))
           elif resource_name == "network_types" :
              latest_resource_list = network_types.objects.all()
              #template = loader.get_template('network_types.html')
              context = {
              'latest_resource_list': latest_resource_list,
              'form': form,
              'resource_name': resource_name,
              }

              return HttpResponse(template.render(context, request))
           elif resource_name == "bare_metal_servers" :
              latest_resource_list = bare_metal_servers.objects.all()
              #template = loader.get_template('bare_metal_servers.html')
              context = {
              'latest_resource_list': latest_resource_list,
              'form': form,
              'resource_name': resource_name,
              }


              return HttpResponse(template.render(context, request))

           else :
               return HttpResponseRedirect('/itms/')


           #form.cleaned_data['name']
           #form.cleaned_data['last_name']
           #template = loader.get_template('resources.html')
           #return HttpResponse(template.render(request), {'form': form})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'home.html', {'form': form})






