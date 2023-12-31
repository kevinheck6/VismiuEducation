from django.shortcuts import render
from django import http

def index(request):
	return render(request, 'core/index.html')