from django.contrib import admin
from .models import *

# Register your models here.

class TagTabularInline(admin.TabularInline):
    model = Tag

class PostAdmin(admin.ModelAdmin):
    inlines = [TagTabularInline]
    list_display = ['title', 'author', 'date', 'status' , 'section', 'main_post']
    list_editable = ['status' , 'section', 'main_post']
    search_fields = ['title', 'section']

admin.site.register(Category)
admin.site.register(Post, PostAdmin)
admin.site.register(Tag)