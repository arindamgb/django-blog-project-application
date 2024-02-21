from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, UserProfileChange, ProfilePic

# Create your views here.

def sign_up(request):
    #form = UserCreationForm()
    form = SignUpForm()
    registered = False
    if request.method == 'POST':
        #form = UserCreationForm(request.POST)
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            registered = True
    dict = {'form': form, 'registered': registered}
    return render(request, 'app_login/signup.html', context=dict)


def login_page(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                print('login successful')
                return HttpResponseRedirect(reverse('index'))
    return render(request, 'app_login/login.html', context={'form':form})

@login_required
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

@login_required
def profile(request):
    return render(request, 'app_login/profile.html', context={})

@login_required
def user_change(request):
    current_user = request.user
    form = UserProfileChange(instance=current_user)
    if request.method == 'POST':
        form = UserProfileChange(request.POST, instance=current_user)
        if form.is_valid():
            form.save()
            form = UserCreationForm(instance=current_user)
    return render(request, 'app_login/change_profile.html', context={'form':form})

# @login_required
# def pass_change(request):
#     current_user = request.user
#     changed = False
#     form = PasswordChangeForm(current_user)
#     if request.method == 'POST':
#         form = PasswordChangeForm(current_user, request.POST)
#         if form.is_valid():
#             form.save()
#             changed = True
#     return render(request, 'app_login/pass_change.html', context={'form':form, 'changed':changed})


@login_required
def pass_change(request):
    current_user = request.user
    changed = False
    form = PasswordChangeForm(current_user)
    #form = PasswordChangeForm(user=current_user)  # works same as above
    if request.method == 'POST':
        form = PasswordChangeForm(current_user, request.POST)
        #form = PasswordChangeForm(user=current_user, data=request.POST)  # works same as above
        if form.is_valid():
            form.save()
            changed = True
    return render(request, 'app_login/pass_change.html', context={'form':form, 'changed':changed})
        

@login_required
def add_pro_pic(request):
    form = ProfilePic()
    if request.method == 'POST':
        form = ProfilePic(request.POST, request.FILES)
        if form.is_valid():
            user_obj = form.save(commit=False)
            user_obj.user = request.user
            user_obj.save()
            return HttpResponseRedirect(reverse('app_login:profile'))
    return render(request, 'app_login/add_pro_pic.html', context={'form':form})

@login_required
def change_pro_pic(request):
    form = ProfilePic(instance=request.user.user_profile)
    if request.method == 'POST':
        form = ProfilePic(request.POST, request.FILES, instance=request.user.user_profile)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('app_login:profile'))
    return render(request, 'app_login/add_pro_pic.html', context={'form':form})
                  
    
                  
                  




