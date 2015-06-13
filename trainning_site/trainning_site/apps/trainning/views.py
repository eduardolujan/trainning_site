from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth import authenticate, logout
from django.contrib.auth.forms import UserCreationForm,UserChangeForm,\
                               PasswordChangeForm
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import \
                         authenticate, login as auth_login, logout as auth_logout
from django.core import serializers



def test(request):
	return HttpResponse('Hola')
