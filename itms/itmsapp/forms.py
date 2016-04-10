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
                ("device_types", "Device Types"),
                ("devices", "Devices"),
                )
    resource_types = forms.ChoiceField(choices=OPTIONS, label="Select Resource Type:")
    resource_types.widget.attrs['class']='it_resources'


class BackupsForm(forms.Form):

    OPTIONS = (
                ("backup", "Backup"),
                ("restore", "Restore"),

                )
    action_types = forms.ChoiceField(choices=OPTIONS, label="Select Backup/Restore:")
    action_types.widget.attrs['class']='it_resources'
