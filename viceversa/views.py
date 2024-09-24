from django.http import HttpResponse
from django.shortcuts import render


def home(request):
	return render(request, 'home.html')

def reverse(request):
	message = request.GET['message']
	reverse_text = message[::-1]
	return render(request, 'reverse.html', {'message':message, 'reversetext':reverse_text})