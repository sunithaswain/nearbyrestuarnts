from django.conf.urls import url
from .import views
from django.views.generic import TemplateView
urlpatterns = [
    url('^signup/',views.signupdetails,name='signdata'), 
    url('^login/',views.loginup,name='logdet'),
    url('^logout/',views.logout),
    url('^location/(?P<useriddata>\d+)/',views.locationdetails,name='loc'),
    url('^ind/(?P<useriddata>\d+)/',views.indivualrest,name='indpage'),
]   