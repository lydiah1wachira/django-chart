from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Editors

# Create your views here.
def bar_chart_view(request):
    editors_data = Editors.objects.all()

    context = {
        'editors_data': editors_data,
    }

    return render(request, 'editors/chart.html', context)

def line_chart_view(request):
    editors_data = Editors.objects.all()

    context = {
        'editors_data': editors_data,
    }

    return render(request, 'editors/lineGraph.html', context)
