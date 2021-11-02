from django.contrib import admin
from .models import Graphs
# Register your models here.

class GraphAdmin(admin.ModelAdmin):
    list_display= ('title', 'description')

admin.site.register(Graphs)
