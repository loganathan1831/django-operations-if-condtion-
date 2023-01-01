from django.shortcuts import render

# Create your views here.
def operations(request):
    d={'a':5}
    return render(request,'operations.html',d)