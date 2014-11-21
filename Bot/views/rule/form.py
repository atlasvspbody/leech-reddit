from django import forms
from Bot.models import Rule

class FormRule(forms.Form):
    regex = forms.CharField(label="Regex", max_length=100)
    alias = forms.CharField(label="Alias", max_length=50)
    
    def clean(self):
        cleaned_data = super(FormRule, self).clean()
        return self.cleaned_data

    
class FormRuleUpdate(FormRule): 
    def __init__(self, *args, **kwargs):
        self.pk = kwargs.pop('pk', None)
        super(FormRule, self).__init__(*args, **kwargs)
        if self.pk is not None:
            rule = Rule.objects.get(pk=self.pk)
            self.fields['regex'].initial = rule.regex
            self.fields['alias'].initial = rule.alias