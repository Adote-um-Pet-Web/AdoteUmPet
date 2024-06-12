from django.db import models


# Create your models here.
class BannerImagens(models.Model):
    banner_image1 = models.ImageField(
        upload_to="banner/imagens/%Y/%m/", blank=False, null=False
    )
    banner_image2 = models.ImageField(
        upload_to="banner/imagens/%Y/%m/", blank=False, null=False
    )
    banner_image3 = models.ImageField(
        upload_to="banner/imagens/%Y/%m/", blank=False, null=False
    )
