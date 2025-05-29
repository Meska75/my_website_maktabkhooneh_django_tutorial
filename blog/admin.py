from django.contrib import admin
from blog.models import Post

# Register your models here.

class PostAdmin (admin.ModelAdmin):
    date_hierarchy = "published_date"
    list_display = ("title" , "counted_view" , "status" , "created_date" , "published_date")
    list_filter = ('status',)
    ordering = ('created_date',)
    search_fields = ('title',)

admin.site.register(Post, PostAdmin)