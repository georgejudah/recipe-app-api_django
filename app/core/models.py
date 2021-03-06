from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
    PermissionsMixin

#helper class for creating user and usuper user - overriding
class UserManager(BaseUserManager):

    def create_user(self, email, password= None, **extra_fields):
        """Create and saves a new user"""
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(email=self.normalize_email(email), **extra_fields) #normalize_email is used to make the email address to small caps for ex GMAIL.com to gmail.com
        user.set_password(password)
        user.save(using = self.db)

        return user
    def create_superuser(self, email, password):
        """creates and saves a new super user"""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using = self._db)

        return user

class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model that supports using email instead of username"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    #customising the USERNAME_FIELD to use email instead of username
