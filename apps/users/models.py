from django.db import models

# Create your models here.
from typing import Tuple
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from simple_history.models import HistoricalRecords
from apps.base.helpers import path_file_name

class UserManager(BaseUserManager):
  def __create_user(self, username, email, name, last_name, password, is_staff, is_superuser, **kwargs):
    user = self.model(
      username = username,
      email = email,
      name = name,
      last_name = last_name,
      is_staff = is_staff,
      is_superuser = is_superuser,
      **kwargs
    )
    user.set_password(password)
    user.save(using=self.db)
    return user

  def create_user(self, username, email, name, last_name, password, is_staff=False, **kwargs):
    return self.__create_user(username, email, name, last_name, password, is_staff, False, **kwargs)

  def create_superuser(self, username, email, name, last_name, password, is_staff=True, is_superuser=True, **kwargs):
    return self.__create_user(username, email, name, last_name, password, is_superuser, is_staff, **kwargs)


class User(AbstractBaseUser, PermissionsMixin):
  username = models.CharField(max_length=20, unique=True)
  email = models.EmailField("Email", max_length=150, unique=True)
  name = models.CharField("Name", max_length=75)
  last_name = models.CharField("Last Name", max_length=75)
  image = models.ImageField("Picture", upload_to=path_file_name("users/img"), default="users/img/empty.png")
  is_active = models.BooleanField(default=True)
  is_staff = models.BooleanField(default=False)
  historical = HistoricalRecords()
  objects = UserManager()

  class Meta:
    verbose_name = "User"
    verbose_name_plural = "Users"

  #USERNMAE_FIELD es la variable que utilizara django para reconocer al usuario en la autentificacion
  USERNAME_FIELD = "username"
  #Una lista de los nombres de campo que se solicitarán al crear un usuario a través del comando de administración createsuperuser
  REQUIRED_FIELDS =["email","name", "last_name"]

  def natural_key(self) -> Tuple[str]:
    return (self.username,)

  def __str__(self) -> str:
    return f'{self.name} {self.last_name}'
