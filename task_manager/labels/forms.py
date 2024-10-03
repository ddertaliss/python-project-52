from django import forms
from task_manager.labels.models import Label


class LabelCreateForm(forms.ModelForm):
    name = forms.CharField(max_length=200)

    class Meta:
        model = Label
        fields = ['name']
