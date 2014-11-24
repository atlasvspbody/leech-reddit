from django.views.generic import ListView
from Bot.models import Alert
from django.contrib.auth.decorators import login_required

class AlertList(ListView):
    model = Alert
    template_name = 'public/list_alert.html'
    paginate_by = 5
    def get_queryset(self):
        queryset = Alert.objects.all()
        return queryset

@login_required
def page(request):
    return AlertList.as_view()(request)