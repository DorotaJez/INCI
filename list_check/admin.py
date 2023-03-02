from django.contrib import admin
from .models import Ingredient

class IngrAdmin(admin.ModelAdmin):
    list_display=['id','name', 'description']


admin.site.register(Ingredient,IngrAdmin)
