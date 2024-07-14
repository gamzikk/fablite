from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.base_user import BaseUserManager

from fablite import settings


class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Users must have an Email')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None):
    	user = self.create_user(username, email, password=password)
    	user.is_staff = True
    	user.save(using=self._db)
    	return user


class CustomUser(AbstractBaseUser):
    username = models.CharField('Имя', max_length=50)
    email = models.EmailField('Почта', max_length=100, unique=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def has_perm(self, perm, obj=None):
    	return True

    def has_module_perms(self, app_label):
    	return True

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.email

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'