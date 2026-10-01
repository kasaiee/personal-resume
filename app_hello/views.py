from datetime import datetime
from django.core.paginator import Paginator
from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.db.models import Q
from app_hello.models import Profile
from .forms import UserForm, ProfileForm, ExperienceFormSet
from django.shortcuts import render, redirect


def index(request):
    location = request.GET.get('location')
    q = request.GET.get('q') or ''
    skills = request.GET.getlist('skill')
    if q:
        users = User.objects.filter(
            Q(first_name__icontains=q) |
            Q(last_name__icontains=q) |
            Q(profile__job_title__icontains=q) |
            Q(skill__title__icontains=q)
        )
    else:
        users = User.objects.all()

    if skills:
        users = users.filter(skill__title__in=skills)

    if location:
        users = users.filter(profile__location__icontains=location)

    ITEM_PER_PAGE = 5  # Item per page
    paginator = Paginator(users.distinct(), ITEM_PER_PAGE)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        "page_obj": page_obj,
        "q": q,
        'skills': skills,
        'locations': Profile.objects.values_list('location', flat=True)
    }
    return render(request, "index.html", context)


    # users = User.objects.all()
    # context = {
    #     'users': users
    # }
    # return render(request, 'index.html', context)


def resume(request, id):
    user = get_object_or_404(User, id=id)
    context = {'user': user}
    return render(request, 'resume.html', context)


def resume_edit(request):
    user_form = None
    profile_form = None

    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        experience_formset = ExperienceFormSet(
            request.POST,
            instance=request.user
        )

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
        experience_formset = ExperienceFormSet(instance=request.user.profile)

    context = {
        'user_form':  user_form,
        'profile_form': profile_form,
        'experience_formset': experience_formset
    }
    return render(request, 'resume-edit.html', context)


def my_form(request):
    q = request.GET.get('q')
    users = User.objects.all()
    if q:
        users = users.filter(first_name__icontains=q)
    context = {
        'users': users,
        'q': q
    }
    return render(request, 'my_form.html', context)