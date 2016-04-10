from django.template import loader
from django.http import Http404
from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import Context, loader
from .models import *
from .forms import NameForm
from .forms import BackupsForm
from .backups import backup_itms

def index(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render(request))


def backups(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = BackupsForm(request.POST)
        # check whether it's valid:
        if form.is_valid():

           action_name = form.cleaned_data['action_types']
           template = loader.get_template('backups.html')
           if action_name == "backup" :
              backup_itms().backup()
              context = {
              'form': form,
              'summary': "Backup is successful, data backed up to folder /opt/backups",
              }
              return HttpResponse(template.render(context, request))
           elif action_name == "restore" :
              latest_resource_list = managers.objects.all()
              context = {
              'latest_resource_list': latest_resource_list,
              'form': form,
              'resource_name': action_name,
              }
              return HttpResponse(template.render(context, request))
           else :
              return HttpResponseRedirect('/itms/backups')
    else:
        form = BackupsForm()

    return render(request, 'backups.html', {'form': form})

def network_topology(request):
    template = loader.get_template('network_topology.html')
    return HttpResponse(template.render(request))

def resources(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():

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
              context = {
              'latest_resource_list': latest_resource_list,
              'form': form,
              'resource_name': resource_name,
              }
              return HttpResponse(template.render(context, request))
           elif resource_name == "projects" :
              latest_resource_list = projects.objects.all()
              context = {
              'latest_resource_list': latest_resource_list,
              'form': form,
              'resource_name': resource_name,
              }

              return HttpResponse(template.render(context, request))
           elif resource_name == "vms" :
              latest_resource_list = vms.objects.all()
              context = {
              'latest_resource_list': latest_resource_list,
              'form': form,
              'resource_name': resource_name,
              }

              return HttpResponse(template.render(context, request))
           elif resource_name == "clouds" :
              latest_resource_list = clouds.objects.all()
              context = {
              'latest_resource_list': latest_resource_list,
              'form': form,
              'resource_name': resource_name,
              }

              return HttpResponse(template.render(context, request))
           elif resource_name == "cloud_types" :
              latest_resource_list = cloud_types.objects.all()
              context = {
              'latest_resource_list': latest_resource_list,
              'form': form,
              'resource_name': resource_name,
              }

              return HttpResponse(template.render(context, request))
           elif resource_name == "network_types" :
              latest_resource_list = network_types.objects.all()
              context = {
              'latest_resource_list': latest_resource_list,
              'form': form,
              'resource_name': resource_name,
              }

              return HttpResponse(template.render(context, request))
           elif resource_name == "bare_metal_servers" :
              latest_resource_list = bare_metal_servers.objects.all()
              context = {
              'latest_resource_list': latest_resource_list,
              'form': form,
              'resource_name': resource_name,
              }


              return HttpResponse(template.render(context, request))
           elif resource_name == "device_types" :
              latest_resource_list = device_types.objects.all()
              context = {
              'latest_resource_list': latest_resource_list,
              'form': form,
              'resource_name': resource_name,
              }


              return HttpResponse(template.render(context, request))
           elif resource_name == "devices" :
              latest_resource_list = devices.objects.all()
              context = {
              'latest_resource_list': latest_resource_list,
              'form': form,
              'resource_name': resource_name,
              }


              return HttpResponse(template.render(context, request))

           else :
               return HttpResponseRedirect('/itms/')




    else:
        form = NameForm()

    return render(request, 'home.html', {'form': form})






