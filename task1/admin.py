from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from .models import Recipe

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('clickable_recipe_name', 'clickable_recipe_description', 'clickable_recipe_image')
    search_fields = ('recipe_name',)

    def clickable_recipe_name(self, obj):
        return format_html('<a href="{}">{}</a>', reverse('admin:task1_recipe_change', args=[obj.pk]), obj.recipe_name)
    clickable_recipe_name.short_description = 'Recipe Name'

    def clickable_recipe_description(self, obj):
        return format_html('<a href="{}">{}</a>', reverse('admin:task1_recipe_change', args=[obj.pk]), obj.recipe_description)
    clickable_recipe_description.short_description = 'Recipe Description'

    def clickable_recipe_image(self, obj):
        if obj.recipe_image:
            return format_html('<a href="{}"><img src="{}" alt="Recipe Image" style="max-width: 100px; max-height: 100px;" /></a>', reverse('admin:task1_recipe_change', args=[obj.pk]), obj.recipe_image.url)
        else:
            return 'No Image'
    clickable_recipe_image.short_description = 'Recipe Image'
