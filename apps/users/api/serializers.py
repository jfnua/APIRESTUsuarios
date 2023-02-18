import os
from uuid import uuid4
from rest_framework import serializers
from apps.users.models import User
from apps.base.helpers import get_new_path, deleteOldImage
from django.conf import settings
from django.contrib.auth.models import Group

class UserSerializer(serializers.ModelSerializer):

  class Meta:
    model = User
    exclude = ("is_superuser", "is_active", "groups","user_permissions","is_staff", "last_login")

  def to_representation(self, instance):
    #instance.get_group_permissions()
    return {
      "id": instance.id,
      "name": instance.name,
      "last_name": instance.last_name,
      "email": instance.email,
      "username": instance.username,
      "password": instance.password,
      "image": instance.image.url,
      "groups": instance.groups.values_list()
    } 
    #el argumento flat elimina el listado interior de los argumentos, osea me los muestra como una lista y no como un matriz
      #"groups": instance.groups.values_list("name", flat=True)
      #"permisos": instance.get_all_permissions(),

  def validate_image(self, value):
    #Cambia el nombre de la imagen por uuid unico si el valor no es igual a cadena vacia
    if value._get_name():
      new_name = get_new_path(value._get_name())
      value._set_name(new_name)
    return value

  def validate_name(self, value):
    if len(value) > 75 or value == "":
      raise serializers.ValidationError("ERROR: Name field is invalid.") # se a errors y no a data
    value = value.title()
    return value

  def validate_last_name(self, value):
    if len(value) > 75 or value == "":
      raise serializers.ValidationError("ERROR: Name field is invalid.") # se a errors y no a data
    value = value.title()
    return value
    
  def update(self, instance, validated_data):
    if validated_data.get("image", -1) != -1 and validated_data["image"] != "":
      deleteOldImage(instance.image.url)
    updated_user = super().update(instance=instance, validated_data=validated_data)
    updated_user.set_password(validated_data["password"])
    updated_user.save()
    return updated_user

  def create(self, validated_data):
    if validated_data.get("groups",-1) == -1 or validated_data["groups"] == []:
      data_groups = [Group.objects.get(name="Common User")]
    else:
      data_groups = validated_data.pop("groups")
    new_user = User(**validated_data)
    new_user.set_password(validated_data["password"])
    new_user.save()
    for group in data_groups:
      group.user_set.add(new_user)
    return new_user
