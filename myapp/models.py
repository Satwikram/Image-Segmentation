from django.db import models

# Create your models here.
def directory_path(instance, filename):
    return 'uploads/images/{0}-{1}'.format(instance.pk, filename)

def prediction_path(instance, filename):
    return 'uploads/predictions/{0}-{1}'.format(instance.pk, filename)


class Segmentation(models.Model):

    image = models.CharField(null = True, blank = True, max_length = 256)
    prediction = models.CharField(null = True, blank = True, max_length = 256)

    def __str__(self):
        return self.id
