from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from Bot.models import Rule
from Bot.views.rule.form import FormRule
from django.contrib.auth.decorators import login_required
@login_required
def page(request):
    if request.POST:
        form = FormRule(request.POST)
        if form.is_valid():
            regex = form.cleaned_data['regex']
            alias = form.cleaned_data['alias']
            new_rule = Rule(regex=regex, alias=alias)
            new_rule.save()
            return HttpResponseRedirect(reverse('Bot:index'))
        else:
            return render(request, 'public/create_rule.html',{'form' : form})
    else:
        form = FormRule()
        return render(request, 'public/create_rule.html',{'form' : form})


            
            
            
    