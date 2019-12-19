from django.contrib import admin
from . import models

class PostAdmin(admin.ModelAdmin):
    pass

class CategoryAdmin(admin.ModelAdmin):
    pass


admin.site.register(models.Category)
admin.site.register(models.Post)
