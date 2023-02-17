from django.contrib import admin

from .models import CreateStaff, Services, Partners, Reviews


admin.site.register(CreateStaff)
admin.site.register(Services)
admin.site.register(Partners)
admin.site.register(Reviews)