""" Database Models"""
from django.db import models
from django.contrib.auth.models import(
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)

class UserManager(BaseUserManager):
    """Manager class for users"""
    def create_user(self, email, password=None, **extra_fields):
        """creates, saves and returns new users"""
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

class User(AbstractBaseUser,PermissionsMixin):
    """User in the system"""
    email = models.EmailField(max_length=200, unique=True)
    name = models.CharField(max_length=20)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    objects = UserManager()
    USERNAME_FIELD = 'email'
