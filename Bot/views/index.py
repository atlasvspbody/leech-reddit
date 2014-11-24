from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import login_required
@login_required
def page(request):
    return render(request, 'public/index_bot.html')
