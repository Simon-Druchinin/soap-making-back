from django.contrib import admin

from . import models


@admin.register(models.Flavour)
class FlavourAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Color)
class ColorAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Shape)
class ShapeAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Filling)
class FillingAdmin(admin.ModelAdmin):
    pass
