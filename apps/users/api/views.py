from rest_framework import status, viewsets
from rest_framework.response import Response
from apps.users.api.serializers import UserSerializer

from apps.base.general_views import ResponseGeneral

class UserAPIModelViewSet(viewsets.ModelViewSet):

  """
    API Usuarios
  """

  serializer_class = UserSerializer
  response = ResponseGeneral(message="", data=None)

  def get_queryset(self, pk=0):
    if pk:
      return self.get_serializer().Meta.model.objects.filter(id=pk, is_active=True).first()
    return self.get_serializer().Meta.model.objects.filter(is_active=True, is_superuser=False)

  def create(self, request, *args, **kwargs):
    """
      Crea un nuevo usuario

      sin paramentos get
    """

    user_serializer = self.serializer_class(data = request.data)
    if user_serializer.is_valid():
      user_serializer.save()
      self.response.message = "[+] User added"
      self.response.data = user_serializer.data
      headers = self.get_success_headers(user_serializer.data)
      return Response(self.response.__dict__, status=status.HTTP_201_CREATED, headers=headers)
    self.response.message = "[-] ERROR"
    self.response.data = user_serializer.errors
    return Response(self.response.__dict__, status=status.HTTP_400_BAD_REQUEST)
  
  def update(self, request, pk=0):
    """
      Actuliza un nuevo usuario

      parametros --> id del usuario por URL ejemeplo http://example.com/users/3
      El numero indica el id del usuario que vas  modificar
    """

    user = self.get_queryset().filter(id=pk).first() if pk else None
    self.response.message = "[-] ERROR"
    if user:
      user_serializer = self.serializer_class(user, data=request.data)
      if user_serializer.is_valid():
        user_serializer.save()
        self.response.message = "[+] User modified"
        self.response.data = user_serializer.data
        headers = self.get_success_headers(user_serializer.data)
        return Response(self.response.__dict__, status=status.HTTP_200_OK, headers=headers)
      self.response.data = user_serializer.errors
      return Response(self.response.__dict__, status=status.HTTP_400_BAD_REQUEST)
    self.response.data = "User not found"
    return Response(self.response.__dict__, status=status.HTTP_400_BAD_REQUEST)

  def destroy(self, request, pk=0):
    """
      Elimina un nuevo usuario

      parametros --> id del usuario por URL ejemeplo http://example.com/users/3
      El numero indica el id del usuario que vas eliminar
    """

    user = self.get_queryset().filter(id=pk).first() if pk else None
    self.response.message = "[-] ERROR"
    if user:
      user.is_active = False
      self.get_serializer().deleteOldImage(user.image.url)
      user.image = "users/img/empty.png"
      user.save()
      self.response.message = "[+] User eliminated"
      self.response.data = None
      return Response(self.response.__dict__, status=status.HTTP_200_OK)
    self.response.data = "User not found"
    return Response(self.response.__dict__, status=status.HTTP_400_BAD_REQUEST)