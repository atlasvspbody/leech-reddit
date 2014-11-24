from django.shortcuts import render,HttpResponseRedirect,redirect
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login
from Bot.views.connection.form import FormLogin

def page(request):
    if request.POST:
        form = FormLogin(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                if request.GET.get('next') is not None:
                    return redirect(request.GET['next'])
                else:
                    return HttpResponseRedirect(reverse('Bot:index'))
                    
        else:
            return render(request,'public/login_user_bot.html',{'form' : form})
    else:
        form = FormLogin()
    return render(request,'public/login_user_bot.html',{'form' : form})