from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
@user_passes_test(lambda u: u.is_superuser)
def page(request):
    return render(request, 'public/index_bot.html')
