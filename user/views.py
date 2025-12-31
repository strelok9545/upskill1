from django.shortcuts import render,redirect
from .forms import RegisterForm

# Create your views here.

def register_page(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(user.password)
            user.save()
            return redirect('user:login_page')
        
    return render(request,'user/register.html',{'form':form})