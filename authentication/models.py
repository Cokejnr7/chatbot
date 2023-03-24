from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
# Create your models here.


class CustomManager(BaseUserManager):
    def create_user(self, email, password, **other_fields):
        if not email:
            raise ValidationError(_('You must provide an email.'))

        email = self.normalize(email)

        user = self.model(email=email, **other_fields)

        user.set_password(password)

        user.save()

        return user

    def create_superuser(self, email, password, **other_fields):
        other_fields.setdefault("is_staff", True)
        other_fields.setdefault("is_superuser", True)

        if not other_fields['is_staff']:
            raise ValidationError(
                _('is_staff must be set to True for a superuser.'))

        if not other_fields['is_superuser']:
            raise ValidationError(
                _('is_superuser must be set to True for a superuser.'))

        return self.create_user(email, password, **other_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    created = models.DateTimeField(auto_now_add=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = CustomManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email
