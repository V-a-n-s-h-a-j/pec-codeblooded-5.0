from django.shortcuts import render
from .models import User
from .forms import UserRegForm

# Create your views here.
def home(request):
    return render(request, 'userregistration/home.html')

def add(request):
    # pass
    if request.method =='POST':
        form = UserRegForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=UserRegForm()
    return render(request,'userregistration/add.html',{'form': form})



def authenticate(request):
    pass

def update(request):
    pass

def delete(request):
    pass
