from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^bmi/(?P<name>\w+)/$', views.member_bmi, name='member_bmi'),
]