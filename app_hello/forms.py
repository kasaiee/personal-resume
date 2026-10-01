from django import forms
from django.contrib.auth.models import User
from django.forms import inlineformset_factory

from .models import (
    Profile,
    Experience,
    Education,
    Project,
    Skill,
)


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email"]


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            "phone",
            "job_title",
            "description",
            "intrests",
            "location",
        ]


class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        exclude = ["profile"]


class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        exclude = ["profile"]


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ["profile"]


class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        exclude = ["profile"]


ExperienceFormSet = inlineformset_factory(
    Profile,
    Experience,
    form=ExperienceForm,
    extra=1,
    can_delete=True,
)