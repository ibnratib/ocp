
from django.contrib import admin
from .models import contact
# Register your models here.
class mycontact(admin.ModelAdmin):
    pass
admin.site.register(contact, mycontact)