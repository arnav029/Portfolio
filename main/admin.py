from django.contrib import admin
from .models import Profile, Education, Project, Skill

admin.site.register(Profile)
admin.site.register(Education)
admin.site.register(Project)
admin.site.register(Skill)