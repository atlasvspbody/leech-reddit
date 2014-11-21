from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from Bot.models import SubReddit
from Bot.views.subreddit.form import FormSubReddit

def page(request):
    if request.POST:
        form = FormSubReddit(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            new_subreddit = SubReddit(name=name)
            new_subreddit.save()
            return HttpResponseRedirect(reverse('Bot:index'))
        else:
            return render(request, 'public/create_subreddit.html',{'form' : form})
    else:
        form = FormSubReddit()
        return render(request, 'public/create_subreddit.html',{'form' : form})


            
            
            
    