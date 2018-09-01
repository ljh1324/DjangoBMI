from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse

from bmi.models import BMI

from .forms import BMIForm

import matplotlib.pyplot as plt

def home(request):
    #return HttpResponse('home')
    if request.method == 'POST':
        name = request.POST.get('name', None)
        return redirect('/bmi/member/' + name)

    return render(request, 'bmi/home.html', {})
    

def member_bmi(request, name):
    bmi_query_set_list = BMI.objects.filter(name=name)

    bmi_list = []
    date_list = []
    for bmi in bmi_query_set_list:
        bmi_list.append(bmi.calculate_bmi())
        date_list.append(bmi.get_date())
    
    xn = range(len(date_list))
    plt.ylabel('BMI')
    plt.plot(xn, bmi_list)
    plt.xticks(xn, date_list)
    plt.savefig('bmi/static/temp/' + name + '.png')
    
    img_url = '/static/temp/' + name + '.png'
    
    return render(request, 'bmi/member_bmi.html', {'member_name': name, 'img_url' : img_url})


def bmi_new(request):
    if request.method == "POST":
        form = BMIForm(request.POST)
        
        if form.is_valid():
            bmi = form.save()
            return redirect('/bmi/member/' + bmi.name)
            
    form = BMIForm()
    return render(request, 'bmi/bmi_new.html', {'form': form})