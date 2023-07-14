from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .models import Car
from .forms import CarForm

def car_form(request):
    if request.method == 'POST':
        model_name = request.POST['model_name']
        year = request.POST['year']
        driving_id = request.POST['driving_id']
        Car.objects.create(model_name=model_name, year=year, driving_id=driving_id)
        context = {
            'car':model_name
        }
        return render(request, 'car/accept.html', context)
    else:
        return render(request, 'car/car_form.html')
    
class car_list(ListView):
    model = Car
    template_name = 'car/car_list.html'
    context_object_name = 'cars'

def car_form_fields(request):
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid:
            form.save()
            return render(request, 'car/accept.html', {'form':form})
    else:
        form = CarForm()
        return render(request, 'car/car_form_fields.html', {'form':form})
    
class car_form_default(CreateView):
    model = Car
    template_name = 'car/car_form_default.html'
    fields = '__all__'
    success_url = reverse_lazy('cars')