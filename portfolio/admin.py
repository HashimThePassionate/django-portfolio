from django.contrib import admin
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    # Replace with actual field names
    list_display = ('name', 'email', 'subject', 'message')


admin.site.register(Contact, ContactAdmin)
