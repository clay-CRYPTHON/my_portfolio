from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from .forms import ContactForm
from .models import ProjectModel, ExperienceEdu, SkillsLang


def homePageView(request):
    projects = ProjectModel.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'portfolio/index.html', context)


def contactPageView(request):
    form = ContactForm(request.POST)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return render(request, 'portfolio/request.html', {'form': form})
    context = {
        'form': form
    }
    return render(request, 'portfolio/index.html', context)

def experiencePageView(request):
    experience = ExperienceEdu.objects.filter(status=ExperienceEdu.Status.Experience)
    context = {
        'experience': experience
    }
    return render(request, 'portfolio/index.html', context)