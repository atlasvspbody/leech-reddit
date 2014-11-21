from Bot.models import Rule, SubReddit, Alert
from django import forms

class FormAlert(forms.Form): 
                  
    rule = forms.ModelChoiceField(label="Rule", queryset=Rule.objects.all())
    subreddit = forms.ModelChoiceField(label="Sub Reddit", queryset=SubReddit.objects.all())
        
    def clean(self):
        cleaned_data = super(FormAlert, self).clean()
        return self.cleaned_data
    
class FormAlertUpdate(FormAlert): 
    def __init__(self, *args, **kwargs):
        self.pk = kwargs.pop('pk', None)
        super(FormAlert, self).__init__(*args, **kwargs)
        if self.pk is not None:
            alert = Alert.objects.get(pk=self.pk)
            self.fields['rule'].initial = alert.rule.id
            self.fields['subreddit'].initial = alert.subreddit.id
            