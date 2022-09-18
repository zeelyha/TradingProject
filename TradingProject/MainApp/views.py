from rest_framework import generics, status
from django.shortcuts import render
import io, csv, pandas as pd
from rest_framework.response import Response
from .models import File
from .serializers import FileUploadSerializer, SaveFileSerializer

# Create your views here.
class UploadFileView(generics.CreateAPIView):
    serializer_class = FileUploadSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        file = serializer.validated_data['file']
        timeframe = serializer.validated_data['timeframe']
        reader = pd.read_csv(file)
        for _, row in reader.iterrows():
            new_file = File( id = row['BANKNIFTY'], 
            date = row["DATE"],
            time = row["TIME"], 
            open= row["OPEN"],
            high= row['HIGH'],
            low= row["LOW"],
            close= row["CLOSE"], 
            volume = row["VOLUME"]
            )
            new_file.save()
            
        return Response({"status": "success"}, status.HTTP_201_CREATED)

