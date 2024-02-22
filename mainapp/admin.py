from django.contrib import admin

from mainapp.models import Category, Recipe

class CategoryAdmin(admin.ModelAdmin):

    save_on_top = True
    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['title'],
            },
        ),
    ]


admin.site.register(Category, CategoryAdmin)
admin.site.register(Recipe)
