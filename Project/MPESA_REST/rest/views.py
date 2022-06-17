# from django.shortcuts import render
from urllib import request, response
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
import urllib3
from .conf import *
from rest.Mpesa import *


http = urllib3.PoolManager()


@api_view(['GET'])
def get_mpesa_outh(request):
   
   #  url='https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'
    
   #  encoded = base64.b64encode(b'GVdEBJvZKR4bGnvFTv76Ooh3XniD5TQi:ugCADwJUOXUoiuuo')
   #  en=encoded.decode('ascii')

   #  res=http.request(method='GET',
   #   url=url,headers={
   #      'Authorization':f'Basic {en}'
   #   })

   #  data=json.loads(res.data.decode('utf-8'))
    data=mpesa_token()
    return Response({'status':True,'payload':data},status.HTTP_200_OK)

@api_view(['POST'])
def stkPush(request):
    m_time=mpesa_time()
    print(m_time)
    p_key="bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919"
    m_pass=mpesa_password("174379",p_key,m_time)
    token=mpesa_token()
   
    body=request.body
   
    body=json.loads(body)
    phone=body['phone']
    amount=body['amount']

    print(body)
  
    res=stk_push(phone,amount,m_pass,m_time,token['access_token'])

    return Response({'status':True,'payload':res},status.HTTP_200_OK)

@api_view(['POST'])
def stkQuery(request):
    
    m_time=mpesa_time()
    p_key="bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919"
    m_pass=mpesa_password("174379",p_key,m_time)
    token=mpesa_token()

    body=request.body
    body=json.loads(body)
    transaction_id=body['id']
    print(transaction_id)
    res=stk_Query(transaction_id,m_pass,m_time,token['access_token'])
    print(res)
    return Response({'status':True,'payload':res},status.HTTP_200_OK)
    
 
@api_view(['GET'])
def mpesa_time_stamp(request):
    res= mpesa_time()
    
    return Response({'status':True,'payload':res},status.HTTP_200_OK)