from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.template import RequestContext
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import authenticate, login as django_login
from django.contrib.auth.decorators import login_required


from pprint import pprint


def test(request):
	response = {}

	obj = {
		'text_field':'text_field', 
		'char_field':'char_field'
	}
	response = { 'objects' : [obj,obj] }
	return render_to_response(
		'trainning/test.html', 
		{ 'response':[obj,obj] },
		context_instance=RequestContext(request)	
	)


@login_required
def trainning(request):
	response = {
		'success': True,
		'message': _('Message from ')
	}
	return render_to_response(
		'trainning/base.html', 
		response,
		context_instance=RequestContext(request)	
	)


@login_required(login_url='/login')
def logout(request):
	user = request.user 
	username = user.username

	if not user:
		HttpResponseRedirect('/login')

	return  HttpResponse('Logout success for %s'% username)

@csrf_protect
def login(request):
	if request.POST:
		pprint(request.POST)
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				django_login(request, user)
				return HttpResponse('Loged')
			else:
				return HttpResponse('Disabled account')	
		else:
			return HttpResponse('Inavlid Login')

	return render_to_response(
		'trainning/login.html', 
		{},
		context_instance=RequestContext(request)	
	)





