from django.shortcuts import render

def page(request):
    return render(request, 'public/index_bot.html')
