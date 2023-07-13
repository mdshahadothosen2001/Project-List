from django.shortcuts import render
from .models import Car

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
    

