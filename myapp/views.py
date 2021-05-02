from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializers import *
import requests
from io import StringIO
import urllib.request
import tensorflow as tf
import numpy as np

class ImageSegmentationAPIView(APIView):

    def get(self, request):

        data = Segmentation.objects.all()

        serializer = SegmentationSerializer(data, many = True)

        return Response(serializer.data, status = status.HTTP_200_OK)

    def post(self, request):

        image = request.data['image']

        print(image.name)

        model = tf.keras.models.load_model('segment.hdf5')

        return Response({"Status": "Sucess!"})
