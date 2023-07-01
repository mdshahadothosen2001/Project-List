from django.shortcuts import render
from django.views import View

class home_page(View):
    def get(self, request):
        return render(request, 'develop/home_page.html')
