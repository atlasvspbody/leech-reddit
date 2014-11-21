from django.views.generic import ListView
from Bot.models import SubReddit

class AlertList(ListView):
    model = SubReddit
    template_name = 'public/list_subreddit.html'
    paginate_by = 5
    def get_queryset(self):
        queryset = SubReddit.objects.all()
        return queryset

def page(request):
    return AlertList.as_view()(request)