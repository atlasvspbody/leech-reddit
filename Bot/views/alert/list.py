from django.views.generic import ListView
from Bot.models import Alert

class AlertList(ListView):
    model = Alert
    template_name = 'public/list_alert.html'
    paginate_by = 5
    def get_queryset(self):
        queryset = Alert.objects.all()
        return queryset

def page(request):
    return AlertList.as_view()(request)