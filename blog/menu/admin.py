from django.contrib import admin
from .models import Journey
from mptt.admin import MPTTModelAdmin

admin.site.register(Journey, MPTTModelAdmin)
