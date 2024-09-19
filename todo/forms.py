from django import forms
from django.forms import fields
from formset.widgets import DateTimeInput

from todo.models import Task, Tag


class TaskForm(forms.ModelForm):
    deadline = fields.DateTimeField(
        widget=DateTimeInput,
        required=False,
    )
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Task
        fields = "__all__"


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = "__all__"
