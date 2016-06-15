from django.contrib import admin
from learn.models import Technology, Domain, Resources
# Register your models here.

class TechnologyAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

class DomainAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

class ResourceAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Technology, TechnologyAdmin)
admin.site.register(Domain, DomainAdmin)
admin.site.register(Resources, ResourceAdmin)

#TODO
#generate permalinks for the resources as slug