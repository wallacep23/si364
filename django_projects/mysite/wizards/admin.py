from django.contrib import admin

# Register your models here.

from wizards.models import Wizard, House

# Register your models here.

admin.site.register(House)
admin.site.register(Wizard)
