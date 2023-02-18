import os
from uuid import uuid4
from django.conf import settings
from django.core.files import File
from django.core.files.base import ContentFile
from PIL import Image
from io import BytesIO

def path_file_name(dir):
  """
    Generates unique filename to save in model
  """
  def _return_function(instance, filename):
    filename, ext = os.path.splitext(filename)
    return "%s/%s%s" % (dir, uuid4(), ext)
  return _return_function

def get_new_path(path):
  """
    Generates unique filename
  """
  _, ext = os.path.splitext(path)
  return "%s%s" % (uuid4(), ext)

def deleteOldImage(filename):
  """
    Delete image
  """
  if os.path.exists(f"{settings.BASE_DIR}{filename}"):
    os.remove(f"{settings.BASE_DIR}{filename}")

def resize(imageField, size):
  """
    Resize image
  """
  im = Image.open(imageField)  # Catch original
  source_image = im.convert('RGB')
  source_image.thumbnail(size)  # Resize to size
  output = BytesIO()
  source_image.save(output, format="JPEG") # Save resize image to bytes
  output.seek(0)

  content_file = ContentFile(output.read())  # Read output and create ContentFile in memory
  imageField.save(imageField.__str__(), File(content_file), save=False)

  return imageField