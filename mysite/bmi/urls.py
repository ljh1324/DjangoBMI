from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^bmi/member/(?P<name>\w+)$', views.member_bmi, name='member_bmi'),
    url(r'^bmi/new', views.bmi_new, name='bmi_new'),
]