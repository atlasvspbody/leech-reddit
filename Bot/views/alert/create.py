from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from Bot.models import Alert
from Bot.views.alert.form import FormAlert

def page(request):
    if request.POST:
        form = FormAlert(request.POST)
        if form.is_valid():
            rule = form.cleaned_data['rule']
            subreddit = form.cleaned_data['subreddit']
            new_alert = Alert(rule=rule, subreddit=subreddit)
            new_alert.save()
            return HttpResponseRedirect(reverse('Bot:index'))
        else:
            return render(request, 'public/create_alert.html',{'form' : form})
    else:
        form = FormAlert()
        return render(request, 'public/create_alert.html',{'form' : form})


            
            
            
    