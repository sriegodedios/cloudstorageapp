from django.db import models

# Create your models here.
from django.core.files.storage import FileSystemStorage
from django.conf import settings

def upload_to(instance, filename):
    #return '%s/%s' % (instance.user.user.username, filename)
    
    return '%s/files/%s' % ('sriegode',filename)

upload_storage = FileSystemStorage(location=settings.UPLOAD_ROOT, base_url='/uploads')
class File(models.Model):
    file = models.FileField(upload_to=upload_to,storage=upload_storage)