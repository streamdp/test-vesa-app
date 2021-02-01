import random

from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.views.decorators.http import require_GET

from .forms import QueryForm
from .models import Fan


def index(request, *args, **kwargs):
    fans = None
    if request.method == "POST":
        form = QueryForm(request.POST)

        if form.is_valid():
            airflow = form.cleaned_data.get('airflow')
            airflow_unit = form.cleaned_data.get('airflow_unit')
            pressure = form.cleaned_data.get('pressure')
            pressure_unit = form.cleaned_data.get('pressure_unit')

            fans = Fan.objects.filter(airflow=airflow, airflow_unit=airflow_unit,
                                      pressure=pressure, pressure_unit=pressure_unit)
    else:
        form = QueryForm()
        fans = None
    return render(request, 'gs/index.html', {
        'form': form,
        'fans': fans
    })


def get_all_fans(request, *args, **kwargs):
    fans = Fan.objects.new()
    return render(request, 'gs/index.html', {
        'fans': fans,
    })


def add_fan(request, *args, **kwargs):
    for i in range(10):
        Fan.objects.create_fan(pic_url='temp.png',
                               num=i + random.randrange(100000, 999999),
                               type=random.choice(['AZL', 'BFD', 'ASK', 'LKT']),
                               diameter=random.randrange(500, 1500, 100),
                               airflow=random.randrange(500, 1500, 100),
                               airflow_unit=random.choice(['M3S', 'M3H', 'CFM']),
                               pressure=random.randrange(1, 5),
                               pressure_unit=random.choice(['PA', 'WC']),
                               efficiently=random.randrange(50, 100))
    fans = Fan.objects.new()
    return render(request, 'gs/index.html', {
        'fans': fans
    })
