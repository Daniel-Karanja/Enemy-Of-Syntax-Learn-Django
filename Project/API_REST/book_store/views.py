
from django.shortcuts import render
from django.http import JsonResponse
from .models import Puppies
from .serializer import PuppiesSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
import json

# Create your views here.
@api_view(['GET'])
def get_puppies(request):
    # puppies=[
    #     {
    #       'name':'Angela',
    #       'age':23
    #     },{
    #       'name':'Angela',
    #       'age':23
    #     }
    # ]

    puppies=Puppies.objects.all()
    all_puppies=[]
    print(type(puppies))
    # for puppy in puppies:
    #    all_puppies.append({"name":puppy.name,"age":puppy.age})
    serializer=PuppiesSerializer(puppies,many=True)
    # return JsonResponse(serializer.data,safe=False)
    return Response(serializer.data,status.HTTP_200_OK)


@api_view(['POST'])
def post_puppies(request):

      print(request.method)
      print(request.body)
      # data=json.loads(request.body)
      # print(data)
      # puppy=Puppies(name=data['name'],age=data['age'])
      # puppy.save()
      serializer=PuppiesSerializer(data=request.data)
      
      if serializer.is_valid():
         serializer.save()
         return Response({"status":True,"data":serializer.data},status.HTTP_200_OK)
      return Response({"status":False,"data":"!! Error Saving Data. Check Json Object"},status.HTTP_200_OK)
     