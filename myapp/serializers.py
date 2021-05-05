from rest_framework import serializers

from .models import *

class SegmentationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Segmentation

        fields = ('id', 'image', 'prediction')