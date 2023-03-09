from django.shortcuts import render

# Create your views here.
def test():
	mytest = ("Hello World"

	)
	return mytest

def index(request):
	mytest = test()

	return render(request, 'esd_home/index.html', {'test': mytest})
