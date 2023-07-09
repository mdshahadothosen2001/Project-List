from django.http import HttpResponse
from django.views import View

class message_display(View):
    def get(self, request):
        context = 'Hello World!'
        return HttpResponse(context)