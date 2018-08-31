from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse

from bmi.models import BMI

from .forms import BMIForm

def home(request):
    #return HttpResponse('home')
    if request.method == 'POST':
        name = request.POST.get('name', None)
        return redirect('/bmi/member/' + name)

    return render(request, 'bmi/home.html', {})
    

def member_bmi(request, name):
    bmi_query_set_list = BMI.objects.filter(name=name)

    bmi_list = []
    for bmi in bmi_query_set_list:
        bmi_list.append(bmi.calculate_bmi())

    return render(request, 'bmi/member_bmi.html', {'member_name': name, 'bmi_list': bmi_list})


def bmi_new(request):
    if request.method == "POST":
        form = BMIForm(request.POST)
        
        if form.is_valid():
            bmi = form.save()
            return redirect('/bmi/member/' + bmi.name)
            
    form = BMIForm()
    return render(request, 'bmi/bmi_new.html', {'form': form})