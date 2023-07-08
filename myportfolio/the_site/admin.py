from django.contrib import admin
from .models import Identity,Service, Education, Experience, Skill, Work, Uploadresume

# Register your models here.
class DisplayIdentity(admin.ModelAdmin):
    list_display = ['name', 'title','phone','pro_phone','email','pro_email','address','pro_address','birthday']
    
class DisplayService(admin.ModelAdmin):
    list_display = ['service']
    
class DisplayEducation(admin.ModelAdmin):
    list_display = ['qualification','year','school']

class DisplayExperience(admin.ModelAdmin):
    list_display = ['year','title','description']

class DisplaySkill(admin.ModelAdmin):
    list_display = ['skill']
    
class DisplayWork(admin.ModelAdmin):
    list_display = ['name','type','image','tech_used','description']

class DisplayResume(admin.ModelAdmin):
    list_display = ['name']
    
    
admin.site.register(Identity, DisplayIdentity)
admin.site.register(Service, DisplayService)
admin.site.register(Education, DisplayEducation)
admin.site.register(Experience, DisplayExperience)
admin.site.register(Skill, DisplaySkill)
admin.site.register(Work, DisplayWork)
admin.site.register(Uploadresume, DisplayResume)