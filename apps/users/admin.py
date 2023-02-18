from django.contrib import admin
from django.utils.html import mark_safe
from .models import User
from .models import User
from apps.base.helpers import deleteOldImage, resize


# Register your models here.
@admin.register(User)
class AdminUser(admin.ModelAdmin):
  readonly_fields = ("is_superuser", "is_staff")
  list_display = ["id","username", "email","name", "last_name", "show_image"]
  list_display_links = ["id","username"]
  search_fields = ["id", "username", "email", "name"]

  @admin.display(description="IMAGE")
  def show_image(self, obj):
    return mark_safe("<a href='%s' target='_blank'><img src='%s' width='50' height='50'></a>" % (obj.image.url, obj.image.url))

  def save_model(self, request, obj, form, change):
    obj.name = obj.name.title()
    obj.last_name = obj.last_name.title()
    
    if obj.password.startswith("pbkdf2"):
      obj.password=obj.password
    else:
      obj.set_password(obj.password)
    
    if obj.id:
      user = User.objects.get(id=obj.id)
      if "/empty.png" not in user.image.url and obj.image.url != user.image.url: #verifica que la imagen no sea la de por defecto
        deleteOldImage(user.image.url) #elimina la imagen anterior
        obj.image = resize(obj.image, (250, 250))
    elif "/empty.png" not in obj.image.url:
      obj.image = resize(obj.image, (250, 250))
    super().save_model(request, obj, form, change)

  def delete_model(self, request, obj) -> None:
    if "/empty.png" not in obj.image.url:
      deleteOldImage(obj.image.url)
    super().delete_model(request, obj)

  def get_queryset(self, request):
    if request.user.is_superuser:
      self.readonly_fields = () #Le permite modificar cualquier campo
      return self.model.objects.all()
    elif request.user.is_staff:
      self.readonly_fields = ("is_superuser", "is_staff", "user_permissions", "groups")
      return self.model.objects.filter(is_superuser=False, is_staff=False) | self.model.objects.filter(id=request.user.id)
    
    self.readonly_fields = ("is_superuser", "is_staff")
    return self.model.objects.filter(is_superuser=False, is_staff=False)
