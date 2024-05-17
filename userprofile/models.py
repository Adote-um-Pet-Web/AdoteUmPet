import uuid

from django.db import models
from django.db.models.signals import post_save
from shortuuid.django_fields import ShortUUIDField

from userauth.models import User

ACCOUNT_STATUS = (
    ("active", "Active"),
    ("pending", "Pending"),
    ("in-active", "In-active")
)


def user_directory_path(instace, filename):
    ext = filename.split('.')[-1]
    filename = "%s_%s" % (instace.id, ext)

    return "user_{0}/{1}".format(instace.user.id, filename)


class Profile(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='account')
    account_status = models.CharField(max_length=100, choices=ACCOUNT_STATUS, default="in-active")
    red_code = ShortUUIDField(unique=True, length=10, max_length=20, alphabet="abcdefgh1234567890")
    date = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ["-date"]

    def __str__(self):
        return f"{self.user}"


def create_account(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

def save_account(sender, instance, **kwargs):
    instance.account.save()


post_save.connect(create_account, sender=User)
post_save.connect(save_account, sender=User)
