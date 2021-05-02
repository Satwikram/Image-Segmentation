from django.db import models

# Create your models here.
def directory_path(instance, filename):
    return 'uploads/images/{0}-{1}'.format(filename, instance.pk)

def prediction_path(instance, filename):
    return 'uploads/predictions/{0}-{1}'.format(filename, instance.pk)


class Segmentation(models.Model):

    image = models.ImageField(upload_to = directory_path)
    prediction = models.ImageField(upload_to = prediction_path)
