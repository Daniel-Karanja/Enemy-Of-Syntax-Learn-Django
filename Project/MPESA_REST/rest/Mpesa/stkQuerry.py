
import urllib3
import json

http = urllib3.PoolManager()


conf={
    "BusinessShortCode": 174379,
    "Password": "",
    "Timestamp": "",
    "CheckoutRequestID": ""
  }


def stk_Query(id,password,timestamp,token):
    conf['Password'] =password
    conf['Timestamp'] =timestamp
    conf["CheckoutRequestID"]=id

    url="https://sandbox.safaricom.co.ke/mpesa/stkpushquery/v1/query"
    payload=json.dumps(conf).encode('utf-8')

    res=http.request(method='POST', url=url,body=payload,headers={
        'Content-Type': 'application/json',
        'Authorization':f'Bearer {token}'
    })
    print(res)
    data=json.loads(res.data.decode('utf-8'))
    return data