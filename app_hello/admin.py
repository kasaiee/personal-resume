from django.contrib import admin
from app_hello.models import Profile, Experience, Education, Project, Skill


class SkillInline(admin.TabularInline):
    model = Skill

class ProjectInline(admin.TabularInline):
    model = Project

class EducationInline(admin.TabularInline):
    model = Education
    
class ExperienceInline(admin.TabularInline):
    model = Experience

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user__username', 'job_title')
    search_fields = ('user__username', 'user__first_name', 'user__last_name', 'job_title')
    list_filter = ('location', )
    inlines = (SkillInline, ProjectInline, EducationInline, ExperienceInline)


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Experience)
admin.site.register(Education)
admin.site.register(Project)
admin.site.register(Skill)
