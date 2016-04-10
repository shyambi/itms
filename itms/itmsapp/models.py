import datetime

from django.db import models
from django.utils import timezone


class network_types(models.Model):
    name = models.CharField(max_length=200)
    other_info = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural="Network_types"

class networks(models.Model):
    range = models.CharField(max_length=200)
    gateway = models.GenericIPAddressField(null=True, blank=True)
    netmask = models.CharField(max_length=200, null=True, blank=True)
    dhcp_server = models.GenericIPAddressField(null=True, blank=True)
    dns_server = models.GenericIPAddressField(null=True, blank=True)
    dhcp_range = models.CharField(max_length=200, null=True, blank=True)
    firewall_server = models.GenericIPAddressField(null=True, blank=True)
    network_type = models.ForeignKey(network_types, on_delete=models.CASCADE, null=True, blank=True)
    other_info = models.CharField(max_length=200, null=True, blank=True)

    

    def __str__(self):
        return self.range

    class Meta:
        verbose_name_plural="Networks"

class bare_metal_servers(models.Model):
    ip = models.GenericIPAddressField(null=True, blank=True)
    storage_capacity = models.CharField(max_length=200, null=True, blank=True)
    cpus = models.IntegerField(default=1, null=True, blank=True)
    ram = models.CharField(max_length=200, null=True, blank=True)
    location = models.CharField(max_length=200, null=True, blank=True)
    network = models.ForeignKey(networks, on_delete=models.CASCADE, null=True, blank=True)
    other_info = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.ip

    class Meta:
        verbose_name_plural="Servers"


class cloud_types(models.Model):
    name = models.CharField(max_length=200)
    other_info = models.CharField(max_length=200, null=True, blank=True)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural="Cloud Types"

class managers(models.Model):
    name = models.CharField(max_length=200)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural="Managers"

class projects(models.Model):
    name = models.CharField(max_length=200)
    manager = models.ForeignKey(managers, on_delete=models.CASCADE, null=True, blank=True)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural="Projects"


class clouds(models.Model):
    name = models.CharField(max_length=200, null=True)
    cloud_type = models.ForeignKey(cloud_types, on_delete=models.CASCADE)
    nodes = models.ForeignKey(bare_metal_servers, on_delete=models.CASCADE, null=True, blank=True)
    networks = models.ForeignKey(networks, on_delete=models.CASCADE, null=True, blank=True)
    assigned_to_project = models.ForeignKey(projects, on_delete=models.CASCADE, null=True, blank=True)
    other_info = models.CharField(max_length=200, null=True, blank=True)


    def __str__(self):
      return self.name

    class Meta:
        verbose_name_plural="Clouds"

class vms(models.Model):
    name = models.CharField(max_length=200)
    ip = models.GenericIPAddressField(null=True, blank=True)
    network = models.ForeignKey(networks, on_delete=models.CASCADE, null=True, blank=True)
    username = models.CharField(max_length=200, null=True, blank=True)
    password = models.CharField(max_length=200, null=True, blank=True)
    cloud_id = models.ForeignKey(clouds, on_delete=models.CASCADE, null=True, blank=True)
    assigned_to = models.CharField(max_length=200, null=True, blank=True)
    other_info = models.CharField(max_length=200, null=True, blank=True)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural="VMs"