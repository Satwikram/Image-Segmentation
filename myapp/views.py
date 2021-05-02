from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView


class ImageSegmentationAPIView(APIView):

    def post(self, request):
        print(request.data)

        return Response({"Status": "Sucess"})
