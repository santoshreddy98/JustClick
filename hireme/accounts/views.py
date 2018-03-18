from django.shortcuts import render,redirect
from accounts.models import UserProfile,Category
from django.shortcuts import get_object_or_404
from django.views.generic.list import ListView
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm,EditProfileForm,ProfileForm
# Create your views here.

def home(request):
    return redirect('/home')

def view_home(request):
    items = UserProfile.objects.all()
    args = {'item':items}
    return render(request,'accounts/home.html',args)

def view_list(request):
    prof = UserProfile.objects.all()
    return render(request,'accounts/list.html',{'prof':prof})

def search(request):
    query = request.GET.get("q")
    if query:
        items = UserProfile.objects.filter(Q(user__first_name__icontains=query)|Q(user__last_name__icontains=query)|Q(category__icontains=query)|Q(qualif__icontains=query)|Q(description__icontains=query)).distinct()

    return render(request,'accounts/home.html',{'items':items})

@login_required
def profile(request):
    user = request.user
    return render(request,'accounts/profile.html',{'user':user})

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login')
    else:
        form = RegistrationForm()


    return render(request,'accounts/signup.html',{'form':form})


@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST,instance=request.user)
        form2 = ProfileForm(request.POST,instance=request.user.userprofile)
        if form.is_valid() and form2.is_valid():
            form.save()
            form2.save()
            return redirect('/profile')
    else:
        form = EditProfileForm(instance=request.user)
        form2 = ProfileForm(instance=request.user.userprofile)

    return render(request,'accounts/edit.html',{'form':form,'form2':form2})
