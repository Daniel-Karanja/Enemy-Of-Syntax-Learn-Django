import urllib3
import json
import base64

http = urllib3.PoolManager()


def mpesa_token():
    url='https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'
    

    #encoded = base64.b64encode(b'ConsumerSecret:ConsumerKey')
    encoded = base64.b64encode(b'I9vF5Dh0B94dgdI46yOvQMnq8GvdAsoJ:JXauvzX0QohsHjYX')
    en=encoded.decode('ascii')
  

    res=http.request(method='GET',
     url=url,headers={
        'Authorization':f'Basic {en}'
     })

    data=json.loads(res.data.decode('utf-8'))
    return data
