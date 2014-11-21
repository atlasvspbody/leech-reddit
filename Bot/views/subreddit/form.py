from django import forms
from Bot.models import SubReddit

class FormSubReddit(forms.Form):
    name = forms.CharField(label = "Name", max_length=50)
    
    def clean(self):
        cleaned_data = super(FormSubReddit, self).clean()
        return self.cleaned_data

class FormSubRedditUpdate(FormSubReddit): 
    def __init__(self, *args, **kwargs):
        self.pk = kwargs.pop('pk', None)
        super(FormSubReddit, self).__init__(*args, **kwargs)
        if self.pk is not None:
            sub = SubReddit.objects.get(pk=self.pk)
            self.fields['name'].initial = sub.name