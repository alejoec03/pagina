from django.shortcuts import render

# Create your views here.

def search(request):
	plantilla = render(request,"search.html",{})
	return plantilla