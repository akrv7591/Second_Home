from django.shortcuts import render

# Create your views here.
def create(request):
	return render(request, 'create.html')

def detail(request):
	return render(request, 'detail.html')