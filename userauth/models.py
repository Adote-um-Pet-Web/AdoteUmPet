import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models

ACCOUNT_STATUS = (
    ("active", "Active"),
    ("pending", "Pending"),
    ("in-active", "In-active"),
)


class User(AbstractUser):
    id = models.UUIDField(
        primary_key=True, unique=True, default=uuid.uuid4, editable=False
    )
    username = models.CharField(max_length=100, unique=False)
    email = models.EmailField(unique=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=100, blank=True, null=True)
    instagram_field = models.CharField(max_length=100, blank=True, null=True)
    facebook_field = models.CharField(max_length=100, blank=True, null=True)
    image_user_profile = models.ImageField(
        upload_to="user/profile/%Y/%m/", blank=True, null=True
    )
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self) -> str:
        return self.username


def user_directory_path(instace, filename):
    ext = filename.split(".")[-1]
    filename = "%s_%s" % (instace.id, ext)

    return "user_{0}/{1}".format(instace.user.id, filename)


# class Profile(models.Model):
#     id = models.UUIDField(
#         primary_key=True, unique=True, default=uuid.uuid4, editable=False
#     )
#     user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="account")
#     account_status = models.CharField(
#         max_length=100, choices=ACCOUNT_STATUS, default="in-active"
#     )
#     red_code = ShortUUIDField(
#         unique=True, length=10, max_length=20, alphabet="abcdefgh1234567890"
#     )
#     date = models.DateTimeField(auto_now_add=True)

#     class Meta:
#         ordering = ["-date"]

#     def __str__(self):
#         return f"{self.user}"


# def create_account(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)


# def save_account(sender, instance, **kwargs):
#     instance.account.save()


# post_save.connect(create_account, sender=User)
# post_save.connect(save_account, sender=User)
