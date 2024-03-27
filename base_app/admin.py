from django.contrib import admin
from .models import ProjectModel, Contact, ExperienceEdu, SkillsLang

@admin.register(ProjectModel)
class ProjectModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'body')
    search_fields = ('name', 'body')


admin.site.register(Contact)
admin.site.register(ExperienceEdu)
admin.site.register(SkillsLang)