from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView

class message_display(View):
    def get(self, request):
        context = 'Hello World!'
        return HttpResponse(context)

class home_view(TemplateView):
    template_name = 'classview/home_view.html'