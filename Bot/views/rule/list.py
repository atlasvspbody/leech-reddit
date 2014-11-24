from django.views.generic import ListView
from Bot.models import Rule
from django.contrib.auth.decorators import login_required

class AlertList(ListView):
    model = Rule
    template_name = 'public/list_rule.html'
    paginate_by = 5
    def get_queryset(self):
        queryset = Rule.objects.all()
        return queryset

@login_required
def page(request):
    return AlertList.as_view()(request)