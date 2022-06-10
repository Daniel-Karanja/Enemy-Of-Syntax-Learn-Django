# from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
import urllib3
from .conf import *
import base64
import json

http = urllib3.PoolManager()


@api_view(['GET'])
def get_mpesa_outh(request):
   
    url='https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'
    
    encoded = base64.b64encode(b'GVdEBJvZKR4bGnvFTv76Ooh3XniD5TQi:ugCADwJUOXUoiuuo')
    en=encoded.decode('ascii')

    res=http.request(method='GET',
     url=url,headers={
        'Authorization':f'Basic {en}'
     })

    data=json.loads(res.data.decode('utf-8'))

    return Response({'status':True,'payload':data},status.HTTP_200_OK)