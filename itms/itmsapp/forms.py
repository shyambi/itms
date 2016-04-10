from django import forms

class NameForm(forms.Form):

    OPTIONS = (
                ("networks", "Networks"),
                ("network_types", "Network Types"),
                ("bare_metal_servers", "Bare Metal Servers"),
                ("vms", "VMs"),
                ("clouds", "Clouds"),
                ("cloud_types", "Cloud Types"),
                ("managers", "Managers"),
                ("projects", "Projects"),
                )
    resource_types = forms.ChoiceField(choices=OPTIONS, label="Select Resource Type:")
    #resource_types.widget_attrs({'class':'it_resources', 'size':'40'})
    resource_types.widget.attrs['class']='it_resources'
