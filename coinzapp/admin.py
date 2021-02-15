from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Detail)
admin.site.register(Status)
admin.site.register(Package)

admin.site.register(BasicPrice)
admin.site.register(AdvancedPrice)
admin.site.register(PremiumPrice)
admin.site.register(BasicOption)
admin.site.register(AdvancedOption)
admin.site.register(PremiumOption)


# Changing the admin header
admin.site.site_header = "24KOINZ ADMINISTRATION"
