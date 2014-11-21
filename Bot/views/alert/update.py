from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from Bot.models import Alert
from Bot.views.alert.form import FormAlertUpdate

def page(request,pk):
    if request.POST:
        form = FormAlertUpdate(request.POST)
        if form.is_valid():
            alert = Alert.objects.get(pk=pk)
            alert.rule = form.cleaned_data['rule']
            alert.subreddit = form.cleaned_data['subreddit']
            alert.alias = form.cleaned_data['alias']
            alert.save()
            return HttpResponseRedirect(reverse('Bot:index'))
        else:
            return render(request, 'public/update_alert.html',{'form' : form,'pk' : pk})
    else:
        form = FormAlertUpdate(pk=pk)
        return render(request, 'public/update_alert.html',{'form' : form,'pk' : pk})


            
            
            
