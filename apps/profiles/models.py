# encoding: utf-8

from django.db import models

from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)

class UttrUserManagerManager(BaseUserManager):
    def create_user(self, email,
                        password=None):
        if not email:
            msg = "Users must have a valid email address"
            raise ValueError(msg)

        user = self.model(
            email = UttrUserManagerManager.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,
                            email,
                            password):
        """
        Creates and saves a superuser with the given email and password
        """
        user = self.create_user(email,
            password=password
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class UttrUser(AbstractBaseUser, PermissionsMixin):
    """
    Default user for uttr profiles.
    Requires email confirmation to activate
    """
    email = models.EmailField(
        verbose_name=u'email address',
        max_length=255,
        unique=True,
        db_index=True
        )

    first_name = models.CharField(
        max_length=255,
        blank=True
        )
    last_name = models.CharField(
        max_length=255,
        blank=True
        )

    USERNAME_FIELD = "email"

    is_active = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = UttrUserManagerManager()

    def get_full_name(self):
        # The user is identified by their email and first name
        if self.first_name or self.last_name:
            return "%s (%s %s)" % (self.email, self.first_name, self.last_name)
        else:
            return self.get_short_name()

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __unicode__(self):
        return self.email
