from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect




def test(request):
	return HttpResponse('Hola')



