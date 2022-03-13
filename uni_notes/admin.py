from django.contrib import admin
from .models import Note, Topic

# Register your models here.
@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    # top display of options
    list_display = ('title', 'slug','topic', 'author', 'publish')
    # menu on the right side with filtering options
    list_filter = ('created', 'publish', 'author')
    # search field and where to search
    search_fields = ('title', 'body')
    # creating a slug using title
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    
   

""" registering topic view in admin page """
admin.site.register(Topic)