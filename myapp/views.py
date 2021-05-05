from django.core.files.storage import FileSystemStorage
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
from .serializers import *
import os
import shutil
import matplotlib.pyplot as plt
from .models import *

def normalize(input_image):

    #input_image = tf.constant(input_image)
    input_image = tf.image.resize(input_image, (128, 128))
    input_image = tf.cast(input_image, tf.float32) / 255.0

    return input_image

def create_mask(pred_mask):

  pred_mask = tf.argmax(pred_mask, axis=-1)
  pred_mask = pred_mask[..., tf.newaxis]

  return pred_mask[0]

class ImageSegmentationAPIView(APIView):

    def get(self, request):

        data = Segmentation.objects.all()

        serializer = SegmentationSerializer(data, many = True)

        return Response(serializer.data, status = status.HTTP_200_OK)

    def post(self, request):

        image = request.data['image']

        model = tf.keras.models.load_model('segment.hdf5')

        #image = normalize(image)
        print(image)
        folder = 'uploads/images/'

        fs = FileSystemStorage(location=folder)
        name = fs.save(image.name, image)

        mediapath = folder + "{}"
        filepath = os.path.join(mediapath).format(name)
        print("File path:", filepath)

        input_image = plt.imread(filepath)

        input_image = normalize(input_image)

        print(input_image.shape)
        prediction = model.predict(input_image[tf.newaxis, ...])

        prediction = create_mask(prediction)

        prediction = tf.image.resize(prediction, (480, 480))

        prediction = tf.keras.preprocessing.image.array_to_img(prediction)

        path = 'uploads/predictions/'+name
        print(path)
        plt.imsave(path, prediction)

        data = {'image': filepath,
                'prediction': path}

        serializer = SegmentationSerializer(data = data)

        if serializer.is_valid():
            serializer.save()

        return Response({"Status": serializer.data})
