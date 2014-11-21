from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from Bot.models import  SubReddit
from Bot.views.subreddit.form import FormSubRedditUpdate

def page(request,pk):
    if request.POST:
        form = FormSubRedditUpdate(request.POST)
        if form.is_valid():
            sub = SubReddit.objects.get(pk=pk)
            sub.name = form.cleaned_data['name']
            sub.save()
            return HttpResponseRedirect(reverse('Bot:index'))
        else:
            return render(request, 'public/update_subreddit.html',{'form' : form,'pk' : pk})
    else:
        form = FormSubRedditUpdate(pk=pk)
        return render(request, 'public/update_subreddit.html',{'form' : form,'pk' : pk})


            
            
            
