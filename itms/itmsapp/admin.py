from django.contrib import admin


from .models import *


admin.site.register(networks)
admin.site.register(network_types)
admin.site.register(bare_metal_servers)
admin.site.register(vms)
admin.site.register(cloud_types)
admin.site.register(clouds)
admin.site.register(projects)
admin.site.register(managers)



