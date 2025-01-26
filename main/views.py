from django.shortcuts import render
from .models import Profile, Education, Project, Skill

def home(request):
    profile = Profile.objects.first()
    education = Education.objects.all()
    projects = Project.objects.all()
    skills = {
        'Programming Languages': Skill.objects.filter(category='PROG'),
        'Frameworks': Skill.objects.filter(category='FRAME'),
        'Tools & Technologies': Skill.objects.filter(category='TOOL'),
        'Soft Skills': Skill.objects.filter(category='SOFT'),
    }
    
    return render(request, 'main/home.html', {
        'profile': profile,
        'education': education,
        'projects': projects,
        'skills': skills,
    })
