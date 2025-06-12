from django.contrib import admin
from website.models import Contact , Newsletter

# Register your models here.

class ContactAdmin (admin.ModelAdmin):
    date_hierarchy = "create_date"
    list_display = ("name" , "subject" , "email" , "create_date")
    ordering = ('create_date',)
    search_fields = ('subject','name','email',)

class NewsletterAdmin (admin.ModelAdmin):
    date_hierarchy = "create_date"
    list_display = ("email" , "create_date")
    ordering = ('create_date',)
    search_fields = ('email',)

admin.site.register(Contact,ContactAdmin)
admin.site.register(Newsletter,NewsletterAdmin)
