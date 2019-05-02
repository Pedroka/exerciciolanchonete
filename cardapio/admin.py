from django.contrib import admin
from .models import Lanches, Ingredientes


class LanchesAdmin(admin.ModelAdmin):
    list_display = ['lanche_name','lanche_created','lanche_modified']
    search_fields = ['lanche_name']
    list_filter = ['lanche_created']

class IngredientAdmin(admin.ModelAdmin):
    list_display = ['ingrediente_name','ingredient_created','ingredient_modifed']
    search_fields = ['ingrediente_name']
    list_filter = ['ingredient_created']

admin.site.register(Lanches,LanchesAdmin)
admin.site.register(Ingredientes,IngredientAdmin)