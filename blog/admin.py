from django.contrib import admin
from blog.models import Post , Category

# Register your models here.

class PostAdmin (admin.ModelAdmin):
    date_hierarchy = "published_date"
    list_display = ("title" , "author" , "counted_view" , "status" , "created_date" , "published_date")
    list_filter = ('status', 'category',)
    ordering = ('created_date',)
    search_fields = ('title',)

admin.site.register(Post, PostAdmin)
admin.site.register(Category)