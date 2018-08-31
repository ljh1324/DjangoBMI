from django.shortcuts import render
from django.http import HttpResponse

from bmi.models import BMI

def home(request):
    return HttpResponse('home')


def member_bmi(request, name):
    bmi_query_set_list = BMI.objects.filter(name=name)

    '''
    bmi_list = [list(bmi_query_set)]

    for i in range(len(bmi_list)):
        weight = float(bmi_list[i].weight)
        height = float(bmi_list[i].height) / 100.0

        bmi_list[i] = weight / (height * height)
    '''
    bmi_list = []
    for bmi in bmi_query_set_list:
        bmi_list.append(bmi.calculate_bmi())

    return render(request, 'bmi/member_bmi.html', {'member_name': name, 'bmi_list': bmi_list})