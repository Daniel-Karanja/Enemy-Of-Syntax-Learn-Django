import urllib3
import json

http = urllib3.PoolManager()



conf={
    "BusinessShortCode": 174379,
    "Password": "",
    "Timestamp": "",
    "TransactionType": "CustomerPayBillOnline",
    "Amount": 0,
    "PartyA": 254,
    "PartyB": 174379,
    "PhoneNumber": 254,
    "CallBackURL": "https://mydomain.com/path",
    "AccountReference": "COMPANY X",
    "TransactionDesc": "Payment of X" 
  }


def stk_push(phone,amount,Password,Timestamp,token):
    conf['Password']=Password
    conf['Timestamp']=Timestamp
    conf['Amount']=amount
    conf['PartyA'] =phone
    conf['PhoneNumber']=phone

    url="https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
    payload=json.dumps(conf).encode('utf-8')

    res=http.request(method='POST', url=url,body=payload,headers={
        'Content-Type': 'application/json',
        'Authorization':f'Bearer {token}'
    })

    print(conf)
    print(payload)

    data=json.loads(res.data.decode('utf-8'))
    return data
