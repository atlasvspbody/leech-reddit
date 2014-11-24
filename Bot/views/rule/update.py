from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from Bot.models import Rule
from Bot.views.rule.form import FormRuleUpdate
from django.contrib.auth.decorators import login_required
@login_required
def page(request,pk):
    if request.POST:
        form = FormRuleUpdate(request.POST)
        if form.is_valid():
            rule = Rule.objects.get(pk=pk)
            rule.regex = form.cleaned_data['regex']
            rule.alias = form.cleaned_data['alias']
            rule.save()
            return HttpResponseRedirect(reverse('Bot:index'))
        else:
            return render(request, 'public/update_rule.html',{'form' : form,'pk' : pk})
    else:
        form = FormRuleUpdate(pk=pk)
        return render(request, 'public/update_rule.html',{'form' : form,'pk' : pk})


            
            
            
