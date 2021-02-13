from django.contrib import admin
from .models import *

class TaskAdmin(admin.ModelAdmin):
    list_display = ('author', 'description' ,'completed')
    
    fieldsets = [
         (None,     {'fields': [  'author', 'description' ,'completed']}),
        # ('FECHA', {'fields': ['creation_date', 'update_date'], 'classes': ['']}), #['collapse']
    
    ]

# Register your models here.
admin.site.register(Task, TaskAdmin)
