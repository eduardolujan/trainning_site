from django.conf.urls.static import static
from django.conf.urls import patterns, url, include
from django.conf import settings
from django.views.generic import TemplateView

from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',

	url(r'^test/?$','apps.trainning.views.test', name='test'),
	url(r'^login/?$',TemplateView.as_view(template_name="trainning/login.html")),
	
)