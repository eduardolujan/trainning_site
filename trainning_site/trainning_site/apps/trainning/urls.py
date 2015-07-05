from django.conf.urls.static import static
from django.conf.urls import patterns, url, include
from django.conf import settings
from django.views.generic import TemplateView
import front_edit
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',

	url(r'^test/?$','apps.trainning.views.test', name='test'),
	url(r'^login/?$','apps.trainning.views.login', name='login'),
	url(r'^logout/?$','apps.trainning.views.logout', name='logout'),
	url(r'', include('front_edit.urls')),
	url(r'^trainning/?$','apps.trainning.views.trainning', name='trainning'),
)