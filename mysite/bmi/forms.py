from django import forms

from .models import BMI

class BMIForm(forms.ModelForm):
    class Meta:
        model = BMI
        fields = ('name', 'weight', 'height')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'이름'}),
            'weight' : forms.TextInput(attrs={'class': 'form-control', 'placeholder':'몸무게'}),
            'height': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'키'}),
        }

        labels = {
            'name': '이름',
            'weight': '몸무게',
            'height': '키'
        }

    # 글자수 제한
    def __init__(self, *args, **kwargs):
        super(BMIForm, self).__init__( *args, **kwargs)