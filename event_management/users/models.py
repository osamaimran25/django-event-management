
from typing import ClassVar

from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, BooleanField
from django.db.models import EmailField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from .managers import UserManager


class User(AbstractUser):
    name = CharField(_("Name of User"), blank=True, max_length=255)
    first_name = None 
    last_name = None  
    email = EmailField(_("email address"), unique=True)
    username = None
    mobile_number:str = CharField(max_length=255, blank=True)
    is_active:bool = BooleanField(default=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects: ClassVar[UserManager] = UserManager()

    def get_absolute_url(self) -> str:
        """Get URL for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"pk": self.id})
