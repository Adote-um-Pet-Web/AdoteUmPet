from django.contrib import admin

from . import models


class BannerImagesLine(admin.StackedInline):
    model = models.BannerImagens
    extra = 1


admin.site.register(models.BannerImagens)
