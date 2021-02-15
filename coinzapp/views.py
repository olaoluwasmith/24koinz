from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, Http404
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.db import models
from django.db.models import Q, signals
from .forms import *

# Create your views here
def index(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        p_form = CreateDetailForm(request.POST)

        if form.is_valid() and p_form.is_valid():
            user = form.save()
            user.refresh_from_db()
            p_form = CreateDetailForm(request.POST, instance=user.detail)
            p_form.full_clean()
            p_form.save()
            username = form.cleaned_data.get('username')

            messages.success(request, 'Account successfully created for ' + username)
            return redirect('login')
        else:
            messages.info(request, 'Error encountered! Check if data is valid and email is not used already.')
    else: 
        form = CreateUserForm()
        p_form = CreateDetailForm()


    context = {'form': form, 'p_form': p_form}
    return render(request, 'index.html', context)

def loginPage(request):
    redirect_to = request.GET.get('next', '/dashboard/')
    if request.method == 'POST':
        userinput = request.POST.get('username')
        try:
            username = User.objects.get(email=userinput).username
        except User.DoesNotExist:
            username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(redirect_to)
        else:
            messages.info(request, 'Username, email or password incorrect.')

    return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    return redirect('/')

@login_required
def editProfile(request):
    if request.method == 'POST':
        u_form = UpdateUserForm(request.POST, instance=request.user)
        p_form = UpdateDetailForm(request.POST, 
                                    request.FILES,
                                    instance=request.user.detail)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Profile updated successfully.')
            return redirect('dashboard')
    else:
        u_form = UpdateUserForm(instance=request.user)
        p_form = UpdateDetailForm(instance=request.user.detail)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'edit-profile.html', context)

@login_required
def dashboard(request):
    details = Detail.objects.all()
    return render(request, 'dashboard.html', {'details': details})

@login_required
def basicOption(request):
    if request.method == 'POST':
        form = BasicForm(request.POST)
        if form.is_valid():
            basic = form.save(commit=False)
            basic.user = request.user
            basic.save()

            messages.success(request, 'Submitted successfully. Update pending.')
            return HttpResponseRedirect('/dashboard/')
    else:
        form = BasicForm()

    context = {
        'form': form,
    }
    return render(request, 'basic_option.html', context)

@login_required
def advancedOption(request):
    if request.method == 'POST':
        form = AdvancedForm(request.POST)
        if form.is_valid():
            advanced = form.save(commit=False)
            advanced.user = request.user
            advanced.save()

            messages.success(request, 'Submitted successfully. Update pending.')
            return HttpResponseRedirect('/dashboard/')
    else:
        form = AdvancedForm()

    context = {
        'form': form,
    }
    return render(request, 'advanced_option.html', context)

@login_required
def premiumOption(request):
    if request.method == 'POST':
        form = PremiumForm(request.POST)
        if form.is_valid():
            premium = form.save(commit=False)
            premium.user = request.user
            premium.save()

            messages.success(request, 'Submitted successfully. Update pending.')
            return HttpResponseRedirect('/dashboard/')
    else:
        form = PremiumForm()

    context = {
        'form': form,
    }
    return render(request, 'premium_option.html', context)
